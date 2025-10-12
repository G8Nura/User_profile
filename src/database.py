from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base
from src.config import settings
from typing import AsyncGenerator


engine = create_async_engine(settings.DATABASE_URL, echo = True)
new_session = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession,
    expire_on_commit = False
)
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with new_session() as session:
        yield session 