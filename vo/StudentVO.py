from dao import engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StudentVO(Base):
    print('in StudentLoginVOClass')
    __tablename__ = 'studentmaster'

    studentId = Column(Integer, primary_key=True)
    studentFirstName = Column(String(30))
    studentLastName = Column(String(30))
    studentGender = Column(String(20))
    studentEmail = Column(String(40))
    studentContactNumber = Column(Integer)
    studentStatus = Column(String(20))

    def as_dict(self):
        return {
            'studentId': self.studentId,
            'studentFirstName': self.studentFirstName,
            'studentLastName': self.studentLastName,
            'studentGender': self.studentGender,
            'studentEmail': self.studentEmail,
            'studentContactNunmber': self.studentContactNumber,
            'studentStatus': self.studentStatus
        }


Base.metadata.create_all(engine)
