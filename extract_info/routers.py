from fastapi import APIRouter, Request, UploadFile, File, HTTPException, Depends
from extract_info.service import create_task_id_pdf, create_task_id_text
from fastapi import BackgroundTasks
from utils.verify_api_key import verify_api_key

extract_info_router = APIRouter()

#Router for extracting info out of pdf file upload
@extract_info_router.post("/pdf", response_model=dict, dependencies=[Depends(verify_api_key)])
async def extract_pdf(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")

    response_task_id = await create_task_id_pdf(file, background_tasks)
    return {"task_id": response_task_id}


#Router for extracting info out of plain text
@extract_info_router.post("/text", response_model=dict, dependencies=[Depends(verify_api_key)])
async def extract_text(request: Request, background_tasks: BackgroundTasks = BackgroundTasks()):
    # Validate the content type (you should check the content type from the request headers, not a 'file' variable)
    if request.headers.get('content-type') != "text/plain":
        raise HTTPException(status_code=400, detail="Expecting text in the request")
    
    data = await request.body()
    text_content = data.decode('utf-8')
    response_task_id = await create_task_id_text(text_content, background_tasks)
    
    return {"task_id": response_task_id}

