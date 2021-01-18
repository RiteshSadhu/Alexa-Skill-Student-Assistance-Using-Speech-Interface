from vo.TopicVO import TopicVO
from dao.TopicDAO import TopicDAO

print('In topicController')

def viewTopic():
    print('in viewTopic at topicController')
    topicDAO = TopicDAO()
    topicList = topicDAO.viewTopic()
    return topicList