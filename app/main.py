from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

@app.get("/")
def root():
    return {"message": "Root Page"}
    
@app.get("/hello/{name}")
def hello_name(name: str):
    p = name.strip().lower().title()
    return {"message": f"Hello, {p}. How are you?"}