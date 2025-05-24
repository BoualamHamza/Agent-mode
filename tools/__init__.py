# tools/__init__.py

# This file makes the 'tools' directory a Python package.
# We can selectively import functions from the modules here to make them available
# directly under the 'tools' namespace if desired.

# For example, if you want to allow `from tools import read_file`:
# from .file_system import read_file, write_file
# from .shell import run_command
# from .testing import run_tests
# from .git import git_commit

# Or, to import all tools (though selective is often better for clarity):
# from .file_system import *
# from .shell import *
# from .testing import *
# from .git import *

# For now, we'll keep it simple and require users to import from the specific modules,
# e.g., `from tools.file_system import read_file`.
# This can be revisited if a flatter namespace is preferred for the agent's direct use.

print("tools package initialized")
