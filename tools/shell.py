# tools/shell.py
import subprocess
import shlex

def run_command(command: str) -> str:
    """
    Runs a shell command and returns its output.
    For safety, this should ideally run in a sandboxed environment.
    Destructive commands should be handled with extreme care or require user confirmation.
    """
    try:
        # For now, we'll implement a basic version.
        # Consider adding safety checks for destructive commands (e.g., rm -rf)
        # or a mechanism for user confirmation.
        if "rm -rf" in command or "sudo" in command: # Basic safety check
            # In a real agent, this might ask for user confirmation
            # or prevent the command altogether.
            return "Error: Destructive or privileged command detected. Execution aborted for safety."

        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(timeout=60) # Added timeout
        if process.returncode == 0:
            return f"Command executed successfully.\nOutput:\n{stdout}"
        else:
            return f"Command failed with error code {process.returncode}.\nError:\n{stderr}"
    except subprocess.TimeoutExpired:
        return "Error: Command timed out."
    except FileNotFoundError:
        return f"Error: Command not found (it may not be installed or not in PATH)."
    except Exception as e:
        return f"Error running command: {str(e)}"
