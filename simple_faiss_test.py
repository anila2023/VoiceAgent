#!/usr/bin/env python3
"""
Simple FAISS indexing test
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def main():
    print("🔄 Testing FAISS indexing...")
    
    try:
        from rag_agent.tools.faiss_search_tools import get_faiss_manager
        manager = get_faiss_manager()
        
        print("📄 Indexing documents...")
        result = manager.index_documents()
        print(f"Result: {result}")
        
        print("🔍 Testing search...")
        search_results = manager.search_documents("contact information", top_k=2)
        print(f"Found {len(search_results)} results")
        
        for i, result in enumerate(search_results):
            print(f"\n{i+1}. {result['metadata']['source']} (score: {result['score']:.3f})")
            print(f"   {result['content'][:200]}...")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()