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

python -m venv venv

venv\Scripts\activate

## Installing Dependencies
pip install -r requirements.txt

For Version Compatiblity

pip install "fastapi<0.100" "pydantic<2.0"

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
