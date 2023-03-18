from typing import Optional
from data.User import User
from data import db_session
from passlib.handlers.sha2_crypt import sha512_crypt as crypto


# Notes: I can make this a class
# Have the controllers for the API and the app use this services maybe?

def find_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()


def create_user(name: str, email: str, password: str) -> Optional[User]:
    if find_user_by_email(email):
        return None

    user = User(email=email, name=name, hashed_password=hash_text(password))
    session = db_session.create_session()
    session.add(user)
    session.commit()
    return user


def hash_text(text: str) -> str:
    hashed_text = crypto.encrypt(text, rounds=171204)
    return hashed_text


def verify_hash(hashed_text: str, plain_text: str) -> bool:
    return crypto.verify(plain_text, hashed_text)


def login_user(email, password) -> Optional[User]:
    session = db_session.create_session()

    user = session.query(User).filter(User.email == email).first()

    if not user:
        return None

    if not verify_hash(user.hashed_password, password):
        return None

    return user
