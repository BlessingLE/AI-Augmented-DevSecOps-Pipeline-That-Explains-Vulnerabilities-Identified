from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("report.txt", "r", encoding="utf-16") as file:
    report = file.read()

conversation= []

prompt = f"""
    You are a Cybersecurity SOC analyst. Read and explain the following Bandit security report in simple terms for a software developer to understand the security issues. 
    Group the issues into: Critical / Medium /  Low. 

    Also explain the following for each issue:
    1. What the issue meas
    2. Why the issue is dangerous
    3. How the issue can be fixed

    Here is the report: {report}
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

conversation.append({
    "role":"assistant",
    "content":ai_response
})

print(ai_response)