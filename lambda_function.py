#alexa student assistance program

#import python libraries
import logging
import random
import string

#import alexa skill kit basic requirments
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard

#import controller
from controller.StudentController import validateLogin, sendOTP, sendLink
from controller.TopicController import viewTopic
from controller.QuestionController import viewQuestions
from controller.TestController import viewTestQuestionList, insertTestData
sb = SkillBuilder()

#log genration
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#all sessions
session_studentId = 'session_studentId'
session_studentEmail = 'session_studentEmail'
session_studentFirstName = 'session_studentFirstName'
session_studentLastName = 'session_studentLastName'
session_loginOTP = 'session_loginOTP'
session_answer1 = 'session_answer1'
session_answer2 = 'session_answer2'
session_answer3 = 'session_answer3'
session_answer4 = 'session_answer4'
session_answer5 = 'session_answer5'
session_answer6 = 'session_answer6'

session_questionCounter = 'session_questionCounter'

session_userValidated = 'closed'



#questionType
#questionTypeId '1' for 'one word answer' or 'short questions'
#questionTypeId '2' for 'True or False'

#get random topic
topicList = viewTopic()
topicId = topicList[0].topicId
print(topicId)

#get list of all questions objects
questionList= []
for i in [1,2,3]:
    questionTypeId = i
    questionList.append(viewQuestions(topicId, questionTypeId))
print('questionList at lambda_function...', questionList)


#get test question list
testQuestionList = viewTestQuestionList(questionList)
print('testQuestionList.........', testQuestionList)



testQuestionsIdList=[]



#LunchRequest Handeler
class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Hi, welcome to Student Asistance Program. " \
                      "This program designed for the Voice based test. " \
                      "For test enter username by saying 'My username is'"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Student Assistance", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response



