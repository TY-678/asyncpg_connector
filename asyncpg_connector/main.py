import asyncio
import asyncpg
from asyncpg_connector.error.error_models import DatabaseConnectionError


class AsyncpgConnector:
    def __init__(self, connect_config: dict):
        self.connect_config = connect_config
        self.conn = None

    async def __aenter__(self):
        try:
            self.conn = await asyncpg.connect(**self.connect_config)
            return self
        except Exception as e:
            raise DatabaseConnectionError(f"Database connection failed:{e}")

    async def __aexit__(self, *args):
        await asyncio.gather(self.conn.close(timeout=10), return_exceptions=True)

    def __await__(self):
        return self.__aenter__().__await__()
