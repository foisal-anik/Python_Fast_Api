from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my api"}
@app.get("/post/")
async def root():
    return {"message": "post"}
