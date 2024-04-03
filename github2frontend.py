import os
import sys
import requests
import zipfile
import io
import ast

def is_desired_file(file_path):
    """Check if the file is a Python, HTML, CSS, JavaScript, TypeScript, Svelte, or Rust file."""
    return file_path.endswith(".py") or file_path.endswith(".HTML") or file_path.endswith(".CSS") or file_path.endswith(".js") or file_path.endswith(".ts") or file_path.endswith(".svelte") or file_path.endswith(".rs")

def is_likely_useful_file(file_path):
    """Determine if the file is likely to be useful by excluding certain directories and specific file types."""
    excluded_dirs = ["docs", "examples", "tests", "test", "__pycache__", "scripts", "utils", "benchmarks", "node_modules", ".venv"]
    utility_or_config_files = ["hubconf.py", "setup.py", "package-lock.json"]
    github_workflow_or_docs = ["stale.py", "gen-card-", "write_model_card"]

    if any(part.startswith('.') for part in file_path.split('/')):
        return False
    for excluded_dir in excluded_dirs:
        if f"/{excluded_dir}/" in file_path:
            return False
    for file_name in utility_or_config_files:
        if file_name in file_path:
            return False
    return all(doc_file not in file_path for doc_file in github_workflow_or_docs)

def has_sufficient_content(file_content, min_line_count=10):
    """Check if the file has a minimum number of substantive lines."""
    lines = [line for line in file_content.split('\n') if line.strip() and not line.strip().startswith('#')]
    return len(lines) >= min_line_count

def remove_comments_and_docstrings(source):
    """Remove comments and docstrings from the Python source code."""
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)) and ast.get_docstring(node):
            node.body = node.body[1:]  # Remove docstring
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Str):
            node.value.s = ""  # Remove comments
    return ast.unparse(tree)



def download_repo(repo_url, output_file):
    """Download and process files from a GitHub repository."""
    if '/tree/' in repo_url:
        repo_url = f'https://download-directory.github.io/?{repo_url}'

    response = requests.get(f"{repo_url}/archive/master.zip")
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))

    for file_info in zip_file.infolist():
        file_path = file_info.filename
        if is_desired_file(file_path) and is_likely_useful_file(file_path):
            with zip_file.open(file_info) as file:
                file_content = file.read().decode('utf-8')
                if has_sufficient_content(file_content):
                    with open(output_file, 'wb') as output:  # Open file in binary mode
                        output.write(file_content.encode('utf-8'))  # Encode content to utf-8

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <github_repo_url>")
        sys.exit(1)

    repo_url = sys.argv[1]
    repo_name = repo_url.split("/")[-1]
    output_file = f"{repo_name}_code.txt"

    download_repo(repo_url, output_file)
    print(f"Combined source code saved to {output_file}")