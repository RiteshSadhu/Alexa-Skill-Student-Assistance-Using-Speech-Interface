from dao import engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TopicVO(Base):
    print('In TopicVO')
    __tablename__ = 'topicmaster'
    topicId = Column('topicId', Integer, primary_key=True, autoincrement=True)
    topicName = Column('topicName', String(50), nullable=False)
    topicDescription = Column('topicDescription', String(500), nullable=False)

    def as_dict(self):
        return {
            'topicId': self.topicId,
            'topicName': self.topicName,
            'topicDescription': self.topicDescription
        }

Base.metadata.create_all(engine)