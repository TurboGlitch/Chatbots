# AI Streamlit Apps

A collection of AI-powered apps built with Streamlit and Google Gemini.

---

## 🧮 Math Chatbot

An AI-powered math assistant. Ask any math question and get step-by-step explanations.

**Features**
- Conversational chat interface with memory
- Powered by Google Gemini
- Clear chat button to reset conversation
- Responsive wide layout

**Run it**
```bash
streamlit run app.py
```

---

## 🌐 Website Builder

An AI-powered website builder chatbot. Describe the website you want in plain English, and watch it get built and rendered live in a preview pane, side by side with the chat.

https://chatbots-asnyd7dw3knbqksbbbrup7.streamlit.app/

**Features**
- Conversational chat interface with memory
- Generates complete HTML/CSS/JS from natural language prompts
- Live preview rendered in a sandboxed iframe
- Iteratively edit your site — ask for changes and the preview updates
- Clear chat button to start fresh
- Responsive wide layout

**Run it**
```bash
streamlit run bots/websitedisplay.py
```

---

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

4. Run whichever app you want (see above)

## Requirements
```
streamlit
google-genai
python-dotenv
```
