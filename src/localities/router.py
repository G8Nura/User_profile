from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.localities import schemas, service
from src.database import get_db

router = APIRouter(prefix="/localities", tags=["Localities"])

@router.post("/", response_model=schemas.LocalityResponse)
async def create_locality(
    data: schemas.LocalityCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await service.create_locality(db, data)

@router.put("/{locality_id}", response_model=schemas.LocalityResponse)
async def update_locality(
    locality_id: int, 
    data: schemas.LocalityUpdate, 
    db: AsyncSession = Depends(get_db)
):
    locality = await service.update_locality(db, locality_id, data)
    if not locality:
        raise HTTPException(status_code=404, detail="Locality not found")
    return locality

@router.delete("/{locality_id}")
async def delete_locality(
    locality_id: int, 
    db: AsyncSession = Depends(get_db)
):
    result = await service.delete_locality(db, locality_id)
    if not result["ok"]:
        raise HTTPException(status_code=404, detail="Locality not found")
    return result

@router.get("/", response_model=List[schemas.LocalityResponse])
async def get_all_localities(db: AsyncSession = Depends(get_db)):
    return await service.get_all(db)
