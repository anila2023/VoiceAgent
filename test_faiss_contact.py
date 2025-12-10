#!/usr/bin/env python3
"""
Test contact search with FAISS
"""

import sys
from pathlib import Path

# Add project root to path  
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from rag_agent.tools.faiss_search_tools import get_faiss_manager

print("Loading FAISS manager...")
manager = get_faiss_manager()
print("Searching for contact details...")
results = manager.search_documents('phone number contact details', top_k=3)

print("🔍 Contact Search Results:")
for i, r in enumerate(results):
    print(f"\n{i+1}. {r['metadata']['source']} (score: {r['score']:.3f})")
    print(f"   {r['content'][:150]}...")