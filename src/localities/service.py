from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.localities import models, schemas

async def create_locality(
    db: AsyncSession, 
    data: schemas.LocalityCreate
):
    locality = models.Locality(**data.dict())
    db.add(locality)
    await db.commit()
    await db.refresh(locality)
    return locality

async def update_locality(
    db: AsyncSession, 
    locality_id: int, 
    data: schemas.LocalityUpdate
):
    result = await db.execute(select(models.Locality).where(models.Locality.id == locality_id))
    locality = result.scalars().first()
    if not locality:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(locality, key, value)
    await db.commit()
    await db.refresh(locality)
    return locality

async def delete_locality(
    db: AsyncSession, 
    locality_id: int
):
    result = await db.execute(select(models.Locality).where(models.Locality.id == locality_id))
    locality = result.scalars().first()
    if not locality:
        return {"ok": False}
    await db.delete(locality)
    await db.commit()
    return {"ok": True}

async def get_all(db: AsyncSession):
    result = await db.execute(select(models.Locality))
    return result.scalars().all()
