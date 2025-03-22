# Python Project Generator

This is a lightweight Python script to quickly scaffold a standard project folder structure using a YAML configuration file.

---

## 🔧 Features

- Customizable folder/file structure via `project_config.yaml`
- Automatically initializes a Git repository
- Adds a minimal `.gitignore` for Python
- Simple and easy to use from the command line

---

## 📦 Requirements

- Python 3.x
- `pyyaml` library

Install `pyyaml` if needed:

```bash
pip install pyyaml
```

---

##  How to Use

1. Clone or copy this script (`generate_project.py`) and the config file (`project_config.yaml`) into any directory.

2. Edit `project_config.yaml` to define your desired folder structure. Example:

   ```yaml
   structure:
     - data/
     - data/raw/
     - notebooks/
     - src/
     - src/__init__.py
     - .gitignore
   ```

3. Run the script from your terminal:

   ```bash
   python generate_project.py my_project_name
   ```

4. It will create a new folder named `my_project_name/` with the full structure inside.


---

You guessed it! This README file was built by ChatGPT!
---

## 🧼 License

MIT License – free to use, modify, and share.
