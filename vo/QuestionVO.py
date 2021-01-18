from dao import engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from vo.TopicVO import TopicVO
from vo.QuestionTypeVO import QuestionTypeVO

Base = declarative_base()

class QuestionVO(Base):
    __tablename__ = 'questionmaster'
    questionId = Column('questionId', Integer, primary_key=True, autoincrement=True)
    question = Column('question', String(300), nullable=False)
    keyword = Column('keyword', String(4000), nullable=False)
    question_TopicId = Column('question_TopicId', Integer, ForeignKey(TopicVO.topicId), nullable=False)
    question_QuestionTypeId = Column('question_QuestionTypeId', Integer,
                                     ForeignKey(QuestionTypeVO.questionTypeId), nullable=False)

    def as_dict(self):
        return {
            'questionId': self.questionId,
            'questionName': self.questionName,
            'questionDescription': self.questionDescription,
            'question_TopicId': self.question_TopicId,
            'question_QuestionTypeId': self.question_QuestionTypeId
        }


Base.metadata.create_all(engine)
