from fastapi import APIRouter, Depends, HTTPException
from papers.schemas import SamplePaper
from papers.service import create_paper, delete_paper, get_paper, update_paper
from utils.caching import redis_cache
from utils.verify_api_key import verify_api_key

paper_router = APIRouter()

@paper_router.post("/", response_model=dict, status_code=201, dependencies=[Depends(verify_api_key)])
async def create_new_paper(paper: SamplePaper):
    paper_id = await create_paper(paper)
    return {"id": paper_id}

@paper_router.get("/{paper_id}", response_model=SamplePaper, dependencies=[Depends(verify_api_key)])
async def retrieve_paper(paper_id: str):
    cached_paper = await redis_cache.get_cache(paper_id)
    
    if cached_paper:
        return SamplePaper.model_validate_json(cached_paper)
    
    paper = await get_paper(paper_id)
    
    if not paper:
        raise HTTPException(status_code=404, detail="Paper not found")

    paper_model = SamplePaper.from_mongo(paper)
    await redis_cache.set_cache(paper_id, paper_model.model_dump_json())
    
    return paper_model

@paper_router.put("/{paper_id}", dependencies=[Depends(verify_api_key)])
async def modify_paper(paper_id: str, paper: dict):
    updated_paper = await update_paper(paper_id, paper)
    
    if not updated_paper:
        raise HTTPException(status_code=404, detail="Paper not found or no changes made")
    
    return updated_paper  # This should also be converted to SamplePaper if needed

@paper_router.delete("/{paper_id}", response_model=dict, dependencies=[Depends(verify_api_key)])
async def remove_paper(paper_id: str):
    success = await delete_paper(paper_id)
    if not success:
        raise HTTPException(status_code=404, detail="Paper not found")
    return {"detail": "Paper deleted successfully"}