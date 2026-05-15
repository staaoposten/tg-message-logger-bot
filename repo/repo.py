from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from repo.modules.base import Base
from repo.modules.messages import MessagesRepo
from repo.modules.users import UsersRepo


class Repo:
    def __init__(self, username: str, password: str, ip: str, port: int, db: str) -> None:
        self.engine = create_engine(f'mysql+pymysql://{username}:{password}@{ip}:{port}/{db}', pool_pre_ping=True, pool_recycle=3600)

        self._Session = sessionmaker(bind=self.engine)

        Base.metadata.create_all(self.engine)

    def save(self) -> None:
        with self._Session() as session:
            session.commit()

    @property
    def users(self) -> UsersRepo:
        return UsersRepo(s=self._Session)

    @property
    def messages(self) -> MessagesRepo:
        return MessagesRepo(s=self._Session)
