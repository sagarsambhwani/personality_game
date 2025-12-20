import requests
import json
import sys

# Use localhost
url = "http://localhost:8000/api/v1/personality/analyze"
health_url = "http://localhost:8000/api/v1/personality/health"

payload = {
  "name": "Sagar",
  "age": 25,
  "gender": "Male",
  "profession": "Data Engineer",
  "nationality": "Indian"
}
headers = {'Content-Type': 'application/json'}

def test_api():
    print(f"\nTesting Health Endpoint: {health_url}")
    try:
        resp = requests.get(health_url)
        print(f"Health Status: {resp.status_code}")
        print(resp.json())
    except Exception as e:
        print(f"Health Check Failed: {e}")
        return

    print(f"\nTesting Analyze Endpoint: {url}")
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("Response JSON (truncated):")
            data = response.json()
            # Truncate long fields for display
            if 'final_response' in data:
                print(f"Final Response: {str(data['final_response'])[:100]}...")
            if 'profile' in data:
                print(f"Profile: {data['profile']}")
            print("Success!")
        else:
            print("Error Response:")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
