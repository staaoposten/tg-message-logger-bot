import logging
from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update

from utils.config import config


def _parse_ids(raw: str) -> set[int]:
    return {int(x) for x in raw.replace(" ", "").split(",") if x}


class WhitelistMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        self.allowed = _parse_ids(config.BOT.allowed_ids or "")
        if self.allowed:
            logging.info(f"Whitelist enabled: {len(self.allowed)} allowed user(s)")

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        if not self.allowed:
            return await handler(event, data)

        if event.business_connection:
            user = event.business_connection.user
        elif event.message:
            user = event.message.from_user
        else:
            return await handler(event, data)

        if user is not None and user.id in self.allowed:
            return await handler(event, data)

        logging.warning(f"Blocked user {user.id if user else 'unknown'}")
        return None
