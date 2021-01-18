import smtplib

from dao.StudentDAO import StudentDAO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from vo.StudentVO import StudentVO

print('in StudentLoginController')


def validateLogin(loginUsername):
    print('at validateLogin>>>>>>>>>>>>>>>>>..', loginUsername)

    studentVO = StudentVO()
    studentDAO = StudentDAO()

    studentVO.studentEmail = (loginUsername.lower()) + "@gmail.com"

    print('student email....', studentVO.studentEmail)

    studentVOList = studentDAO.validateLogin(studentVO)

    print('studentLoginVOList ..........', studentVOList)

    print('type of studentLoginVOList......', type(studentVOList))

    studentDictList = [i.as_dict() for i in studentVOList]

    print('studentDictList........', studentDictList)

    return studentDictList


def sendOTP(OTP, receiver):
    print('in sendOTP')

    sender = "studentassistence.donotreply4@gmail.com"
    msg = MIMEMultipart()

    msg['Form'] = sender
    msg['To'] = receiver
    msg['Subject'] = "One Time Password is:"

    msg.attach(MIMEText(OTP, 'plain'))
    print('mail forwarded')

    # smtp mail server setup
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    print('before login')

    # login details for mail server
    server.login(sender, "cjp_@1234")
    text = msg.as_string()

    # send email
    server.sendmail(sender, receiver, text)
    # email sent

    # mail server quit.
    server.quit()

def sendLink(receiver):
    print('in sendOTP')

    sender = "studentassistence.donotreply4@gmail.com"
    msg = MIMEMultipart()

    msg['Form'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Attention for second round."
    message = "Section one is complated." \
                "for next round logon on this link. " \
              "http://127.0.0.1:/studentLogin"

    msg.attach(MIMEText(message, 'plain'))
    print('mail forwarded')

    # smtp mail server setup
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    print('before login')

    # login details for mail server
    server.login(sender, "cjp_@1234")
    text = msg.as_string()

    # send email
    server.sendmail(sender, receiver, text)
    # email sent

    # mail server quit.
    server.quit()
