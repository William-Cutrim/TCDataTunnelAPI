from fastapi import FastAPI, HTTPException, status
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

    if item.data.get('reference', None):

        return {'message': 'message sent',
                'status': status.HTTP_200_OK}

    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST)

