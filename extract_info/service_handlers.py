from utils.gemini import extract_from_pdf, extract_from_text
import json, os
from config.database import db
from bson import ObjectId
from datetime import datetime

async def process_pdf(file_path: str, task_id: str):
    try:
        extracted_info_str = await extract_from_pdf(file_path)
        extracted_info_dict = convert_string_to_dict(extracted_info_str)

        result = await db.papers.insert_one(extracted_info_dict)
        # Update the task status to completed with the paper ID
        await db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"status": "completed", "result": str(result.inserted_id), "updated_at": datetime.now()}}
        )

    except Exception as e:
        # Update the task status to failed with the error message
        await db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"status": "failed", "error": str(e), "updated_at": datetime.now()}}
        )

    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)


async def process_text(file_path: str, task_id: str):
    try:
        extracted_info_str = extract_from_text(file_path)
        extracted_info_dict = convert_string_to_dict(extracted_info_str)

        result = await db.papers.insert_one(extracted_info_dict)
        # Update the task status to completed with the paper ID
        await db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"status": "completed", "result": str(result.inserted_id), "updated_at": datetime.now()}}
        )

    except Exception as e:
        # Update the task status to failed with the error message
        await db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"status": "failed", "error": str(e), "updated_at": datetime.now()}}
        )

    finally:
        # Clean up the temporary file
        if os.path.exists(file_path):
            os.remove(file_path)

def convert_string_to_dict(text):
    text = text.strip("```")
    text = text.lstrip("json")

    dict_data = json.loads(text)
    return dict_data