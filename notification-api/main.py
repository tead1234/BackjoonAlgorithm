from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/blog')
## 쿼리변수를 함수에 직접 떄려박음
# 디폴트값 넣기 가능
def index(limit= 10, published = True):
    if published:

        return {"da": f'{limit}hji'}
    else:
        return "ERROR"
@app.get('/blog/{id}')
def comments(id: int):
    return {'data': {
        id
        }
    }

@app.get('/blog/unpublished')
def unpublished():
    return {
        'data' : 'all unpublished blogs'
    }