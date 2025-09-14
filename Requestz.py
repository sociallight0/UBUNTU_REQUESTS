#!/usr/bin/env python3
"""
Requests Library Demonstration
HTTP requests, API interactions, and web scraping basics
"""

import requests
import json
import time
from urllib.parse import urljoin

class APIExplorer:
    """Class to demonstrate various requests operations"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Python-Requests-Demo/1.0'
        })
    
    def basic_get_request(self):
        """Demonstrate basic GET request"""
        print("=== Basic GET Request ===")
        
        try:
            url = "https://httpbin.org/get"
            response = self.session.get(url)
            
            print(f"URL: {url}")
            print(f"Status Code: {response.status_code}")
            print(f"Response Headers: {dict(response.headers)}")
            print(f"Response Content (first 200 chars):")
            print(response.text[:200] + "...")
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def get_with_parameters(self):
        """Demonstrate GET request with parameters"""
        print("\n=== GET Request with Parameters ===")
        
        try:
            url = "https://httpbin.org/get"
            params = {
                'name': 'Python',
                'library': 'requests',
                'version': '2.31'
            }
            
            response = self.session.get(url, params=params)
            data = response.json()
            
            print(f"Request URL: {response.url}")
            print(f"Parameters sent: {data.get('args', {})}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def post_request_demo(self):
        """Demonstrate POST request with data"""
        print("\n=== POST Request Demo ===")
        
        try:
            url = "https://httpbin.org/post"
            data = {
                'username': 'demo_user',
                'email': 'demo@example.com',
                'message': 'Hello from Python requests!'
            }
            
            response = self.session.post(url, data=data)
            result = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"Form data sent: {result.get('form', {})}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def json_post_request(self):
        """Demonstrate POST request with JSON data"""
        print("\n=== JSON POST Request ===")
        
        try:
            url = "https://httpbin.org/post"
            json_data = {
                'user_id': 123,
                'preferences': {
                    'theme': 'dark',
                    'language': 'en'
                },
                'active': True
            }
            
            response = self.session.post(url, json=json_data)
            result = response.json()
            
            print(f"Status Code: {response.status_code}")
            print(f"JSON data sent: {result.get('json', {})}")
            print(f"Content-Type: {result.get('headers', {}).get('Content-Type')}")
            
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def headers_and_auth_demo(self):
        """Demonstrate custom headers and authentication"""
        print("\n=== Headers and Authentication Demo ===")
        
        try:
            url = "https://httpbin.org/headers"
            custom_headers = {
                'X-Custom-Header': 'Python-Demo',
                'X-API-Version': '1.0',
                'Accept': 'application/json'
            }
            
            response = self.session.get(url, headers=custom_headers)
            result = response.json()
            
            print(f"Custom headers sent:")
            sent_headers = result.get('headers', {})
            for key, value in custom_headers.items():
                if key in sent_headers:
                    print(f"  {key}: {sent_headers[key]}")
            
            # Basic auth demo
            print("\nBasic Authentication Demo:")
            auth_url = "https://httpbin.org/basic-auth/demo/password"
            auth_response = self.session.get(auth_url, auth=('demo', 'password'))
            
            if auth_response.status_code == 200:
                print("✓ Authentication successful")
                print(f"Response: {auth_response.json()}")
            else:
                print(f"✗ Authentication failed: {auth_response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def timeout_and_error_handling(self):
        """Demonstrate timeout and error handling"""
        print("\n=== Timeout and Error Handling ===")
        
        # Timeout demo
        try:
            print("Testing timeout (3 seconds)...")
            response = self.session.get("https://httpbin.org/delay/2", timeout=3)
            print(f"✓ Request completed: {response.status_code}")
        except requests.exceptions.Timeout:
            print("✗ Request timed out")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request failed: {e}")
        
        # Error status codes
        try:
            print("\nTesting 404 error handling...")
            response = self.session.get("https://httpbin.org/status/404")
            response.raise_for_status()  # Will raise an exception
        except requests.exceptions.HTTPError as e:
            print(f"✓ HTTP Error caught: {e}")
        except requests.exceptions.RequestException as e:
            print(f"✗ Other error: {e}")
    
    def public_api_demo(self):
        """Demonstrate working with a public API"""
        print("\n=== Public API Demo ===")
        
        try:
            # JSONPlaceholder API
            print("Fetching posts from JSONPlaceholder...")
            posts_url = "https://jsonplaceholder.typicode.com/posts"
            response = self.session.get(posts_url)
            
            if response.status_code == 200:
                posts = response.json()
                print(f"✓ Retrieved {len(posts)} posts")
                
                # Show first 3 posts
                for i, post in enumerate(posts[:3]):
                    print(f"\nPost {i+1}:")
                    print(f"  Title: {post['title']}")
                    print(f"  Body: {post['body'][:50]}...")
                    print(f"  User ID: {post['userId']}")
            
            # Get specific user info
            print(f"\nFetching user info for User ID 1...")
            user_url = "https://jsonplaceholder.typicode.com/users/1"
            user_response = self.session.get(user_url)
            
            if user_response.status_code == 200:
                user = user_response.json()
                print(f"✓ User: {user['name']} ({user['email']})")
                print(f"  Company: {user['company']['name']}")
                print(f"  City: {user['address']['city']}")
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    def session_demo(self):
        """Demonstrate session usage for multiple requests"""
        print("\n=== Session Demo ===")
        
        # Create a new session for this demo
        demo_session = requests.Session()
        demo_session.headers.update({'X-Demo-Session': 'True'})
        
        try:
            # Multiple requests using the same session
            urls = [
                "https://httpbin.org/get?request=1",
                "https://httpbin.org/get?request=2",
                "https://httpbin.org/get?request=3"
            ]
            
            print("Making multiple requests with session...")
            for i, url in enumerate(urls, 1):
                response = demo_session.get(url)
                if response.status_code == 200:
                    print(f"✓ Request {i} successful")
                else:
                    print(f"✗ Request {i} failed: {response.status_code}")
                
                # Small delay between requests
                time.sleep(0.5)
                
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        finally:
            demo_session.close()

def download_file_demo():
    """Demonstrate file downloading"""
    print("\n=== File Download Demo ===")
    
    try:
        # Download a small image
        url = "https://httpbin.org/image/png"
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            filename = "downloaded_image.png"
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✓ File downloaded: {filename}")
            print(f"  Content-Type: {response.headers.get('Content-Type')}")
            print(f"  Size: {len(response.content)} bytes")
        else:
            print(f"✗ Download failed: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    """Main function to run all demonstrations"""
    print("Requests Library Demonstration")
    print("=" * 50)
    
    explorer = APIExplorer()
    
    # Run all demos
    explorer.basic_get_request()
    explorer.get_with_parameters()
    explorer.post_request_demo()
    explorer.json_post_request()
    explorer.headers_and_auth_demo()
    explorer.timeout_and_error_handling()
    explorer.public_api_demo()
    explorer.session_demo()
    download_file_demo()
    
    print("\n" + "=" * 50)
    print("Requests demonstration completed!")
    print("Check for any downloaded files in your directory.")

if __name__ == "__main__":
    main()
