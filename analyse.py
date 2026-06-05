from dotenv import load_dotenv
import os
import json
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("report.txt", "r", encoding="utf-16") as file:
    report = file.read()

conversation= []

prompt = f"""
    You are a Cybersecurity SOC analyst.

    Read the following Bandit security report and return ONLY valid JSON.

    Do NOT include explanations outside JSON.
    Do NOT use markdown.

    Structure must be:

    {
    "critical": [
        {
        "issue": "",
        "meaning": "",
        "risk": "",
        "fix": ""
        }
    ],
    "medium": [],
    "low": []
    }

    Rules:
    - Group all issues correctly
    - Keep explanations simple and developer-friendly
    - If no issues exist in a category, return an empty list

    Here is the report:
    {report}
"""

conversation.append({
    "role":"user",
    "content":prompt
})

request = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=conversation
)

ai_response = request.choices[0].message.content

ai_response = ai_response.replace("```json", "").replace("```", "")  #removing any markdown and extra text from ai reponse before parsing to json

parsed = json.loads(ai_response)

conversation.append({
    "role":"assistant",
    "content":parsed
})

print(parsed)