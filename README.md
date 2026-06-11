# Math Chatbot

An AI-powered math assistant built with Streamlit and Google Gemini. Ask any math question and get step-by-step explanations.

## Features
- Conversational chat interface with memory
- Powered by Google Gemini
- Clear chat button to reset conversation
- Responsive wide layout

## Tech Stack
- Python
- Streamlit
- Google Gemini API (`google-genai`)
- python-dotenv

## Setup

1. Clone the repo
```bash
git clone https://github.com/TurboGlitch/math-chatbot
cd math-chatbot
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your Gemini API key
```
GEMINI_API_KEY=your_key_here
```

4. Run the app
```bash
streamlit run app.py
```

## Requirements
```
streamlit
google-genai
python-dotenv
```