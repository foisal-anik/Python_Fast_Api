from fastapi import FastAPI
app = FastAPI()
#Request Get Method Url
@app.get("/posts")
async def root():
    return {"message": "post"}
@app.get("/")
async def root():
    return {"message": "Welcome to my api"}

