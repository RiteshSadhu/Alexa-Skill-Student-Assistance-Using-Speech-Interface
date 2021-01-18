from dao import engine
from sqlalchemy.orm import sessionmaker
from vo.StudentVO import StudentVO

Session = sessionmaker(bind=engine)
session = Session()

print('in StudentDAO')


class StudentDAO():
    def validateLogin(self, studentLoginVO):
        print('in StudentLoginDAO in validateLogin')
        studentLoginList = session.query(StudentVO).filter_by(studentEmail = studentLoginVO.studentEmail).all()
        return studentLoginList
