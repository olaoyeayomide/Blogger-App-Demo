
from schemas.blogger_schemas import CreateBlogger as FakeBlogger
from schemas.blogger_schemas import CreateBlogger, BloggerBase, Response
from uuid import UUID

bloggerDB:list[BloggerBase] = {}




# class CreateBlogger:

async def create_blogger_profile(blogger_details: FakeBlogger):
    blogger = BloggerBase(id=str(UUID(int=len(bloggerDB) + 1)), **blogger_details).model_dump()
    # bloggerDB[blogger.id] = blogger

    return Response (data=blogger)
    
# blogger_service = CreateBlogger()
# blogger_service = create_blogger_profile()

# CB = CreateBlogger()