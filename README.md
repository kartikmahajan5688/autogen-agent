# 🧠 AI Mental Health Assistant

A conversational **AI-powered mental health companion** built using **OpenAI**, **AutoGen**, and **Gradio**.
This assistant engages in a **multi-agent dialogue** to:

1. Understand how a user feels (Patient Agent)
2. Analyze emotional tone (Emotion Analysis Agent)
3. Provide personalized self-care and relaxation suggestions (Therapy Recommendation Agent)

> ⚠️ Disclaimer: This project is **not a replacement for professional mental health care**. It is a demo for educational and experimental use only.

---

## 🌟 Features

- 🤖 **Multi-Agent Architecture** using [AutoGen](https://github.com/microsoft/autogen)
- 💬 **Emotion understanding and recommendations** through collaborative AI agents
- 🎨 **Interactive web interface** powered by [Gradio](https://gradio.app)
- 🔒 **Secure API key management** with `.env` and `python-dotenv`
- ⚡ Lightweight, modular, and easy to extend

---

## 🧩 Project Structure

```
AI-Mental-Health-Assistant/
│
├── main.py                     # Main application file
├── requirements.txt            # Project dependencies
├── .env.example                # Example environment variable file
└── README.md                   # Documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kartikmahajan5688/ai-mental-health-assistant.git
cd ai-mental-health-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # On Mac/Linux
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```bash
OPENAI_API_KEY=your_openai_api_key_here
MODEL_ID=gpt-4o-mini
PORT=7860
```

You can use `MODEL_ID=gpt-4o-mini` or another supported model.

---

## 🚀 Run the Application

To launch the **Gradio web app**, simply run:

```bash
python main.py
```

Then, open your browser and visit:

👉 [http://localhost:7860](http://localhost:7860)

---

## 🧠 How It Works

### 🤝 Multi-Agent Flow

1. **Patient Agent** — Accepts the user’s emotional description.
2. **Emotion Analysis Agent** — Analyzes text to detect emotional states (e.g., sadness, anxiety, joy).
3. **Therapy Recommendation Agent** — Suggests coping mechanisms and self-care activities based on the analysis.

All interactions are coordinated by the **GroupChatManager**, which facilitates a round-robin dialogue between the agents to produce the final output.

---

## 🖥️ Interface Preview

**Gradio UI Components:**

- 🧍 Input box — Describe how you feel
- 🔍 Analyze button — Starts the emotional analysis process
- 💬 Output box — Displays the AI’s self-care suggestions

---

## 🧰 Tech Stack

| Component       | Purpose                           |
| --------------- | --------------------------------- |
| **Python 3.9+** | Core programming language         |
| **OpenAI API**  | LLM reasoning and text generation |
| **AutoGen**     | Multi-agent orchestration         |
| **Gradio**      | Web-based UI                      |
| **dotenv**      | Environment variable management   |

---

## ⚠️ Disclaimer

This project is **not intended for clinical use**.
The AI responses are **for informational and self-help purposes only**.
If you are experiencing emotional distress, please seek professional help or contact a local mental health helpline.

---

## 💡 Future Improvements

- 🧩 Integrate sentiment visualization (charts or emoji feedback)
- 🗣️ Add speech-to-text for accessibility
- 🌐 Enable multilingual emotion analysis
- 🧠 Log anonymized chat sessions for behavioral insights (opt-in)

---

## 📜 License

This project is released under the **MIT License**.
You are free to modify and distribute it, provided that credit is given to the original author.

---
