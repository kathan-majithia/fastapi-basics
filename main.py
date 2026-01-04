from fastapi import FastAPI

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

@app.get("/")
def index():
    return {"data":"Hello"}

@app.get('/about')
def about():
    return {"name":"Kathan Majithia"}

@app.get('/blob')
def blob(limit=10,lod : bool = True):
    if lod:
        return {"data" : f"{limit} blobs from the db"}
    else:
        return {"data":"Not loaded"}

@app.get('/blob/{id}')
def show(id: int):
    return {"data":id}

