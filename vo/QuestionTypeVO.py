from dao import engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class QuestionTypeVO(Base):
    __tablename__ = 'questiontypemaster'
    questionTypeId = Column('questionTypeId', Integer, primary_key=True, autoincrement=True)
    questionTypeName = Column('questionTypeName', String(50), nullable=False)
    questionTypeDescription = Column('questionTypeDescription', String(200), nullable=False)

    def as_dict(self):
        return {
            'questionTypeId': self.questionTypeId,
            'questionTypeName': self.questionTypeName,
            'questionTypeDescription': self.questionTypeDescription
        }


Base.metadata.create_all(engine)