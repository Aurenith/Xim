

from prisma import Prisma as PrismaClient


class PrismaService:
    """Manage the application-wide Prisma database client."""

    client: PrismaClient
    _connected: bool

    def __init__(self) -> None:
        """Create a disconnected Prisma client."""
        self.client = PrismaClient()
        self._connected = False

    async def connect(self) -> PrismaClient:
        """Connect to the database and return the Prisma client."""
        if not self._connected:
            await self.client.connect()
            self._connected = True

        return self.client

    async def disconnect(self) -> None:
        """Disconnect the Prisma client when it is currently connected."""
        if self._connected:
            await self.client.disconnect()
            self._connected = False


prisma_service = PrismaService()


async def get_prisma_client() -> PrismaClient:
    """Return the shared, connected Prisma client."""
    return await prisma_service.connect()


async def disconnect() -> None:
    """Disconnect the shared Prisma client."""
    await prisma_service.disconnect()
