from openai import OpenAI
import requests

Api_key="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"
# client = OpenAI(api_key="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")

def analyze_with_ai(log_data):
    prompt = f"""
    You are a cybersecurity expert.

    Analyze this log data:
    {log_data}

    Tell:
    - Is there an attack?
    - Targeted user?
    - Type of attack?
    - Recommended action?
    # """
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

        return response.json()['choices'][0]['message']['content']
    except:
        return "AI analysis failed"