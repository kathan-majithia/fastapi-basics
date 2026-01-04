from fastapi import FastAPI

app = FastAPI()

@app.post('/blog')
def create(title,body):
    return {"title":title,"body":body}