from typing import Optional
from bson import ObjectId
from config.database import db

async def get_task_details(task_id: str) -> Optional[dict]:
    # Find the document in MongoDB (returns dict)
    paper = await db.tasks.find_one({"_id": ObjectId(task_id)})

    # Return the document directly, which should be a dict
    return paper 