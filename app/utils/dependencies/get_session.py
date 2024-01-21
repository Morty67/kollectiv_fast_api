from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session


async def get_session() -> AsyncSession:
    """
    Asynchronous context manager for obtaining an SQLAlchemy AsyncSession.

    This function is used to asynchronously acquire an SQLAlchemy AsyncSession
    from the database connection pool. It should be used within
        a `async with` statement.

    Returns:
        AsyncSession: An SQLAlchemy AsyncSession instance.
    """
    async with async_session() as session:
        yield session
