import os
import uuid
from datetime import datetime
from bson import ObjectId
from fastapi import BackgroundTasks
from config.database import db
from fastapi import UploadFile, BackgroundTasks
from bson import ObjectId
from datetime import datetime
from extract_info.service_handlers import process_pdf, process_text

async def create_task_id_pdf(file: UploadFile, background_tasks: BackgroundTasks):
    # Save the uploaded file to a temporary location
    temp_dir = "/tmp/sample_papers_api"
    os.makedirs(temp_dir, exist_ok=True)
    file_path = os.path.join(temp_dir, f"{uuid.uuid4()}.pdf")  # Use the file extension

    # Save the uploaded file
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Create a task entry in the database
    task_id = str(ObjectId())
    task = {
        "_id": ObjectId(task_id),
        "status": "processing",
        "result": None,
        "error": None,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    await db.tasks.insert_one(task)

    background_tasks.add_task(process_pdf, file_path, task_id)
    return task_id

async def create_task_id_text(text, background_tasks: BackgroundTasks):
    # Create a task entry in the database
    task_id = str(ObjectId())
    task = {
        "_id": ObjectId(task_id),
        "status": "processing",
        "result": None,
        "error": None,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    await db.tasks.insert_one(task)

    background_tasks.add_task(process_text, text, task_id)
    return task_id





    