### app.py

import dotenv
from agents import create_petstore_agent
import gradio as gr

dotenv.load_dotenv()

petstore_agent = create_petstore_agent()


def chat_fn(messages, history):
    result = petstore_agent.invoke({"input": messages})
    return result["output"]


demo = gr.ChatInterface(
    chat_fn,
    type="messages",
    title="🐾 Pet Store Agent",
    description=
    ("Interact with the Swagger Pet Store API using a ReAct agent. "
     "Add, update, or delete pets. Ask about pets by status, tags, or specific pet details. "
     "For example, you can ask 'Find all available pets' or 'Get details for pet ID 12345'."
     ))

if __name__ == "__main__":
    demo.launch(debug=True, share=True)
