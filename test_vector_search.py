#!/usr/bin/env python3
"""
Test ChromaDB vector search functionality
"""

import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_vector_search_imports():
    """Test if vector search can be imported"""
    try:
        from rag_agent.tools.vector_search_tools import VectorPolicyManager, enhanced_search_tool
        print("✅ Vector search imports successful")
        return True
    except ImportError as e:
        print(f"❌ Vector search import failed: {e}")
        return False

def test_vector_manager_init():
    """Test if VectorPolicyManager can be initialized"""
    try:
        from rag_agent.tools.vector_search_tools import VectorPolicyManager
        manager = VectorPolicyManager()
        print("✅ VectorPolicyManager initialized successfully")
        print(f"  - Database path: {manager.db_path}")
        print(f"  - Raw policies dir: {manager.raw_policies_dir}")
        return manager
    except Exception as e:
        print(f"❌ VectorPolicyManager initialization failed: {e}")
        return None

def test_chromadb_collection():
    """Test ChromaDB collection creation"""
    try:
        from rag_agent.tools.vector_search_tools import VectorPolicyManager
        manager = VectorPolicyManager()
        
        # Test collection creation
        collection = manager._get_or_create_collection()
        count = collection.count()
        print(f"✅ ChromaDB collection accessible, documents: {count}")
        
        # If empty, try to index some documents
        if count == 0:
            print("📄 Collection empty, checking for documents to index...")
            if manager.raw_policies_dir.exists():
                documents = list(manager.raw_policies_dir.glob("*.txt"))
                print(f"  - Found {len(documents)} .txt files in raw_policies")
                if documents:
                    result = manager.index_documents()
                    print(f"  - Indexing result: {result}")
            else:
                print(f"  - Raw policies directory not found: {manager.raw_policies_dir}")
        
        return True
    except Exception as e:
        print(f"❌ ChromaDB collection test failed: {e}")
        return False

def test_search_assistant():
    """Test if search assistant can be created with vector tools"""
    try:
        from rag_agent.agents.search_assistant import SearchAssistantAgent
        agent = SearchAssistantAgent()
        print("✅ Search assistant created successfully")
        
        # Check tools
        tool_names = [tool.name for tool in agent.tools]
        print(f"  - Available tools: {tool_names}")
        
        return True
    except Exception as e:
        print(f"❌ Search assistant test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Testing ChromaDB Vector Search Integration\n")
    
    # Test 1: Imports
    print("1. Testing imports...")
    if not test_vector_search_imports():
        return
    
    # Test 2: Manager initialization
    print("\n2. Testing VectorPolicyManager initialization...")
    manager = test_vector_manager_init()
    if not manager:
        return
    
    # Test 3: ChromaDB collection
    print("\n3. Testing ChromaDB collection...")
    if not test_chromadb_collection():
        return
    
    # Test 4: Search assistant
    print("\n4. Testing search assistant with vector tools...")
    if not test_search_assistant():
        return
    
    print("\n🎉 All tests passed! Vector search is ready to use.")
    print("\nNext steps:")
    print("- Add .txt policy files to data/raw_policies/ for indexing")
    print("- Use 'index documents' command to add them to vector database")
    print("- Try semantic searches like 'find contact information' or 'claims process'")

if __name__ == "__main__":
    main()