class LoginIntentHandler(AbstractRequestHandler):
    #Login Intent Handler

    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("LoginIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print('inside LoginIntentHandler')

        #set request_slot
        request_slot = handler_input.request_envelope.request.intent.slots

        #get slot value of 'request_loginUsername'
        slot_loginUsername = request_slot['request_loginUsername']

        if slot_loginUsername.value is not None:
            print('slot_Username......', slot_loginUsername.value)

            studentDicList = validateLogin(slot_loginUsername.value)
            print('studentDicList.......', studentDicList)

            if len(studentDicList) != 0:

                if studentDicList[0]['studentStatus'] == 'active':
                    #store user data in session
                    handler_input.attributes_manager.session_attributes[session_studentId] = \
                        studentDicList[0]['studentId']
                    handler_input.attributes_manager.session_attributes[session_studentEmail] = \
                        studentDicList[0]['studentEmail']
                    handler_input.attributes_manager.session_attributes[session_studentFirstName] = \
                        studentDicList[0]['studentFirstName']
                    handler_input.attributes_manager.session_attributes[session_studentLastName] = \
                        studentDicList[0]['studentLastName']

                    OTP = ''.join((random.choice(string.digits)) for i in range(4))
                    #OTP = '3456'

                    print(OTP)

                    handler_input.attributes_manager.session_attributes[session_loginOTP] = OTP

                    receiver = studentDicList[0]['studentEmail']

                    #send OTP
                    sendOTP(OTP, receiver)

                    speech_text = "Welcome " + studentDicList[0]['studentFirstName'] + " " + \
                                  studentDicList[0]['studentLastName'] + \
                        ". Your OTP sent to registered Email address. Please enter your OTP by saying 'my otp is'"
                else:

                    speech_text = "Attention," + studentDicList[0]['studentFirstName'] + " " + \
                                  studentDicList[0]['studentLastName'] + " You are temporarily Blocked! " \
                                                                         "Ask faculty for more details."

            else:
                speech_text = "It seems that your Username is incorrect or you not registered for test, kindly try again"
        else:
            speech_text = "No Key set in Alexa Session !"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Login", speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class UserOTPIntentHandler(AbstractRequestHandler):
    #OTP intent handler

    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("UserOTPIntent")(handler_input)


    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print('inside UserOTPIntentHandler')

        # set request_slot
        request_slot = handler_input.request_envelope.request.intent.slots

        #get slot value in session
        slot_loginOTP = request_slot['request_loginOTP']
        print('slot_loginOTP..............', slot_loginOTP)
        print('slot_loginOTP.value........', slot_loginOTP.value)

        if slot_loginOTP.value is not None:

            if slot_loginOTP.value == handler_input.attributes_manager.session_attributes[session_loginOTP]:
                speech_text = "Your are authenticated. Now you can start your test by saying, 'begin test'"
                handler_input.attributes_manager.session_attributes[session_userValidated] = 'active'

            else:
                speech_text = "Sorry, wrong OTP. Please try agin."
        else:
            speech_text = "no key set in alexa"

        handler_input.attributes_manager.session_attributes[session_questionCounter] = 0



        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Otp verification", speech_text)).set_should_end_session(False)
        return  handler_input.response_builder.response



class TopicDescriptionIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("TopicDescriptionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        userValidated = handler_input.attributes_manager.session_attributes[session_userValidated]

        if userValidated == 'active':

            speech_text = "Hello, Your topic is '" + topicList[0].topicName + "'. " + " Description of topic is here,'" + \
                          topicList[0].topicDescription + " ' " + " Pleaase follow given instruction across the test." \
                                                                  " to begin say, 'I am ready'"

        else:
            speech_text = "You must login in test. Something went wrong."

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('Topic Description', speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response



class QuestionIntentHandler(AbstractRequestHandler):
    # Hander for fourth question

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("QuestionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        questionCounter = handler_input.attributes_manager.session_attributes[session_questionCounter]

        userValidated = handler_input.attributes_manager.session_attributes[session_userValidated]

        if userValidated == 'active':

            if questionCounter == 0:
                speech_text = "Now here your first question: '" + testQuestionList[0].question + "' To answer this Question " \
                                                                                                 "say, 'answer is'"


            elif questionCounter == 1:
                speech_text = "Now here your second question: '" + testQuestionList[
                    1].question + "' To answer this Question" \
                                  "say: 'answer is'"


            elif questionCounter == 2:
                speech_text = "Now here your third question: '" + testQuestionList[2].question + "' To answer this Question " \
                                                                                                 "say, 'answer is'"


            elif questionCounter == 3:
                speech_text = "Now here your fourth question: '" + testQuestionList[
                    3].question + "' To answer this Question " \
                                  "say, 'select true or false'"


            elif questionCounter == 4:

                speech_text = "Now here your fourth question: '" + testQuestionList[
                    4].question + "' To answer this Question" \
                                  "say, 'select true or false'"


            elif questionCounter == 5:

                speech_text = "Now here your sixth question: '" + testQuestionList[5].question + "' To answer this Question" \
                                                                                                 "say, 'select true or false'"

            else:
                speech_text = "Something went wrong."
        else:
            speech_text = "please login for test. say 'my username is'"


        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('Question', speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response



class AnswerIntentHandler(AbstractRequestHandler):
    #Hander for First Answer

    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("AnswerIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response

        # set request_slot
        request_slot = handler_input.request_envelope.request.intent.slots

        # get slot value in session
        slot_Answer = request_slot['request_Answer']

        questionCounter = handler_input.attributes_manager.session_attributes[session_questionCounter]

        userValidated = handler_input.attributes_manager.session_attributes[session_userValidated]

        if userValidated == 'active':

            if questionCounter == 0:
                handler_input.attributes_manager.session_attributes[session_answer1] = slot_Answer.value
                speech_text = "Your first response is saved. Now for next question say, 'next question please '"
                testQuestionsIdList.append(str(testQuestionList[0].questionId))

            elif questionCounter == 1:
                handler_input.attributes_manager.session_attributes[session_answer2] = slot_Answer.value
                speech_text = "Your second response is stored. Now for next question say, 'next question please '"
                testQuestionsIdList.append(str(testQuestionList[1].questionId))

            elif questionCounter == 2:
                handler_input.attributes_manager.session_attributes[session_answer3] = slot_Answer.value
                speech_text = "Your third response is stored. Just 3 more to go. " \
                      "Remember next three questions are boolean, answer must be True or False. " \
                              "Now, for next question say: 'next question please' "
                testQuestionsIdList.append(str(testQuestionList[2].questionId))

            else:
                speech_text = "Something went wrong."

            questionCounter +=1
            handler_input.attributes_manager.session_attributes[session_questionCounter] = questionCounter

        else:
            speech_text = "Please login for test. say 'my username is'"


        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('Answer', speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class BooleanAnswerIntentHandler(AbstractRequestHandler):
    # Handler for fourth question

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("BooleanAnswerIntent")(handler_input)

    def handle(self, handler_input):

        # set request_slot
        request_slot = handler_input.request_envelope.request.intent.slots

        # get slot value in session
        slot_Answer = request_slot['request_booleanAnswer']
        speech_text = ''

        questionCounter = handler_input.attributes_manager.session_attributes[session_questionCounter]

        userValidated = handler_input.attributes_manager.session_attributes[session_userValidated]

        if userValidated == 'active':

            if slot_Answer.value is not None:

                if questionCounter == 3:
                    handler_input.attributes_manager.session_attributes[session_answer4] = slot_Answer.value
                    speech_text = "Your fourth response is stored. " \
                                  "I hope You are doing Good, You are Just Two Questions Away. " \
                                  "now for next question say: 'next question please'"
                    testQuestionsIdList.append(str(testQuestionList[3].questionId))

                elif questionCounter == 4:
                    handler_input.attributes_manager.session_attributes[session_answer5] = slot_Answer.value
                    speech_text = "Your fifth response is successfully stored. " \
                                  " Now for next question say: 'next question please'"
                    testQuestionsIdList.append(str(testQuestionList[4].questionId))

                elif questionCounter == 5:
                    handler_input.attributes_manager.session_attributes[session_answer6] = slot_Answer.value
                    speech_text = "Your sixth response is stored. " \
                                  "Your test is completed. For submit test say: 'submit test'"
                    testQuestionsIdList.append(str(testQuestionList[5].questionId))
                    testQuestionsIdList.append(str(testQuestionList[6].questionId))

                else:
                    speech_text = "Something went wrong."

                questionCounter +=1
                handler_input.attributes_manager.session_attributes[session_questionCounter] = questionCounter
            else:
                speech_text = 'No answer submitted'
        else:
            speech_text = "Please login for test. say 'my username is'"


        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('Boolean Answer', speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response


class SubmitTestIntentHandler(AbstractRequestHandler):
    #Handler for fourth question

    def can_handle(self, handler_input):
        #type: (HandlerInput) -> bool
        return is_intent_name("SubmitTestIntent")(handler_input)

    def handle(self, handler_input):
        #type: (HandlerInput) -> Response

        userValidated = handler_input.attributes_manager.session_attributes[session_userValidated]

        if userValidated == 'active' :

            testQuestionsId = ','.join(testQuestionsIdList)

            insertTestData(topicId, handler_input.attributes_manager.session_attributes[session_studentId],
                           handler_input.attributes_manager.session_attributes[session_answer1],
                           handler_input.attributes_manager.session_attributes[session_answer2],
                           handler_input.attributes_manager.session_attributes[session_answer3],
                           handler_input.attributes_manager.session_attributes[session_answer4],
                           handler_input.attributes_manager.session_attributes[session_answer5],
                           handler_input.attributes_manager.session_attributes[session_answer6],
                           testQuestionsId)

            speech_text = "Test sucessfully submitted. " + "Thank you. now close "

            receiver = handler_input.attributes_manager.session_attributes[session_studentEmail]
            sendLink(receiver)

        else:
            speech_text = "please login for test. say 'my username is'"


        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard('Student Assistance', speech_text)).set_should_end_session(False)
        return handler_input.response_builder.response








class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "You can say hello to me!"

        handler_input.response_builder.speak(speech_text).ask(speech_text).set_card(
            SimpleCard("Hello World", speech_text))
        return handler_input.response_builder.response




class FallbackIntentHandler(AbstractRequestHandler):
    """AMAZON.FallbackIntent is available in these locales.
    This handler will not be triggered except in supported locales,
    so it is safe to deploy on any locale.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = (
            "The Hello World skill can't help you with that.  "
            "You can say hello!!")
        reprompt = "You can say hello!!"
        handler_input.response_builder.speak(speech_text).ask(reprompt)
        return handler_input.response_builder.response




class CancelAndStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.CancelIntent")(handler_input) \
               or is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speech_text = "Goodbye!"

        handler_input.response_builder.speak(speech_text).set_card(
            SimpleCard("Hello World", speech_text)).set_should_end_session(True)
        return handler_input.response_builder.response




class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # any cleanup logic goes here

        return handler_input.response_builder.response



class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message."""

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        # Log the exception in CloudWatch Logs
        print(exception)
        logger.error(exception, exc_info=True)


        speech = "Sorry, I didn't get it. Can you please say it again!!"
        handler_input.response_builder.speak(speech).ask(speech)
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(LoginIntentHandler())
sb.add_request_handler(UserOTPIntentHandler())
sb.add_request_handler(TopicDescriptionIntentHandler())
sb.add_request_handler(QuestionIntentHandler())
sb.add_request_handler(AnswerIntentHandler())
sb.add_request_handler(BooleanAnswerIntentHandler())
sb.add_request_handler(SubmitTestIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()