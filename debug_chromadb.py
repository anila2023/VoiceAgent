#!/usr/bin/env python3
"""
Debug ChromaDB import issues
"""

print("Testing ChromaDB import...")

try:
    import chromadb
    print(f"✅ ChromaDB imported successfully: {chromadb.__version__}")
    
    try:
        from chromadb.config import Settings
        print("✅ ChromaDB Settings imported successfully")
    except ImportError as e:
        print(f"❌ ChromaDB Settings import failed: {e}")
        
    # Test client creation
    try:
        client = chromadb.Client()
        print("✅ ChromaDB client created successfully")
        
        # Test collection creation
        collection = client.create_collection("test")
        print("✅ ChromaDB collection created successfully")
        
    except Exception as e:
        print(f"❌ ChromaDB client/collection creation failed: {e}")
        
except ImportError as e:
    print(f"❌ ChromaDB import failed: {e}")

print("\nChecking installed packages:")
import pkg_resources
try:
    chromadb_dist = pkg_resources.get_distribution("chromadb")
    print(f"ChromaDB version: {chromadb_dist.version}")
    print(f"ChromaDB location: {chromadb_dist.location}")
except:
    print("ChromaDB not found in installed packages")

print("\nPython path:")
import sys
for p in sys.path[:5]:  # Show first 5 entries
    print(f"  {p}")