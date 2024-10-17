from fastapi import FastAPI
import uvicorn
from papers.routers import paper_router
from extract_info.routers import extract_info_router
from tasks.routers import tasks_router
from config.database import create_indexes, close_database_connection
from contextlib import asynccontextmanager
from utils.caching import redis_cache

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions
    await create_indexes()  # Create your database indexes
    await redis_cache.connect()  # Connect to Redis
    yield  # This is where the app will run
    # Shutdown actions
    await redis_cache.close()  # Close Redis connection
    await close_database_connection()  # Close your database connection

app = FastAPI(
    title="Sample Papers API",
    lifespan=lifespan
)

app.include_router(paper_router, prefix="/papers", tags=["Papers"])
app.include_router(extract_info_router, prefix="/extract", tags=["Extract"])
app.include_router(tasks_router, prefix="/tasks", tags=["Tasks"])

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

