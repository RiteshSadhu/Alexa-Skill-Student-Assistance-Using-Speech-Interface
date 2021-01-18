
from dao.QueestionDAO import QuestionDAO
from vo.QuestionVO import QuestionVO
print('in StudentLoginController')

def viewQuestions(topicId, questionTypeId):
    print('in viewQuestions at QuestionController')
    questionVO = QuestionVO()
    questionDAO = QuestionDAO()

    questionVO.question_TopicId = topicId
    questionVO.question_QuestionTypeId =questionTypeId

    questionList =questionDAO.viewQuestions(questionVO)

    print('questionList at QuestionController after search',  questionList)

    return questionList








