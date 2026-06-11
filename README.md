# 🧮 Math Chatbot

A sleek, conversational AI interface built with Streamlit and powered by Google's Gemini API (`gemini-3.1-flash-lite-preview`). This chatbot is specifically instructed to assist users with all levels of mathematical inquiries while maintaining a polite and focused demeanor.

## ✨ Features
* **Math Focused:** Driven by system instructions to strictly discuss mathematics and refuse off-topic prompts.
* **Custom Dark UI:** Tailored sidebar layouts with customized CSS typography and dynamic component hover-states.
* **Session State Memory:** Maintains a continuous conversation history during your active user session.
* **Quick Actions:** A "Clear Chat" utility button in the sidebar to wipe the session history instantly.
* **Optimized Performance:** Utilizes quick toast responses and status spinners for an interactive user experience.

---

## 🛠️ Installation & Setup

Follow these steps to run the application locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/TurboGlitch/Chatbots.git](https://github.com/TurboGlitch/Chatbots.git)
cd Chatbots


Set Up a Virtual Environment (Recommended)
# Create virtual environment
python -m venv venv

# Activate it
# On Windows (Command Prompt/Git Bash):
source venv/Scripts/activate
# On Mac/Linux:
source venv/bin/activate


Install Dependencies
Make sure you have your dependencies installed:

pip install streamlit python-dotenv google-genai



Environment Configuration
Create a .env file in the root folder of your project to securely store your API keys:

GEMINI_API_KEY=your_actual_gemini_api_key_here

🚀 Running the App

streamlit run app.py