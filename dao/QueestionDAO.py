from dao import engine
from vo.QuestionVO import QuestionVO
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker



Session = sessionmaker(bind=engine)
session = Session()

print('in QuestionDAO')

class QuestionDAO():
    def viewQuestions(self, questionVO):
        print('in view Question at QuestionDAO')
        questionList = session.query(QuestionVO)\
            .filter(and_(QuestionVO.question_TopicId == questionVO.question_TopicId,
                         QuestionVO.question_QuestionTypeId == questionVO.question_QuestionTypeId)).all()

        print('questionList at QuestionDAO after query', questionList)
        return questionList

