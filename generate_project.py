import os
import yaml
import argparse

# Argument parser to accept project name
parser = argparse.ArgumentParser(description="Generate a Python project structure.")
parser.add_argument("project_name", help="Name of the project to create")
args = parser.parse_args()

project_name = args.project_name

# Load YAML structure (excluding project_name)
yaml_file = 'project_config.yaml'
if not os.path.exists(yaml_file):
    print("❌ YAML config file not found.")
    exit(1)

with open(yaml_file) as f:
    try:
        config = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"❌ Error reading YAML: {e}")
        exit(1)

structure = config.get('structure')
if not structure:
    print("❌ Missing 'structure' in YAML.")
    exit(1)

# Define minimal .gitignore content
gitignore_content = """__pycache__/
*.pyc
*.pyo
*.pyd
.env
"""

# Create base project folder
print(f"📁 Creating project: {project_name}")
os.makedirs(project_name, exist_ok=True)

# Create files and folders
for path in structure:
    full_path = os.path.join(project_name, path)
    if path.endswith('/'):
        os.makedirs(full_path, exist_ok=True)
        print(f"📂 Created folder: {full_path}")
    else:
        with open(full_path, 'w') as f:
            if path == '.gitignore':
                f.write(gitignore_content)
            else:
                f.write('')
        print(f"📄 Created file: {full_path}")

# Initialize git repo
print("🔧 Initializing git repo...")
os.system(f"cd {project_name} && git init")

print("✅ Done!")