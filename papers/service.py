from config.database import db
from papers.schemas import SamplePaper
from bson import ObjectId
from typing import Optional
from utils.caching import redis_cache

async def create_paper(paper: SamplePaper) -> str:
    paper_dict = paper.model_dump(by_alias=True)

    # Remove '_id' if it's None to allow MongoDB to generate it
    if paper_dict.get("_id") is None:
        paper_dict.pop("_id", None)

    # Insert the document into MongoDB
    result = await db.papers.insert_one(paper_dict)

    # Return the generated ObjectId as a string
    return str(result.inserted_id)

async def get_paper(paper_id: str) -> Optional[dict]:
    # Find the document in MongoDB (returns dict)
    paper = await db.papers.find_one({"_id": ObjectId(paper_id)})

    # Return the document directly, which should be a dict
    return paper 

async def update_paper(paper_id: str, paper: dict) -> Optional[SamplePaper]:
    update_result = await db.papers.update_one({"_id": ObjectId(paper_id)}, {"$set": paper})
    if update_result.modified_count:
        updated_paper = await db.papers.find_one({"_id": ObjectId(paper_id)})
        updated_paper.pop("_id")
        return updated_paper
    
    return None

async def delete_paper(paper_id: str) -> bool:
    delete_result = await db.papers.delete_one({"_id": ObjectId(paper_id)})
    
    cached_task = await redis_cache.get_cache(paper_id)
    if cached_task:
        await redis_cache.delete_cache(paper_id)

    return delete_result.deleted_count > 0