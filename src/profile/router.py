from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from src.profile import schemas, service
from src.database import get_db

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.post("/", response_model=schemas.ProfileResponse)
async def create_profile(
    data: schemas.ProfileCreate, 
    db: AsyncSession = Depends(get_db)
):
    return await service.create_profile(db, data)

@router.put("/{profile_id}", response_model=schemas.ProfileResponse)
async def update_profile(
    profile_id: int, 
    data: schemas.ProfileUpdate, 
    db: AsyncSession = Depends(get_db)
):
    profile = await service.update_profile(db, profile_id, data)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.delete("/{profile_id}")
async def delete_profile(
    profile_id: int, 
    db: AsyncSession = Depends(get_db)
):
    result = await service.delete_profile(db, profile_id)
    if not result["ok"]:
        raise HTTPException(status_code=404, detail="Profile not found")
    return result

@router.get("/", response_model=List[schemas.ProfileResponse])
async def get_profiles(db: AsyncSession = Depends(get_db)):
    return await service.get_profiles(db)
