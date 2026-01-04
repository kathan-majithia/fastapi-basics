from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return 'Hello'

@app.get('/about')
def about():
    return {"name":"Kathan Majithia"}

