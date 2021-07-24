from fastapi import (
    APIRouter,
    Depends
)

router = APIRouter(
    tags=['app']
)

@router.post('/')
async def index():
    return {'return': 'example'}