import random
import datetime
from dao.TestDAO import TestDAO
from vo.TestVO import TestVO


def viewTestQuestionList(questionList):
    testQuestionList = []
    for i in questionList:
        if (questionList.index(i) == 0):
            for j in range(3):
                print('Type: One word answer')
                testQuestionList.append(i.pop(random.randrange(0, len(i))))
                print(testQuestionList)
        if (questionList.index(i) == 1):
            for j in range(3):
                print('type: True ot false')
                testQuestionList.append(i.pop(random.randrange(0, len(i))))
                print(testQuestionList)
        if (questionList.index(i) == 2):
            print('Type: Descriptive Answer')
            testQuestionList.append(i.pop(random.randrange(0, len(i))))
    return testQuestionList

def insertTestData(test_TopicId, test_LoginId, test_AnswerOne, test_AnswerTwo,
                   test_AnswerThree, test_AnswerFour, test_AnswerFive, test_AnswerSix, testQuestionsId):

    testVO = TestVO()
    testDAO = TestDAO()

    testVO.test_TopicId = test_TopicId
    testVO.test_LoginId = test_LoginId
    testVO.test_AnswerOne = test_AnswerOne
    testVO.test_AnswerTwo = test_AnswerTwo
    testVO.test_AnswerThree = test_AnswerThree
    testVO.test_AnswerFour = test_AnswerFour
    testVO.test_AnswerFive = test_AnswerFive
    testVO.test_AnswerSix = test_AnswerSix
    testVO.test_AnswerSeven = 'none'
    testVO.test_QuestionsId = testQuestionsId
    testVO.test_Time = datetime.datetime.now().strftime('%H:%M')
    testVO.test_Date = datetime.datetime.now().strftime('%d/%m/%Y')

    testDAO.insertTestData(testVO)

    return
