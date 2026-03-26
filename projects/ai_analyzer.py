from openai import OpenAI
import requests
from dotenv import load_dotenv
import os

load_dotenv()
Api_key=os.getenv("OPENROUTER_API_KEY")
# print(Api_key)
def analyze_with_ai(log_data):
    prompt = f"""
    You are a cybersecurity expert.

    Analyze login activity:

    Failed: {log_data['failed']}
    Success: {log_data['success']}
    IPs: {log_data['ips']}

    Is this normal or suspicious? Explain briefly.
    """
    # response=client.chat.completions.create(
    #     model="meta-llama/llama-3-8b-instruct",
    #     messages=[{"role":"user","content":prompt}]
    # )
    response=requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {Api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-3-8b-instruct",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
    )
    try:

        data=response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        print("ERROR:",e)
        print("RESPONSE:",response.text)
        return "AI analysis failed"