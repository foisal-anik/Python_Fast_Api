from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()
#Request Get Method Url
@app.get("/posts")
async def root():
    return {"message": "post"}
@app.get("/")
async def root():
    return {"message": "Welcome to my api"}

@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title {payLoad['title']} content: {payLoad['content']}"}