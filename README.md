# AI Coding Agent (LangChain, Python)

This project is an AI-powered coding assistant built using Python and LangChain. It's designed to understand high-level coding prompts, interact with a codebase, and perform tasks like file manipulation, command execution, and version control.

## 🚀 Quick Start

### Prerequisites

1.  **Python:** Ensure you have Python 3.8+ installed.
2.  **Ollama:** This agent uses [Ollama](https://ollama.com/) to run local LLMs.
    *   Install Ollama on your system.
    *   Pull a model that the agent will use, for example, Llama 2:
        ```bash
        ollama pull llama2
        ```
    *   Ensure Ollama is running before starting the agent.
3.  **Git:** Git must be installed and configured for the `GitCommit` tool to function.

### Setup & Installation

1.  **Clone the repository:**
    ```bash
    # If you are working within a git-managed environment already, skip this.
    # git clone <repository_url>
    # cd <repository_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Agent

Execute the main agent script:

```bash
python agent.py
```

By default, this will run a pre-defined task (e.g., summarizing project goals into `summary.txt`). You can modify the `task_prompt` variable in the `if __name__ == "__main__":` block in `agent.py` to change the agent's objective.

### Logging

*   The agent's thought process (if using a ReAct agent with `verbose=True`) will be printed to the console.
*   Detailed logs are also saved to `agent.log`.

## 🛠️ Implemented Tools

The agent currently has access to the following tools:

*   **ReadFile:** Reads content from a specified file.
*   **WriteFile:** Writes content to a specified file.
*   **RunShellCommand:** Executes shell commands (with basic safety checks).
*   **RunTests:** A stub function to simulate running project tests.
*   **GitCommit:** Commits changes to the Git repository.

## 🤖 Agent Architecture

*   **Core Logic:** `agent.py` orchestrates the agent's operations.
*   **LLM Integration:** Uses LangChain to interface with an LLM (defaults to Ollama with a model like Llama 2).
*   **Tooling:** Custom tools are defined in the `tools/` directory (`file_system.py`, `shell.py`, `testing.py`, `git.py`).
*   **Workflow:** Employs a ReAct-style agent loop (plan, act, observe) provided by LangChain.

---
## 📚 Initial Research & Roadmap Ideas

# Agent-mode (Original Title)
## Overview

Building a coding agent like Claude Code or GitHub Copilot Agent Mode involves integrating a large language model (LLM) with tools that allow it to read, modify, and interact with codebases, automate coding workflows, and execute commands. These agents can perform tasks such as generating code, refactoring, running tests, and even managing project files autonomously[3][5][8].

Below is a structured guide to building your own coding agent, drawing from available best practices and technical resources.

---

## Key Components of a Coding Agent

- **Language Model Integration**: Use a powerful LLM (e.g., Claude, GPT-4/4o, or similar) as the core reasoning and code generation engine[6][7].
- **Tooling and Environment Access**: Provide the agent with programmatic access to your codebase, terminal, version control (e.g., git), and other developer tools[3][5][12].
- **Agentic Loop**: Implement an iterative workflow where the agent can plan, execute, observe results, and self-correct, similar to how Copilot Agent Mode or Claude Code operate[3][5].
- **User Interface**: Integrate into an IDE (like VS Code), terminal, or web interface for user interaction and oversight[3][5][8].

---

## Step-by-Step Guide

**1. Choose Your LLM and Framework**

- Obtain API access to a suitable LLM (Claude, GPT-4, etc.)[6][7].
- Use agent frameworks like [LangChain](https://github.com/hwchase17/langchain) or build your own orchestration layer in Python or Node.js[6].

**2. Set Up the Agent’s Environment**

- Give the agent access to:
  - The file system (to read and write code)
  - Terminal commands (to run tests, install dependencies, etc.)
  - Version control (to commit, branch, or revert changes)[3][5][8][12]
- For safety, restrict permissions or run the agent in a sandbox/container, especially if allowing autonomous command execution[3].

**3. Implement Agentic Workflows**

- **Iterative Coding Loop**:
  - Accept a user prompt (e.g., "Add a login page").
  - The agent analyzes the codebase, plans changes, and proposes edits.
  - Applies changes, runs tests or builds, and observes results.
  - Iterates until the task is complete or user intervenes[3][5].
- **Testing and Validation**:
  - Use test-driven development: have the agent write tests, then code to pass the tests, iterating as needed[3].
  - Allow the agent to run and interpret test results, making further changes if tests fail[3][5].

**4. Tool Integration**

- Integrate with IDEs (VS Code, JetBrains, etc.) using extensions or plugins for seamless developer experience[5][8].
- Optionally, expose additional tools (e.g., browser automation for UI tasks, documentation generators, linters)[3][5].

**5. User Oversight and Safety**

- Provide transparency for every action (e.g., show proposed edits, require approval for terminal commands)[5].
- Support undo/rollback for agent actions[5].
- Optionally, allow "safe YOLO mode" for fully autonomous operation in a controlled environment[3].

---

## Example: Minimal Python Agent with LangChain

```python
from langchain.llms import OpenAI
from langchain.agents import initialize_agent, Tool

# Define tools the agent can use
def run_tests():
    # Implement logic to run tests and return results
    pass

tools = [
    Tool(name="run_tests", func=run_tests, description="Run project tests"),
    # Add more tools as needed
]

llm = OpenAI(api_key="YOUR_API_KEY")
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")

# Run the agent with a user prompt
result = agent.run("Add a user authentication system and write tests for it.")
print(result)
```
This is a simplified example; production agents require more robust file management, error handling, and user interface integration[6].

---

## Best Practices

- **Iterate and Validate**: Let the agent propose, test, and refine changes in cycles[3][5].
- **Explicit Prompts**: Be clear and specific in instructions to the agent for best results[3].
- **Safety First**: Use containers or virtual environments when granting autonomous command execution[3].
- **Transparency**: Always log and display agent actions for user review and intervention[5].

---

## Open-Source and Reference Projects

- **Claude Code**: [GitHub repo](https://github.com/anthropics/claude-code) – a terminal-based agentic coding tool[8].
- **GPTutor**: An open-source AI pair programming tool as an alternative to Copilot[13].
- **LangChain**: Popular framework for building LLM-powered agents with tool integration[6].

---

## Summary Table: Core Features

| Feature                   | Claude Code              | Copilot Agent Mode         | DIY Agent (e.g., LangChain)      |
|---------------------------|--------------------------|----------------------------|----------------------------------|
| LLM Integration           | Claude models            | OpenAI/Anthropic models    | Any (Claude, GPT, etc.)          |
| IDE Integration           | Terminal, CLI            | VS Code                    | Custom (terminal, web, IDE)      |
| Autonomy                  | High (with safeguards)   | High (with user oversight) | Configurable                     |
| Tool Access               | File, terminal, git      | File, terminal, git        | Customizable                     |
| Open Source               | Yes                      | No                         | Yes (LangChain, GPTutor, etc.)   |

---

By combining a strong LLM, tool integrations, and iterative workflows, you can build a coding agent that approaches the capabilities of Claude Code or Copilot Agent Mode. For a hands-on walkthrough, see tutorials like "Build an AI Agent From Scratch in Python" on YouTube[6], and consult the documentation for Claude Code and LangChain for advanced features[3][8].

Citations:
[1] https://www.reddit.com/r/ChatGPTCoding/comments/1jqoagl/agentic_coding_with_tools_like_aider_cline_claude/
[2] https://www.youtube.com/watch?v=LnvlEd9fVok
[3] https://www.anthropic.com/engineering/claude-code-best-practices
[4] https://www.latent.space/p/claude-code
[5] https://code.visualstudio.com/blogs/2025/02/24/introducing-copilot-agent-mode
[6] https://www.youtube.com/watch?v=bTMPwUgLZf0
[7] https://github.blog/ai-and-ml/github-copilot/which-ai-model-should-i-use-with-github-copilot/
[8] https://github.com/anthropics/claude-code
[9] https://www.anthropic.com/solutions/coding
[10] https://arxiv.org/pdf/2303.04142.pdf
[11] https://arxiv.org/pdf/2402.08431.pdf
[12] https://arxiv.org/pdf/2403.08299.pdf
[13] https://arxiv.org/pdf/2310.13896.pdf
[14] https://arxiv.org/pdf/2311.18450.pdf
[15] https://arxiv.org/pdf/2402.07456.pdf
[16] https://arxiv.org/html/2404.04902v1
