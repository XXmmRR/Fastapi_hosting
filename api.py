import shutil
from fastapi import FastAPI, UploadFile, File, APIRouter, Form, HTTPException, BackgroundTasks
from typing import List
from schemas import UploadVideo, GetVideo
from models import Video, User
from services import write_video
from fastapi.responses import StreamingResponse
from uuid import uuid4

video_router = APIRouter()


@video_router.post('/')
async def create_video(background_tasks: BackgroundTasks,
                       title: str = Form(...),
                       description: str = Form(...),
                       file: UploadFile = File(...)):
    file_name = f'media/{uuid4()}_{file.filename}'
    if file.content_type == 'video/mp4':
        background_tasks.add_task(write_video, file_name, file)
    else:
        raise HTTPException(status_code=418, detail="It isn't mp4")
    info = UploadVideo(title=title, description=description)
    user = await User.objects.get(pk=1)
    return await Video.objects.create(user=user, path=file_name, **info.dict())


@video_router.get('/video/{pk}', response_model=GetVideo)
async def video_get(pk: int):
    file = await Video.objects.select_related('user').get(pk=pk)
    print(file.dict())
    file_like = open(file.dict().get('path'), mode='rb')
    return StreamingResponse(file_like, media_type='video/mp4')



