# tools/git.py
import subprocess
import shlex

def git_commit(message: str, branch_name: str = "main") -> str:
    """
    Commits changes to the local git repository with the given message.
    Optionally, specify a branch. (Note: actual branching might need separate commands)
    This assumes git is initialized in the project and configured.
    """
    try:
        # Stage all changes
        stage_command = "git add ."
        process_stage = subprocess.Popen(shlex.split(stage_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout_stage, stderr_stage = process_stage.communicate(timeout=30)
        if process_stage.returncode != 0:
            return f"Error staging files: {stderr_stage}"

        # Commit changes
        commit_command = f"git commit -m \"{message}\"" # Ensure message is quoted
        process_commit = subprocess.Popen(shlex.split(commit_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout_commit, stderr_commit = process_commit.communicate(timeout=30)

        if process_commit.returncode == 0:
            return f"Successfully committed changes with message: '{message}' to branch '{branch_name}'.\nOutput:\n{stdout_commit}"
        else:
            # Check for "nothing to commit" scenario
            if "nothing to commit" in stderr_commit.lower() or "no changes added to commit" in stderr_commit.lower():
                return "No changes to commit."
            return f"Error committing changes: {stderr_commit}"
    except subprocess.TimeoutExpired:
        return "Error: Git command timed out."
    except FileNotFoundError:
        return "Error: Git command not found. Is Git installed and in PATH?"
    except Exception as e:
        return f"Error performing git commit: {str(e)}"

# Example of how one might add a git_branch function if needed later
# def git_branch(branch_name: str) -> str:
#     try:
#         command = f"git checkout -b {branch_name}"
#         process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         stdout, stderr = process.communicate(timeout=30)
#         if process.returncode == 0:
#             return f"Successfully created and switched to new branch: {branch_name}.\nOutput:\n{stdout}"
#         else:
#             if "already exists" in stderr:
#                 # If branch exists, just check it out
#                 command_checkout = f"git checkout {branch_name}"
#                 process_checkout = subprocess.Popen(shlex.split(command_checkout), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#                 stdout_co, stderr_co = process_checkout.communicate(timeout=30)
#                 if process_checkout.returncode == 0:
#                     return f"Successfully switched to existing branch: {branch_name}.\nOutput:\n{stdout_co}"
#                 else:
#                     return f"Error switching to existing branch {branch_name}: {stderr_co}"
#             return f"Error creating branch {branch_name}: {stderr}"
#     except subprocess.TimeoutExpired:
#         return "Error: Git branch command timed out."
#     except Exception as e:
#         return f"Error creating git branch: {str(e)}"
