from typing import Optional
from fishingnet.authentication.User import User
from fishingnet.data import db_session
from passlib.handlers.sha2_crypt import sha512_crypt as crypto


class UserService:
    @staticmethod
    def find_user_by_email(email: str) -> Optional[User]:
        session = db_session.create_session()
        return session.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(name: str, email: str, password: str) -> Optional[User]:
        if UserService.find_user_by_email(email):
            return None

        hashed_password = UserService.hash_text(password)
        user = User(email=email, name=name, hashed_password=hashed_password)
        session = db_session.create_session()
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def hash_text(text: str) -> str:
        hashed_text = crypto.encrypt(text, rounds=171204)
        return hashed_text

    @staticmethod
    def verify_hash(hashed_text: str, plain_text: str) -> bool:
        return crypto.verify(plain_text, hashed_text)

    @staticmethod
    def login_user(email, password) -> Optional[User]:
        session = db_session.create_session()
        user = session.query(User).filter(User.email == email).first()

        if not user:
            return None

        if not UserService.verify_hash(user.hashed_password, password):
            return None

        return user
