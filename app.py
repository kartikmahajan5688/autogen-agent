from openai import OpenAI
from autogen import ConversableAgent, GroupChat, GroupChatManager
import gradio as gr
import os
import warnings
import logging
from dotenv import load_dotenv

# ---- Suppress warnings ----
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
logging.getLogger("autogen.oai.client").setLevel(logging.ERROR)

# ---- Load environment variables ----
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_ID = os.getenv("MODEL_ID", "gpt-4o-mini")

# ---- Initialize LLM config ----
llm_config = {"config_list": [{"model": MODEL_ID, "api_key": OPENAI_API_KEY}]}

# ---- Define Agents ----
patient_agent = ConversableAgent(
    name="patient",
    system_message="You describe your emotions and mental health concerns.",
    llm_config=llm_config
)

emotion_analysis_agent = ConversableAgent(
    name="emotion_analysis",
    system_message=(
        "You analyze the user's emotions based on their input. "
        "Do not provide treatment or self-care advice. "
        "Instead, just summarize the dominant emotions they may be experiencing."
    ),
    llm_config=llm_config
)

therapy_recommendation_agent = ConversableAgent(
    name="therapy_recommendation",
    system_message=(
        "You suggest relaxation techniques and self-care methods "
        "only based on the analysis from the Emotion Analysis Agent. "
        "Do not analyze emotions—just give recommendations based on the prior response."
    ),
    llm_config=llm_config
)

# ---- Create Group Chat ----
groupchat = GroupChat(
    agents=[emotion_analysis_agent, therapy_recommendation_agent],
    messages=[],
    max_round=3,
    speaker_selection_method="round_robin"
)
manager = GroupChatManager(name="manager", groupchat=groupchat)

# ---- Core logic function ----


def chat_response(user_input):
    """Handles the full AI interaction flow and returns only the final recommendation."""
    try:
        # Clear old messages
        groupchat.messages.clear()

        # Run conversation
        patient_agent.initiate_chat(
            manager,
            message=f"I have been feeling {user_input}. Can you help?"
        )

        messages = getattr(groupchat, "messages", [])
        if not messages:
            return "No messages captured from group chat."

        # Find the *last* message from therapy_recommendation
        final_response = None
        for m in reversed(messages):
            # dict-based format
            if isinstance(m, dict):
                if m.get("name") == "therapy_recommendation":
                    final_response = m.get("content", "")
                    break
            # object-based format
            elif hasattr(m, "name") and hasattr(m, "content"):
                if m.name == "therapy_recommendation":
                    final_response = m.content
                    break

        # fallback: if no therapy_recommendation message found, return last non-patient
        if not final_response:
            for m in reversed(messages):
                if isinstance(m, dict) and m.get("name") != "patient":
                    final_response = m.get("content", "")
                    break
                elif hasattr(m, "name") and m.name != "patient":
                    final_response = m.content
                    break

        return final_response or "No AI response found."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


# ---- Gradio UI ----


def gradio_interface(user_input):
    return chat_response(user_input)


with gr.Blocks(theme=gr.themes.Soft(), title="AI Mental Health Assistant") as demo:
    gr.Markdown(
        "## 🧠 AI Mental Health Chatbot\nDescribe how you're feeling, and the AI will analyze and recommend self-care tips.")
    with gr.Row():
        with gr.Column():
            user_input = gr.Textbox(
                label="How are you feeling today?",
                placeholder="e.g., I’ve been feeling anxious and tired lately..."
            )
            submit_btn = gr.Button("Analyze & Recommend")
        with gr.Column():
            output = gr.Textbox(label="AI Response", lines=10)

    submit_btn.click(fn=gradio_interface, inputs=user_input, outputs=output)

# ---- Launch the Gradio app ----
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )


# if __name__ == "__main__":
#     demo.launch()
