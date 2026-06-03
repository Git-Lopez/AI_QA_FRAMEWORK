from pathlib import Path

def write_file(path: str, content: str):
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w") as f:
        f.write(content)

    print(f"Created: {path}")