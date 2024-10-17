from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from tasks.service import get_task_details
from utils.caching import redis_cache
from tasks.schemas import TaskID
from utils.verify_api_key import verify_api_key

tasks_router = APIRouter()

@tasks_router.get("/{task_id}", response_model=dict, dependencies=[Depends(verify_api_key)])
async def retrieve_paper(task_id: str):
    cached_task_id = await redis_cache.get_cache(task_id)

    if cached_task_id:
        # Return validated cached task in dict format
        return TaskID.model_validate_json(cached_task_id).model_dump()

    task_details = await get_task_details(task_id)

    if not task_details:
        raise HTTPException(status_code=404, detail="Task not found")

    # Convert ObjectId to string for _id
    if isinstance(task_details['_id'], ObjectId):
        task_details['_id'] = str(task_details['_id'])

    # Use TaskID schema to parse and validate task_details directly
    task_id_details = TaskID(**task_details)  # Unpacking task_details directly

    # Cache the task result in Redis
    await redis_cache.set_cache(task_id, task_id_details.model_dump_json())

    # Return the model as a dictionary for FastAPI
    return task_id_details.model_dump() 
