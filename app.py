### app.py

import dotenv
from agents import create_petstore_agent
import gradio as gr

dotenv.load_dotenv()

petstore_agent = create_petstore_agent()


def chat_fn(messages, history):
    result = petstore_agent.invoke({"input": messages})

    output = result["output"]
    steps = result.get("intermediate_steps", [])

    # Format intermediate steps as HTML
    step_messages = []
    for i, step in enumerate(steps):
        tool_name = step[0].tool
        tool_input = step[0].tool_input
        tool_output = step[1]
        step_messages.append(
            f"<b>Step {i+1}</b><br>"
            f"<b>Tool Used:</b> <code>{tool_name}</code><br>"
            f"<b>Input:</b> <code>{tool_input}</code><br>"
            f"<b>Output:</b> <code>{tool_output}</code><br>")

    steps_html = "<br>".join(step_messages)

    # Wrap steps in a collapsible <details> section
    intermediate_html = ""
    if steps_html:
        intermediate_html = (
            f"<details><summary>Intermediate Steps</summary><br>{steps_html}</details><br>"
        )

    # Final response with intermediate steps shown first
    response = (f"{intermediate_html}"
                f"<h4>🐾</h4>{output}")

    return response


demo = gr.ChatInterface(
    chat_fn,
    type="messages",
    title="🐾 Pet Store Agent",
    description=(
        "Interact with the Swagger Pet Store API using an intelligent agent. "
        "Ask about pets by status, tags, or pet details. "
        "Examples: 'Find all available pets' or 'Get details for pet ID 12345'."
    ))

if __name__ == "__main__":
    demo.launch(debug=True, share=True)
