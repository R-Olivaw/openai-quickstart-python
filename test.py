import os, requests, json
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

url = "https://api.openai.com/v1/models/text-curie-001"

#session_id = requests.post(url, headers={"Authorization": f"Bearer {openai.api_key}"}).json()["session"]

prompt = (
    "My name is Alex!"
)

params = {
    "prompt": prompt,
    "model": "text-curie-001",
    "max_tokens": 75,
    "temperature": 0.5,
}

headers = {"Authorization": f"Bearer {openai.api_key}"}
response = requests.post(url, json=params, headers=headers)

print(json.dumps(response.json(), indent=2))

prompt = (
    "What's my name?"
)

params = {
    "prompt": prompt,
    "model": "text-curie-001",
    "max_tokens": 75,
    "temperature": 0.5,
}

headers = {"Authorization": f"Bearer {openai.api_key}"}
response = requests.post(url, json=params, headers=headers)

print(json.dumps(response.json(), indent=2))