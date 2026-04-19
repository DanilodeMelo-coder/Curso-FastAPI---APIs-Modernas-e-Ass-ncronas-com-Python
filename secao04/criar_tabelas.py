from core.configs import DBBaseModel
from core.database import engine

async def creat_table() -> None:
    import models.__all_models
    print("criando as tabelas no banco de dados")

    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)
    print("tabelas criadas com sucesso")

if __name__ == '__main__':
    import asyncio

    asyncio.run(creat_table())