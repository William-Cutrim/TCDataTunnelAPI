from dataclasses import field
from lib2to3.pytree import Base
from fastapi import FastAPI
from typing import Optional, List, Dict
from pydantic import BaseModel

app = FastAPI(title='FastAPI, Docker, and Traefik')

class Item(BaseModel):

    now:int
    key:str
    fields:List[str]
    data:Dict[str, str]

data = []

@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.post('/message')
def send_message(item: Item):

    data.append(item)

    return {'message': 'message sent'}
