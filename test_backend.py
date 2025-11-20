"""
Test script for the improved NLP/SQL backend
"""
import requests
import json

BASE_URL = "http://localhost:8000"

# Test queries covering various scenarios
test_queries = [
    "Show me all sales",
    "Count sales by product",
    "Total sales by category",
    "Average price per product",
    "Top 10 sales",
    "Show sales data",
    "Sum of quantity",
    "Count of sales by region",
    "Maximum price by category",
]

def test_query(query):
    """Test a single query"""
    print(f"\n{'='*60}")
    print(f"QUERY: {query}")
    print('='*60)
    
    try:
        response = requests.post(
            f"{BASE_URL}/query",
            json={"query": query},
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"SQL Generated: {result.get('sql', 'N/A')}")
            print(f"Results Count: {len(result.get('results', []))}")
            print(f"Chart Type: {result.get('chart_data', {}).get('type', 'N/A')}")
            
            if result.get('results'):
                print(f"\nSample Data (first 3 rows):")
                for row in result['results'][:3]:
                    print(f"  {row}")
            
            if result.get('error'):
                print(f"ERROR: {result['error']}")
            
            return True
        else:
            print(f"HTTP Error: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("ERROR: Cannot connect to backend. Make sure it's running on port 8000")
        return False
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    print("\n" + "="*60)
    print("BACKEND NLP/SQL ENGINE TEST SUITE")
    print("="*60)
    
    # Check if backend is running
    try:
        health = requests.get(f"{BASE_URL}/health", timeout=5)
        if health.status_code == 200:
            print("✓ Backend is running")
        else:
            print("✗ Backend health check failed")
            exit(1)
    except:
        print("✗ Backend is not running. Start it with: cd backend && python main.py")
        exit(1)
    
    # Run all test queries
    passed = 0
    for query in test_queries:
        if test_query(query):
            passed += 1
    
    print(f"\n{'='*60}")
    print(f"RESULTS: {passed}/{len(test_queries)} tests passed")
    print("="*60)
