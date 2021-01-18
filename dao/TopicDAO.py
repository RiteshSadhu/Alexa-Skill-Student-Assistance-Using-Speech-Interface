import random
from dao import engine
from vo.TopicVO import TopicVO
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

print('In TopicDAO')

class TopicDAO():
    def viewTopic(self):
        print('in topic dao viewTopic')
        topicVOList = session.query(TopicVO).filter_by(topicId = random.randrange(1, session.query(TopicVO).count())).all()
        print('topicVOList....at TopicDAO......', topicVOList)
        return topicVOList