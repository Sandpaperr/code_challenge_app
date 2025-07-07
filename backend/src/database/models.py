from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Specify what database we want to use
# using sqlite as it will run on my own machine
# if I host in the cloud change it to whatever address it is
engine = create_engine('sqlite:///database.db', echo=True)

# Object relational mapping classes 
Base = declarative_base()

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True)
    difficulty = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=False)
    title = Column(String, nullable=False)
    options = Column(String, nullable=False)
    correct_answer_id = Column(Integer, nullable=False)
    explanation = Column(String, nullable=False)


class ChallengeQuota(Base):
    __tablename__ = "challenge_quotas"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False, unique=False)
    remining_quota = Column(Integer, nullable=False, default=50)
    last_reset_date = Column(DateTime, default=datetime.now)

# Convert python code in SQL

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Make sure we don't keep creating duplicate sessions of our database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
