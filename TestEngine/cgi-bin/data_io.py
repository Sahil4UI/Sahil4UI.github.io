import mysql.connector as mc

connection = mc.connect(
    host="localhost",
    user = "root",
    database = "TEST_ENGINE_DB"
    )

cursor = connection.cursor()
def storeUser(obj):
    if obj.role =="teacher":
        table = "teachers"
    else:
        table = "students"
    query = f"insert into {table} (name,id,pwd,grade) values (%s,%s,%s,%s)"
    cursor.execute(query,(obj.name,obj.id,obj.pwd,obj.grade))
    connection.commit()


def loginUser(role,id,pwd):
    if role=="teacher":
        table = "teachers"
    else:
        table = "students"
    
    query = f"select * from {table} where id=%s and pwd=%s"
    cursor.execute(query,(id,pwd))
    data = cursor.fetchall()
    return data

def fetchStudentData(id):
    query = f"select * from students where id={id}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data
    

def fetchAllTest():
    query = "select * from test"
    cursor.execute(query)
    data = cursor.fetchall()
    return data



def insertTest(id,subject,grade):
    query = "insert into test(teacher_id,subject,grade) values (%s, %s,%s)"
    cursor.execute(query,(id,subject,grade))
    connection.commit()

def fetchMyTest(id):
    query = f"select * from test where teacher_id={id}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data


def getTest(id):
    query = f"select * from test where teacher_id={id}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def getTestInfo(grade,sub):
    query = f"select * from test where subject=%s and grade=%s"
    cursor.execute(query,(sub,grade))
    data = cursor.fetchall()
    return data

def getQuestions(test_id):
    query = f"select * from questions where test_id={test_id}"
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def updateQuestion(ques,question1,opt_1,opt_2,opt_3,opt_4,ans):
    query = f"update questions set ques=%s,opt_1=%s,opt_2=%s,opt_3=%s,opt_4=%s,ans=%s where ques like '{ques}%'"
    values=(question1,opt_1,opt_2,opt_3,opt_4,ans)
    cursor.execute(query,values)
    connection.commit()

def insertQues(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub):
    query = "insert into questions values(%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,sub)
    cursor.execute(query,values)
    connection.commit()


def saveResult(s_id,test_id,name,sub,grade,average,result):
    query = "insert into results values(%s,%s,%s,%s,%s,%s,%s)"
    values = (s_id,test_id,name,sub,grade,average,result)
    cursor.execute(query,values)
    connection.commit()

def getSubjects(grade):
    query = f"select subject from test where grade={grade}"
    cursor.execute(query)
    sub = cursor.fetchall()
    return sub

def getSub(t_id):
    query = f"select subject from test where teacher_id={t_id}"
    cursor.execute(query)
    sub = cursor.fetchone()
    return sub


def getAnswer(test_id):
    query=f"select ans from questions where test_id={test_id}"
    cursor.execute(query)
    ans = cursor.fetchall()
    return ans


def fetchQuestions(id):
    query = f'select * from questions where test_id="{id}"'
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def deleteTest(sub,grade):
    query = "delete from test where subject =%s and grade =%s"
    values = (sub,grade)
    cursor.execute(query,values)
    connection.commit()

def deleteQuestion(t_id,subject):
    query = "delete from questions where test_id =%s and subject =%s"
    values = (t_id,subject)
    cursor.execute(query,values)
    connection.commit()


def fetchName(s_id):
    query = f"select name from students where id={s_id}"
    cursor.execute(query)
    name = cursor.fetchone()
    return name

def fetch_Student_Res(s_id,role):
    if role == "student":
        query = f"select * from results where s_id={s_id}"
    else:
        query = f"select * from results where t_id={s_id}"

    cursor.execute(query)
    res = cursor.fetchall()
    return res