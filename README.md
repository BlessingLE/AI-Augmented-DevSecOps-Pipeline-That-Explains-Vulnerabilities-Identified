# 🔐 AI-Augmented DevSecOps Pipeline

This project demonstrates a **CI/CD pipeline enhanced with AI** that not only scans code for vulnerabilities, but also explains them in **simple, developer-friendly language** and suggests **practical fixes**.

---

## 🚀 What This Project Does

Traditional pipelines stop at detecting vulnerabilities.

This pipeline goes further by using AI to:

1. 🔍 Scan code for security vulnerabilities using Bandit  
2. 🧠 Analyze and explain findings in simple terms  
3. ⚠️ Categorize vulnerabilities (Critical / Medium / Low)  
4. 🛠️ Suggest actionable fixes for each issue  

---

## 🧰 Tech Stack

- **Python**
- **Bandit** (Static Application Security Testing)
- **OpenAI / OpenRouter API**
- **GitHub Actions (CI/CD)**

---

## ⚙️ How It Works

```text
Push Code → GitHub Actions Triggered → Bandit Scan Runs → 
Report Generated → AI Analysis → JSON Output with Fixes
```

---

## 🧠 Example AI Output

<img width="523" height="247" alt="image" src="https://github.com/user-attachments/assets/914bc5d3-c42c-43bf-98b3-2b34d40ca542" />

---

## 🖥️ Steps When Running Locally

1. **Clone this Repository**
   ```text
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```
2. **Create a virtual environment**
   ```text
   python -m venv myvenv
   source myvenv/bin/activate   # Linux/Mac
   myvenv\Scripts\activate      # Windows
   ```
3. **Install all dependencies**
   ```text
   pip install -r requirements.txt
   ```
4. **Add your API key**
   - Create an account with (<a href="https://openrouter.ai" target="_blank">OpenRouter<a/>) or (<a href="https://openai.com" target="_blank">OpenAI<a/>) and generate an API Key
   - Create a .env file
   ```text
   OPENROUTER_API_KEY=your_api_key
   OR
   OPENAI_AI_KEY=your_api_key
   ```
   - Make sure to read the docs of your chosen API provider to see how best to make the API call
     
   
6. **Run the scan manually**
   ```text
   bandit -r app/ -f txt -o report.txt
   python analyse.py
   ```
---

## **⚡CI/CD Pipeline (Github Actions)**

The pipeline runs automatically on every push to main:

**Steps:**
1. Checkout code
2. Install dependencies
3. Run Bandit security scan
4. Generate report
5. Run AI analysis
6. Output structured JSON

---

## **🔐 GitHub Secrets Setup**
To run the pipeline:

1. Go to Repository Settings → Secrets → Actions
2. Add your OPENROUTER_API_KEY or your OPENAI_API_KEY

## **📌 Key Features**
* ✅ Fully automated security scanning
* ✅ AI-powered vulnerability explanation
* ✅ Developer-friendly output
* ✅ CI/CD integration
* ✅ Provider-agnostic (OpenAI / OpenRouter)

## **🚧 Future Improvements**
* Add PR comments with AI feedback
* Store results in dashboard (e.g., JSON → UI)
* Integrate Slack/Email alerts
* Support multiple languages (JavaScript, etc.)

## **⭐ Why This Project Matters**
This project demonstrates:
* DevSecOps principles
* CI/CD principles
* AI Integration in real workflows
* Security-focused development
It bridges the gap between **security tools and developer understanding**, making vulnerabilities easier to fix.

## **👩‍💻 Author**
**Name: Blessing Lache-Evandip**<br>
**Email: blessingdevsupport@gmail.com**

