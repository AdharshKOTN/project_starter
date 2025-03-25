import os
from openai import OpenAI, OpenAIError
from structures.flask import FLASK_FILES, FLASK_STRUCTURE
from dotenv import load_dotenv
import ollama

load_dotenv()

def openai_client():
    return OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def run_project_initializer():
    print("\n🚀 Project Starter - ML/AI Edition")
    print("----------------------------------")

    # === User Input ===
    project_name = input("Enter your project name: ").strip()
    project_type = input("Choose project type (flask ): ").strip().lower()
    use_llm_input = input("Use LLM to generate content? (y/n): ").strip().lower()
    use_llm = use_llm_input == "y"

    # === Base Directory ===
    base_dir = os.path.expanduser("~/projects")
    os.makedirs(base_dir, exist_ok=True)

    project_path = os.path.join(base_dir, project_name)
    os.makedirs(project_path, exist_ok=True)
    os.chdir(project_path)

    # === Get Project Structure ===
    folders, files = get_structure_for_type(project_type)

    # === Create Folders & Files ===
    create_folder_structure(".", folders)
    create_files(files, project_name, f"A {project_type} starter project")

    print(f"\n✅ Project '{project_name}' created at: {project_path}")

    
def create_folder_structure(base_path, folder_list):
    for folder in folder_list:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)

    
def generate_readme_with_llm(project_name, description, use_openai=True, model="gpt-4o-mini"):
    prompt = f"Generate a README for a Python project named '{project_name}' focused on: {description}"

    # Try OpenAI first
    if use_openai:
        try:
            response = openai_client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            if hasattr(e, 'status_code') and e.status_code == 429:
                print("⚠️ OpenAI quota exceeded (429). Falling back to local LLM via Ollama...")
            else:
                print(f"⚠️ OpenAI error: {e}. Falling back to Ollama...")

    # Use Ollama fallback
    try:
        response = ollama.chat(
            model="codellama",  # or 'mistral' if you prefer
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']
    except Exception as e:
        print("🚫 Failed to generate README with Ollama:", e)
        return f"# {project_name}\n\n{description} (LLM content unavailable)"


def get_structure_for_type(project_type):
    if project_type == "flask":
        return FLASK_STRUCTURE, FLASK_FILES
    # Add other types here later
    else:
        return [], {}
    
def create_files(file_map, project_name="MyProject", description="A cool project"):
    for file_path, content in file_map.items():
        with open(file_path, "w") as f:
            if file_path.lower() == "readme.md":
                f.write(generate_readme_with_llm(project_name, description=description, use_openai=False))
            else:
                f.write(content)

    
def initialize_git_repo():
    os.system("git init && git add . && git commit -m 'Initial commit'")

def setup_virtualenv(env_name="venv"):
    os.system(f"python3 -m venv {env_name}")
    print(f"✅ Virtual environment '{env_name}' created.")

