import datetime

from fastapi import (
    APIRouter,
    Depends
)
from pydantic import BaseModel


router = APIRouter()

class FormModel(BaseModel):
    email: str
    phone: str
    date: datetime.date
    content: str


@router.post('/get_form')
async def get_form(
    model: FormModel
):
    return {'return': 'example'}
