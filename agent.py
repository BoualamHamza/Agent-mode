# agent.py
import os
import logging
# Ensure an LLM is installed, e.g., Ollama and a model like llama2
# pip install langchain langchain_community ollama
# ollama pull llama2
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import Ollama

from tools.file_system import read_file, write_file
from tools.shell import run_command
from tools.testing import run_tests
from tools.git import git_commit

# --- Logging Configuration ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.FileHandler("agent.log"), # Log to a file
        logging.StreamHandler()          # Log to console
    ]
)
logger = logging.getLogger(__name__)

# --- LLM Configuration ---
llm = None
try:
    llm = Ollama(model="llama2")
    llm.invoke("Hello, world!") 
    logger.info("Ollama LLM configured successfully.")
except Exception as e:
    logger.error(f"Failed to initialize Ollama LLM: {e}")
    llm = None

# --- Tool Definition ---
tools = [
    Tool(
        name="ReadFile",
        func=read_file,
        description="Reads the content of a specified file. Input should be a valid file path."
    ),
    Tool(
        name="WriteFile",
        func=lambda params: write_file(path=params.split(',')[0].strip(), content=",".join(params.split(',')[1:]).strip()),
        description="Writes content to a specified file. Input should be a file path and the content to write, separated by a comma (e.g., 'path/to/file.txt, new file content')."
    ),
    Tool(
        name="RunShellCommand",
        func=run_command,
        description="Executes a shell command. Input should be the command string. Use with caution. Prohibited commands: 'rm -rf', 'sudo'."
    ),
    Tool(
        name="RunTests",
        func=run_tests,
        description="Runs the project's test suite. Input is ignored. This tool will report success or failure of the test run."
    ),
    Tool(
        name="GitCommit",
        func=lambda params: git_commit(message=params.split(',')[0].strip(), branch_name=params.split(',')[1].strip() if len(params.split(',')) > 1 else "main"),
        description="Commits changes to the git repository. Input should be the commit message, optionally followed by a comma and the branch name. Ensure files are staged first if needed."
    )
]

# --- Agent Initialization ---
agent = None
if llm:
    try:
        agent = initialize_agent(
            tools,
            llm,
            agent="zero-shot-react-description",
            verbose=True, # LangChain's own verbose logging
            handle_parsing_errors=True
        )
        logger.info("LangChain agent initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing LangChain agent: {e}")
        agent = None
else:
    logger.warning("LLM not available, LangChain agent cannot be initialized.")


# --- Agent Task Execution ---
def run_agent_task(prompt: str):
    if not agent:
        logger.error("Agent not initialized. Cannot run task.")
        return
    if not llm:
        logger.error("LLM not configured. Agent cannot run task.") # Should be redundant
        return

    logger.info(f"--- Running Agent with Prompt ---")
    logger.info(f"User Prompt: {prompt}")
    try:
        # The agent.invoke method is generally preferred for newer LangChain versions
        response = agent.invoke({"input": prompt})
        final_output = response.get('output', 'No output field found.')
        logger.info(f"--- Agent Execution Finished ---")
        logger.info(f"Final Response: {final_output}")
    except Exception as e:
        logger.error(f"Error during agent execution: {e}", exc_info=True) # exc_info=True logs stack trace
        if "Could not parse LLM output" in str(e):
            logger.warning("This often means the LLM's response wasn't in the expected format for the ReAct agent.")

if __name__ == "__main__":
    if agent:
        logger.info("--- Agent Ready ---")
        logger.info(f"Available tools: {[tool.name for tool in tools]}")
        
        task_prompt = "Write a brief summary of the project goals into a new file called 'summary.txt'."
        # task_prompt = "Read the README.md file and tell me what it is about."
        # task_prompt = "Create a new file named 'hello.txt' with the content 'Hello, agent world!', then read this file and show me its content."
        run_agent_task(task_prompt)
    else:
        logger.critical("Agent initialization failed. Cannot run tasks. Ensure LLM (e.g., Ollama) is running and configured.")
