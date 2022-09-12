from app.server.database import Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
    code = Column(String, nullable=False)

class Result(Base):
    __tablename__ = 'results'

    id = Column(UUID(as_uuid=True), primary_key=True, server_default='gen_random_uuid()')
    user = Column(Integer, ForeignKey('users.id'))
    soil = Column(String, nullable=False)
    s1 = Column(Float, nullable=False)
    s2 = Column(Float, nullable=False)
    s3 = Column(Float, nullable=False)
    s4 = Column(Float, nullable=False)
    s5 = Column(Float, nullable=False)
    s6 = Column(Float, nullable=False)
    s7 = Column(Float, nullable=False)
    s8 = Column(Float, nullable=False)
    s9 = Column(Float, nullable=False)
    s10 = Column(Float, nullable=False)
    s11 = Column(Float, nullable=False)
    s12 = Column(Float, nullable=False)
    s13 = Column(Float, nullable=False)
    s14 = Column(Float, nullable=False)
    s15 = Column(Float, nullable=False)
    s16 = Column(Float, nullable=False)
    s17 = Column(Float, nullable=False)
    s18 = Column(Float, nullable=False)
    s19 = Column(Float, nullable=False)
    s20 = Column(Float, nullable=False)