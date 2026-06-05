from dotenv import load_dotenv
import os
from openai import OpenAI


 #   This file is meant to be a mock AI simulator just testing purposes.
 #   The Analyse is hardcoded in this file to test the capablilities of Pipeline
 #   To run pipeline on actual AI analysis, use analyse.py

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("report.txt", "r", encoding="utf-8", errors="ignore") as file:
    report = file.read()

def mock_ai_analyze(report: str) -> str:
    return f"""
================ SECURITY ANALYSIS REPORT ================

🔴 CRITICAL ISSUES
- subprocess usage or exec detected (if present)
  • What it means: Code is executing system-level commands
  • Why dangerous: Can allow remote code execution
  • Fix: Validate inputs, avoid exec/subprocess where possible

🟠 MEDIUM ISSUES
- Weak hashing or insecure imports (if present)
  • What it means: Security primitives are outdated
  • Why dangerous: Can lead to data compromise
  • Fix: Use hashlib.sha256 or secure libraries

🟡 LOW ISSUES
- assert statements used in production code
  • What it means: Assertions may be stripped in optimized mode
  • Why dangerous: Logic checks may disappear in production
  • Fix: Replace assert with proper error handling

==========================================================
RAW REPORT SUMMARY:
{report[:1000]}...

==========================================================
"""

analysis = mock_ai_analyze(report)

print(analysis)

#saving the analysis report in a file
with open("analysis_output.txt", "w", encoding="utf-16") as f:
    f.write(analysis)