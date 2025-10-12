from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.profile import models, schemas

async def create_profile(
    db: AsyncSession, 
    data: schemas.ProfileCreate
):
    profile = models.Profile(**data.dict())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile

async def update_profile(
    db: AsyncSession, 
    profile_id: int, 
    data: schemas.ProfileUpdate
):
    result = await db.execute(select(models.Profile).where(models.Profile.id == profile_id))
    profile = result.scalars().first()
    if not profile:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(profile, key, value)
    await db.commit()
    await db.refresh(profile)
    return profile

async def delete_profile(
    db: AsyncSession, 
    profile_id: int
):
    result = await db.execute(select(models.Profile).where(models.Profile.id == profile_id))
    profile = result.scalars().first()
    if not profile:
        return {"ok": False}
    await db.delete(profile)
    await db.commit()
    return {"ok": True}

async def get_profiles(db: AsyncSession):
    result = await db.execute(select(models.Profile))
    return result.scalars().all()
