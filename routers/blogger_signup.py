from fastapi import APIRouter, HTTPException
from schemas.blogger_schemas import BloggerBase, CreateBlogger, Response
from services.blogger_service import create_blogger_profile as cbp
from uuid import UUID



blogger_router= APIRouter()

bloggerDB:list[BloggerBase] = {}

@blogger_router.get("/get blogs")
def get_bloggers():
    return bloggerDB

@blogger_router.post("/create", status_code=201)
def create_blogger_profile(blogger_details: CreateBlogger):
    blogger = cbp(blogger_details)

    return Response (message = "Your Profile has been created successfully", data = blogger)


