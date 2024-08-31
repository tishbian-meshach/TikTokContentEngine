import requests

# Replace 'your_huggingface_api_key' with your actual Hugging Face API key
API_KEY = 'HUGGINGFACE_API_KEY'
API_URL = 'https://api-inference.huggingface.co/models/facebook/bart-large-cnn'

headers = {
    'Authorization': f'Bearer {API_KEY}'
}

def generate_content(text):
    response = requests.post(API_URL, headers=headers, json={"inputs": text})
    
    if response.status_code == 200:
        # The response usually contains a list of dictionaries with a 'summary_text' key
        generated_text = response.json()[0].get('summary_text', '')
        cta_text = "Follow for more content!"
        full_content = f"{generated_text}\n\n{cta_text}"
        return full_content
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")