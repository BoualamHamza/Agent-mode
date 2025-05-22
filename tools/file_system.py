# tools/file_system.py
def read_file(path: str) -> str:
    """Reads the content of a file at the given path."""
    try:
        with open(path, 'r') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"Error: File not found at {path}"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def write_file(path: str, content: str) -> str:
    """Writes content to a file at the given path. Creates the file if it doesn't exist."""
    try:
        with open(path, 'w') as f:
            f.write(content)
        return f"File written successfully to {path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"
