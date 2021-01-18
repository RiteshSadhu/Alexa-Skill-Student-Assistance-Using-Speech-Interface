from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from dao import engine
from vo.TopicVO import TopicVO
from vo.StudentVO import StudentVO


Base = declarative_base()

class TestVO(Base):
    print("in testvo class")
    __tablename__ = 'testmaster'
    testId = Column(Integer, primary_key=True)
    test_TopicId = Column(Integer, ForeignKey(TopicVO.topicId))
    test_LoginId = Column(Integer, ForeignKey(StudentVO.studentId))
    test_AnswerOne = Column(String(100))
    test_AnswerTwo = Column(String(100))
    test_AnswerThree = Column(String(100))
    test_AnswerFour = Column(String(100))
    test_AnswerFive = Column(String(100))
    test_AnswerSix = Column(String(100))
    test_AnswerSeven = Column(String(5000))
    test_QuestionsId = Column(String(100))
    test_Time = Column(String(20))
    test_Date = Column(String(20))
    test_ResultStatus = Column(String(20))


    def as_dict(self):
        return {
            'testId': self.testId,
            'test_TopicId': self.test_TopicId,
            'test_LoginId': self.test_LoginId,
            'test_AnswerOne': self.test_AnswerOne,
            'test_AnswerTwo': self.test_AnswerTwo,
            'test_AnswerThree': self.test_AnswerThree,
            'test_AnswerFour': self.test_AnswerFour,
            'test_AnswerFive': self.test_AnswerFive,
            'test_AnswerSix': self.test_AnswerSix,
            'test_AnswerSeven': self.test_AnswerSeven,
            'test_QuestionsId': self.test_QuestionsId,
            'test_Time': self.test_Time,
            'test_Date': self.test_Date,
            'test_ResultStatus': self.test_ReportStatus
        }

Base.metadata.create_all(engine)
