from fastapi import FastAPI
from api import video_router
from db import database, metadata, engine

import sqlalchemy

app = FastAPI()
metadata.create_all(engine)
app.include_router(video_router)
app.state.database = database


@app.on_event("startup")
async def startup():
    database_ = app.state.database
    if database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()