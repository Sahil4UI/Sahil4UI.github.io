import data_io

class User:
    def __init__(self,role,name,id,pwd,grade):
        self.role = role
        self.name = name
        self.id = id
        self.pwd = pwd
        self.grade = grade

def registerUser(role,name,id,pwd,grade):
    obj = User(role,name,id,pwd,grade)
    data_io.storeUser(obj)

def loginUser(role,id,pwd):
    user = data_io.loginUser(role,id,pwd)
    return user


def fetchStudentData(id):
    data = data_io.fetchStudentData(id)
    return data
    
def fetchMyTest(id):
    my_test = data_io.fetchMyTest(id)
    return my_test

def fetchAllTest():
    data = data_io.fetchAllTest()
    return data

def fetchQuestions(id):
    data = data_io.fetchQuestions(id)
    return data

def insertTest(id,subject,grade):
    data_io.insertTest(id,subject,grade)


def getTest(id):
    test = data_io.getTest(id)
    return test



def getTestInfo(grade,sub):
    testInfo = data_io.getTestInfo(grade,sub)
    return testInfo

def getSubjects(grade):
    sub = data_io.getSubjects(grade)
    return sub

def getSub(t_id):
    subjects = data_io.getSub(t_id)
    return subjects

def getQuestions(test_id):
    questions = data_io.getQuestions(test_id)
    return questions

def insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub):
    data_io.insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub)

def getAnswer(test_id):
    ans = data_io.getAnswer(test_id)
    return ans

def deleteTest(sub,grade):
    data_io.deleteTest(sub,grade)

def deleteQuestion(t_id,subject):
    data_io.deleteQuestion(t_id,subject)

def updateQuestion(ques,question1,opt_1,opt_2,opt_3,opt_4,ans):
    data_io.updateQuestion(ques,question1,opt_1,opt_2,opt_3,opt_4,ans)

def fetchName(s_id):
    name = data_io.fetchName(s_id)
    return name

def saveResult(s_id,test_id,name,sub,grade,average,result):
    data_io.saveResult(s_id,test_id,name,sub,grade,average,result)

def fetch_Student_Res(s_id,role):
    res = data_io.fetch_Student_Res(s_id,role)
    return res