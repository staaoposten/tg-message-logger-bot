import logging
import typing

from sqlalchemy import Column, String, BigInteger, select

from repo.modules.base import Base, BaseRepo


class UserData(Base):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    connection_id = Column(String(1028), unique=True)
    channel_id = Column(BigInteger)
    language = Column(String(4), default="en")


class UsersRepo(BaseRepo):
    def __init__(self, s) -> None:
        super().__init__(s)

    def add(self, user: UserData) -> bool:
        s = self.get(user.id)
        if s is not None:
            return False

        try:
            with self._s.begin() as s:
                s.add(user)
            return True
        except Exception as e:
            logging.error(e)
            return False

    def get(self, id: int) -> typing.Optional[UserData]:
        with self._s.begin() as s:
            return s.execute(select(UserData).where(UserData.id == id)).scalar_one_or_none()

    def get_by_connection(self, connection_id: str) -> typing.Optional[UserData]:
        with self._s.begin() as s:
            return s.execute(select(UserData).where(UserData.connection_id == connection_id)).scalar_one_or_none()

    def delete(self, user: UserData) -> bool:
        try:
            with self._s.begin() as s:
                s.delete(user)
            return True
        except Exception as e:
            logging.error(e)
            return False
