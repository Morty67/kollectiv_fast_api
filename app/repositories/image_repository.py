from sqlalchemy.exc import IntegrityError

from app.models.image_model import Images
from app.repositories.base_repository import BaseRepository


class ImageRepository(BaseRepository):

    model = Images

    async def add_image(self, filename: str):
        try:
            # Create a new record in the database and get its id
            image_id = await self.create(name=filename)

        except IntegrityError:
            # Handling the case when the file name is not unique
            raise ValueError("Filename must be unique.")

        return image_id

    async def get_image_by_id(self, image_id: int):
        query = self.model.__table__.select().where(self.model.id == image_id)
        return await self.get_one(query)
