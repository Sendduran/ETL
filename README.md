# ETL App

A Python-based ETL (Extract, Transform, Load) application.

---

## 🚀 Getting Started

Follow these steps to set up your development environment and run the app.

---

### 1. **Clone the Repository**

```sh
git clone <your-repo-url>
cd ETL
```

---

### 2. **Install [Poetry](https://python-poetry.org/)**

Poetry manages dependencies and virtual environments.

```sh
pip install poetry
```

---

### 3. **Install Dependencies**

Poetry will create a virtual environment and install all required packages.

```sh
poetry install
```

---

### 4. **Activate the Virtual Environment**

```sh
poetry shell
```

---

### 5. **Install [pre-commit](https://pre-commit.com/)**

Pre-commit ensures code quality by running checks before each commit.

```sh
pip install pre-commit
pre-commit install
```

To run all pre-commit hooks manually:

```sh
pre-commit run --all-files
```

---

## 🛠️ Project Structure

```
ETL/
│   pyproject.toml
│   README.md
│   test.py
└───etl_app/
    │   __init__.py
    ├───connection/
    │     ├── __init__.py
    │     └── connection.py
    ├───tools/
    │     ├── __init__.py
    │     └── tools.py
    └── main.py
```

---

## 🧹 Code Quality

- **Pre-commit** hooks will check for trailing whitespace, end-of-file fixes, YAML validity, large files, and remove unused imports (except in `__init__.py`).
---

## 💡 Tips

- If you add new dependencies, use `poetry add <package-name>`.
- If you encounter issues with pre-commit or poetry, try updating them:
  ```sh
  pip install --upgrade poetry pre-commit
  ```

---
