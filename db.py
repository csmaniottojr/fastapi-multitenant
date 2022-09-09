from contextlib import contextmanager

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from dal import get_tenant_by_subdomain
from exceptions import TenantNotFound

DB_URI = "postgresql+asyncpg://{user}:{password}@{host}:{port}/{db}".format(
    host="localhost",
    user="pythonsul",
    password="pythonsul",
    db="pythonsul",
    port="7777",
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
)


@contextmanager
def with_session(tenant: str | None):
    schema_translate_map = {}
    if tenant:
        schema_translate_map["tenant"] = tenant

    engine = create_async_engine(
        DB_URI,
        execution_options={"schema_translate_map": schema_translate_map},
    )
    session = SessionLocal(bind=engine)
    try:
        yield session
    finally:
        session.close()


async def get_tenant_schema(req: Request) -> str:
    subdomain = req.headers["host"].split(".")[0].lower()

    with with_session(None) as session:
        tenant = await get_tenant_by_subdomain(session, subdomain)

    if tenant is None:
        raise TenantNotFound(subdomain)

    return subdomain


def get_db(tenant_schema: str = Depends(get_tenant_schema)):
    with with_session(tenant_schema) as session:
        yield session
