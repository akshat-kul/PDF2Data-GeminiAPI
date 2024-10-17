import aioredis
from config.settings import settings

class RedisCache:
    def __init__(self, host: str, port: int):
        self.redis = None
        self.host = host
        self.port = port

    async def connect(self):
        self.redis = await aioredis.from_url(f"redis://{self.host}:{self.port}", decode_responses=True)

    async def get_cache(self, key: str):
        return await self.redis.get(key)

    async def set_cache(self, key: str, value: str, expire: int = 3600):
        await self.redis.set(key, value, ex=expire)

    async def close(self):
        if self.redis:
            await self.redis.close()

# Usage
redis_cache = RedisCache(settings.redis_host, settings.redis_port)