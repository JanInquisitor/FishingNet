import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from fishingnet.data.modelbase import SqlAlchemyBase


class Fish(SqlAlchemyBase):
    __tablename__ = 'fish'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    addresses = Column(Text)
    social_network = Column(String)
    email = Column(String)
    phone_number = Column(String)
    last_activity = Column(DateTime)
    last_locations = Column(Text)
    pictures = Column(Text)
    description = Column(Text)
    evidence_of_activity = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    twitter_profile = Column(String)
    linkedin_profile = Column(String)
    facebook_profile = Column(String)
    followers_count = Column(Integer)  # total followers overall in throughout all social media.
    friends_count = Column(Integer)
    engagement_likes = Column(Integer)
    engagement_comments = Column(Integer)
    engagement_shares = Column(Integer)
    keywords_of_interest = Column(Text)
    website_url = Column(String)
    references = Column(Text)
    geolocation_data = Column(Text)
    access_logs = Column(Text)
    notes_comments = Column(Text)
    user_agent_data = Column(Text)
    privacy_settings = Column(Text)
    legal_compliance = Column(Text)
    event_participation = Column(Text)
    publications = Column(Text)
    content_metadata = Column(Text)
    sentiment_analysis = Column(Text)
    creation_date = Column(DateTime, default=datetime.datetime.utcnow)  # Add creation_date column
    latest_addition = Column(DateTime)  # Add latest_addition column

    def __str__(self):
        return f"Fish Profile: {self.name} (ID: {self.id})\nEmail: {self.email}\nLast Activity: {self.last_activity}"

    def __repr__(self):
        return f"<Fish(name='{self.name}', id={self.id}, last_activity={self.last_activity}, email='{self.email}')>"
