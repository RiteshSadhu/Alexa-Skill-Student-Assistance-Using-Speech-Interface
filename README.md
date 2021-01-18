# Alexa skill of "Student Assistance using Speech Interface"
This Alexa skill is written in Python 3 and It will use the Database of my Final year project ["Student Assistance using speech Interface"](https://github.com/RiteshSadhu/Student-Assistance-Using-Speech-Interface "Final year project").
 
## Descrition:
This skill is designed for student's voice based test. Alexa will ask 6 question in per test.

### Alexa skill test flow
Registered Student can start their varble test by verify with OTP.
First 3 questions answers should be One or two words and next 3 questions answer will True or False.
Alexa will ask randomly selected question from question-database and store student response in database.

### Project and Source Description:
* Project Use MVC design design pattern.
* ORM query for database oprations
* server less architecture


--[controller](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/tree/main/controller)  
 |--[QuestionController.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/controller/QuestionController.py)  
 |--[StudentController.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/controller/StudentController.py)  
 |--[TestController.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/controller/TestController.py)  
 |--[TopicController.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/controller/TopicController.py) 
 |--[__init__.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/controller/__init__.py)   

--[dao](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/tree/main/dao)  
 |--[QueestionDAO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/dao/QueestionDAO.py)  
 |--[StudentDAO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/dao/StudentDAO.py)  
 |--[TestDAO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/dao/TestDAO.py)   
 |--[TopicDAO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/dao/TopicDAO.py)  
 |--[__init__.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/dao/__init__.py)  

--[vo](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/tree/main/vo)  
 |--[QuestionTypeVO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/QuestionTypeVO.py)  
 |--[QuestionVO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/QuestionVO.py)  
 |--[StudentVO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/StudentVO.py)  
 |--[TestVO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/TestVO.py)  
 |--[TopicVO.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/TopicVo.py)  
 |--[__init__.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/vo/__init__.py)  

-[lambda_funcation.py](https://github.com/RiteshSadhu/Alexa-Skill-Student-Assistance-Using-Speech-Interface/blob/main/lambda_function.py)  





#### This repo contains:
* Alexa skill kit
* Python 3.0 Libraries
* Bot Source code

#### Key notepoints of projects

