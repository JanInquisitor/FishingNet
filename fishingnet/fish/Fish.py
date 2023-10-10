import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
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
    followers_count = Column(Integer)
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

    def __init__(self, name, addresses, social_network, email, phone_number, last_activity, last_locations, pictures,
                 description, evidence_of_activity,
                 twitter_profile, linkedin_profile, facebook_profile, followers_count, friends_count, engagement_likes,
                 engagement_comments, engagement_shares, keywords_of_interest, website_url, references,
                 geolocation_data,
                 access_logs, notes_comments, user_agent_data, privacy_settings, legal_compliance, event_participation,
                 publications, content_metadata, sentiment_analysis):
        self.name = name
        self.addresses = addresses
        self.social_network = social_network
        self.email = email
        self.phone_number = phone_number
        self.last_activity = last_activity
        self.last_locations = last_locations
        self.pictures = pictures
        self.description = description
        self.evidence_of_activity = evidence_of_activity
        self.twitter_profile = twitter_profile
        self.linkedin_profile = linkedin_profile
        self.facebook_profile = facebook_profile
        self.followers_count = followers_count
        self.friends_count = friends_count
        self.engagement_likes = engagement_likes
        self.engagement_comments = engagement_comments
        self.engagement_shares = engagement_shares
        self.keywords_of_interest = keywords_of_interest
        self.website_url = website_url
        self.references = references
        self.geolocation_data = geolocation_data
        self.access_logs = access_logs
        self.notes_comments = notes_comments
        self.user_agent_data = user_agent_data
        self.privacy_settings = privacy_settings
        self.legal_compliance = legal_compliance
        self.event_participation = event_participation
        self.publications = publications
        self.content_metadata = content_metadata
        self.sentiment_analysis = sentiment_analysis
