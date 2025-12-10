#!/usr/bin/env python3
"""
Test FAISS vector search functionality
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_faiss_imports():
    """Test if FAISS can be imported"""
    try:
        import faiss
        print("✅ FAISS imported successfully")
        return True
    except ImportError as e:
        print(f"❌ FAISS import failed: {e}")
        return False

def test_faiss_search_imports():
    """Test if FAISS search tools can be imported"""
    try:
        from rag_agent.tools.faiss_search_tools import FAISSPolicyManager, faiss_search_documents
        print("✅ FAISS search tools imported successfully")
        return True
    except ImportError as e:
        print(f"❌ FAISS search tools import failed: {e}")
        return False

def test_faiss_manager_init():
    """Test if FAISSPolicyManager can be initialized"""
    try:
        from rag_agent.tools.faiss_search_tools import FAISSPolicyManager
        manager = FAISSPolicyManager()
        print("✅ FAISSPolicyManager initialized successfully")
        print(f"  - Database path: {manager.vector_db_path}")
        print(f"  - Raw policies dir: {manager.raw_policies_dir}")
        print(f"  - Current index size: {manager.index.ntotal if manager.index else 0}")
        return manager
    except Exception as e:
        print(f"❌ FAISSPolicyManager initialization failed: {e}")
        return None

def test_search_assistant():
    """Test if search assistant can be created with FAISS tools"""
    try:
        from rag_agent.agents.search_assistant import create_search_assistant_agent
        agent = create_search_assistant_agent()
        print("✅ Search assistant created successfully")
        
        # Check tools
        tool_names = [tool.name for tool in agent.tools]
        print(f"  - Available tools: {tool_names}")
        
        return True
    except Exception as e:
        print(f"❌ Search assistant test failed: {e}")
        return False

def test_document_indexing():
    """Test document indexing if raw policies exist"""
    try:
        from rag_agent.tools.faiss_search_tools import get_faiss_manager
        manager = get_faiss_manager()
        
        # Check for documents
        raw_dir = manager.raw_policies_dir
        if raw_dir.exists():
            txt_files = list(raw_dir.glob("*.txt"))
            json_files = list(raw_dir.glob("*.json"))
            print(f"📄 Found {len(txt_files)} .txt files and {len(json_files)} .json files")
            
            if txt_files or json_files:
                print("🔄 Testing document indexing...")
                result = manager.index_documents()
                print(f"  - Indexing result: {result}")
                return True
            else:
                print("📝 No documents to index (add .txt or .json files to data/raw_policies/)")
        else:
            print(f"📁 Raw policies directory doesn't exist: {raw_dir}")
        
        return True
    except Exception as e:
        print(f"❌ Document indexing test failed: {e}")
        return False

def test_search():
    """Test search functionality"""
    try:
        from rag_agent.tools.faiss_search_tools import get_faiss_manager
        manager = get_faiss_manager()
        
        if manager.index.ntotal > 0:
            print("🔍 Testing search...")
            results = manager.search_documents("contact information", top_k=3)
            print(f"  - Found {len(results)} results for 'contact information'")
            
            if results:
                print(f"  - Top result similarity: {results[0]['score']:.3f}")
                print(f"  - Top result source: {results[0]['metadata']['source']}")
        else:
            print("🔍 No documents indexed, skipping search test")
        
        return True
    except Exception as e:
        print(f"❌ Search test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Testing FAISS Vector Search Integration\n")
    
    # Test 1: FAISS import
    print("1. Testing FAISS imports...")
    if not test_faiss_imports():
        return
    
    # Test 2: FAISS search tools import
    print("\n2. Testing FAISS search tools imports...")
    if not test_faiss_search_imports():
        return
    
    # Test 3: Manager initialization
    print("\n3. Testing FAISSPolicyManager initialization...")
    manager = test_faiss_manager_init()
    if not manager:
        return
    
    # Test 4: Search assistant
    print("\n4. Testing search assistant with FAISS tools...")
    if not test_search_assistant():
        return
    
    # Test 5: Document indexing
    print("\n5. Testing document indexing...")
    if not test_document_indexing():
        return
    
    # Test 6: Search
    print("\n6. Testing search...")
    if not test_search():
        return
    
    print("\n🎉 All tests passed! FAISS vector search is ready to use.")
    print("\nNext steps:")
    print("- Add .txt or .json policy files to data/raw_policies/ for indexing")
    print("- Use 'index documents' command to add them to FAISS database")
    print("- Try semantic searches like 'find contact information' or 'claims process'")

if __name__ == "__main__":
    main()