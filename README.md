# 🚀 FastAPI Starter Reference

This repository is a **minimal FastAPI example project** created as a **personal reference**.  
Whenever starting a new FastAPI project, this README can be used as a **step-by-step guide**.

---

## 📁 Project Structure

```text
Fastapi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 🐍 Creating a Virtual Environment
```
python -m venv venv

venv\Scripts\activate
```
Activate the environment (Windows):

Note: If you encounter permission errors regarding scripts, run the following command to bypass the execution policy for the current process:
```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
## Installing Dependencies
```
pip install -r requirements.txt
```
For Version Compatiblity
```
pip install "fastapi<0.100" "pydantic<2.0"
```
## Running the Server
```
uvicorn app.main:app --reload
```

For using Custom code
```python
import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8200
    )
```

Run using `main.py` command

## API Documentation
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 🗄️ SQLite3 CLI Cheatsheet
If inspecting the .db file manually using the sqlite3 command line:

.tables → Show all tables in the database.

.schema → Show the CREATE statements (schema) for tables.

## Hosting Frontend

For normal hosting using python
```
python -m http.server 5500
```

Add the url in main.py
```
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8181"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
```
