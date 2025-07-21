### agents.py

from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from tools import petstore_tools
from langchain.agents import create_openai_tools_agent, AgentExecutor


def create_petstore_agent():
    """    Creates a ReAct agent for interacting with the Pet Store API.
    Returns:
        AgentExecutor: The agent executor configured with the Pet Store tools.
    """
    # Initialize the memory
    memory = ConversationBufferMemory(memory_key="chat_history",
                                      return_messages=True)

    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    # Pull or create a ReAct prompt template
    prompt = hub.pull("hwchase17/openai-tools-agent")

    # Create the agent logic
    openai_tools_agent = create_openai_tools_agent(
        llm=llm,  # Pass the LLM
        tools=petstore_tools,  # Pass the tools
        prompt=prompt)  # Pass the prompt

    # Build the agent executor with memory
    agent_executor = AgentExecutor(
        agent=openai_tools_agent,  # Pass the agent logic
        return_intermediate_steps=True,  # Return intermediate steps
        tools=petstore_tools,  # Pass tools to the executor
        memory=memory,  # Pass memory to the executor
        verbose=True,  # Print out the agent's thoughts
        handle_parsing_errors=True,  # Handle parsing errors
        max_iterations=5)  # Max iterations

    return agent_executor
