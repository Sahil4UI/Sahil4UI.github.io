import model 

def registerUser(role,name,id,pwd,grade):
    model.registerUser(role,name,id,pwd,grade)

def loginUser(role,id,pwd):
    user = model.loginUser(role,id,pwd)
    return user

def fetchStudentData(id):
    data =  model.fetchStudentData(id)
    return data

def fetchMyTest(id):
    my_test=model.fetchMyTest(id)
    return my_test


def fetchAllTest():
    all_test = model.fetchAllTest()
    return all_test

def insertTest(id,subject,grade):
    model.insertTest(id,subject,grade)


def getTest(id):
    test = model.getTest(id)
    return test

def getTestInfo(grade,sub):
    testinfo = model.getTestInfo(grade,sub)
    return testinfo

def insertQuestion(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub):
    model.insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub)

def getQuestions(test_id):
    questions = model.getQuestions(test_id)
    return questions

def fetchQuestions(id):
    data = model.fetchQuestions(id)
    return data

def getSubjects(grade):
    sub = model.getSubjects(grade)
    return sub

def getAnswer(test_id):
    ans = model.getAnswer(test_id)
    return ans

def getSub(t_id):
    subject = model.getSub(t_id)
    return subject

def deleteTest(sub,grade):
    model.deleteTest(sub,grade)

def deleteQuestion(t_id,subject):
    model.deleteQuestion(t_id,subject)


def updateQuestion(ques,question1,opt_1,opt_2,opt_3,opt_4,ans):
    model.updateQuestion(ques,question1,opt_1,opt_2,opt_3,opt_4,ans)

def fetchName(s_id):
    name = model.fetchName(s_id)
    return name

def saveResult(s_id,test_id,name,sub,grade,average,result):
    model.saveResult(s_id,test_id,name,sub,grade,average,result)

def fetch_Student_Res(s_id,role):
    res = model.fetch_Student_Res(s_id,role)
    return res