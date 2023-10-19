from fastapi import FastAPI
from routers.blogger_signup import blogger_router
from schemas.blogger_schemas import BloggerBase

app = FastAPI()

bloggerDB:list[BloggerBase] = {}

app.include_router(blogger_router, prefix="/Create")

@app.get("/")
def home():
    return {"message": "Welcome To The World Of Bloggers"}


@app.get("/about")
def about():
    return {"message": "Share breaking news or whatever's on your mind, we got you covered at MY BLOG. Sign Up to discover why millions of people have realize their dreams here"}

# @app.get("/get blogs")
# def get_bloggers():
#     return bloggerDB