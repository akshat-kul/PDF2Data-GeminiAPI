from motor.motor_asyncio import AsyncIOMotorClient
from config.settings import settings

mongo_db_url = settings.mongo_db_url
client = AsyncIOMotorClient(mongo_db_url)
db = client.papers_tasks_db

# Create indexes for efficient querying
async def create_indexes():
    await db.papers.create_index("title")
    await db.papers.create_index("type")
    await db.papers.create_index("params.board")
    await db.papers.create_index("params.grade")
    await db.papers.create_index("params.subject")
    await db.papers.create_index([("sections.questions.question_text", "text"), ("sections.questions.answer", "text")])
    await db.tasks.create_index("status")

# Close the database connection
async def close_database_connection():
    client.close()