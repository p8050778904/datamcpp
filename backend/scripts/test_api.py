import httpx

BASE_URL = "http://127.0.0.1:8000/api"

queries = [
    "Give me sales by region",
    "Show brand performance",
    "Top employees by revenue"
]

def test_query(query):
    print(f"\nTesting query: {query}")
    try:
        response = httpx.post(f"{BASE_URL}/query", json={"query": query})
        if response.status_code == 200:
            data = response.json()
            print(f"Title: {data.get('title')}")
            print(f"Chart Type: {data.get('chart_type')}")
            print(f"Data Sample (first 2): {data.get('data')[:2]}")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Connection Error: {e}")

if __name__ == "__main__":
    for q in queries:
        test_query(q)
