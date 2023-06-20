import shutil
from fastapi import FastAPI, UploadFile, File, APIRouter
from typing import List
from schemas import UploadVideo
from models import Video

video_router = APIRouter()


@video_router.post('/')
async def root(info: UploadVideo, file: UploadFile = File(...)):
    with open('test.mp4', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {'file_name': file.filename}


@video_router.post('/img')
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(img.filename, 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)

        return {'file_name': 'good'}


@video_router.post('/video')
async def create_video(video: Video):
    await video.save()
    return video


@video_router.get('/info')
async def info_get(info: UploadVideo):
    title = 'Test'
    desription = 'desct'
    return UploadVideo(title=title, desription=desription)

