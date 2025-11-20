import os
import google.generativeai as genai
from dotenv import load_dotenv
from pathlib import Path

# Load .env
env_path = Path('backend/.env')
load_dotenv(dotenv_path=env_path)

api_key = os.getenv('GEMINI_API_KEY')
print(f"API Key found: {'Yes' if api_key else 'No'}")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        print("Sending test query...")
        response = model.generate_content("Say 'Hello World'")
        print(f"Response: {response.text}")
        print("✅ API Connection Successful!")
    except Exception as e:
        print(f"❌ API Connection Failed: {e}")
        import traceback
        traceback.print_exc()
else:
    print("❌ No API Key found in backend/.env")
