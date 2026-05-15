import logging
import typing

from sqlalchemy import Column, Integer, String, BigInteger, Boolean, Text, select, delete

from repo.modules.base import Base, BaseRepo


class MessageData(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)

    connection_id = Column(String(4112))
    message_id = Column(BigInteger)
    message = Column(Text, default=None)

    is_sticker = Column(Boolean, default=False)
    is_media = Column(Boolean, default=False)

    sticker = Column(Text, default=None)

    media = Column(Text, default=None)
    media_type = Column(Text, default=None)


class MessagesRepo(BaseRepo):
    def __init__(self, s):
        super().__init__(s)

    def add(self, message: MessageData) -> bool:
        try:
            with self._s.begin() as s:
                s.add(message)

            return True
        except Exception as e:
            logging.error(e)
            return False

    def get(self, message_id: int, connection_id: str) -> typing.Optional[MessageData]:
        with self._s.begin() as s:
            return s.execute(select(MessageData).where(MessageData.message_id == message_id,
                                                       MessageData.connection_id == connection_id)).scalar_one_or_none()

    def delete(self, message: MessageData) -> bool:
        try:
            with self._s.begin() as s:
                s.delete(message)
            return True
        except Exception as e:
            logging.error(e)
            return False

    def delete_by_cid(self, connection_id) -> bool:
        try:
            with self._s.begin() as s:
                s.execute(delete(MessageData).where(MessageData.connection_id == connection_id))
            return True
        except Exception as e:
            logging.error(e)
            return False
