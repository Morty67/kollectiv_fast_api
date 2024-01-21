from typing import Any, List

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select


class BaseRepository:
    model: Any = None

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self) -> List:
        query = Select(self.model)
        response = await self.session.execute(query)
        return response.scalars().all()

    async def create(self, **kwargs):
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def exists(self, query: Select):
        query = query.with_only_columns(self.model.id)
        response = await self.session.execute(query)

        result = response.first()
        return bool(result)

    async def get_one(self, query: Select):
        response = await self.session.execute(query)
        result = response.scalars().first()
        return result

    async def delete(self, obj_id: int):
        query = delete(self.model).where(self.model.id == obj_id)
        await self.session.execute(query)
        await self.session.commit()

    async def save(self, obj: Any):
        self.session.add(obj)
        await self.session.commit()
