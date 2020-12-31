import cgi
import controller
import math
form = cgi.FieldStorage()
s_id = form.getvalue('s_id')
test_id = form.getvalue('test_id')
sub = form.getvalue('sub')
grade = form.getvalue('grade')
num_ques = form.getvalue('num_ques')
answers = []
attempted = 0
correct=0
incorrect=0

answer = controller.getAnswer(test_id)

for i in range(int(num_ques)):
    ans = form.getvalue(f'ques_{i+1}')
    if ans:
        answers.append(str(ans).replace('+'," "))
        attempted+=1
    else:
        answers.append(None)

for i in range(int(num_ques)):
    if answers[i]==answer[i][0]:
        correct+=1
    else:
        incorrect+=1

average = math.floor(((correct)/int(num_ques))*100)
result = None
if average > 40:
    result="Pass"
else:
    result="Fail"
name = controller.fetchName(s_id)

controller.saveResult(s_id,test_id,name[0],sub,grade,average,result)

print("Content-type:text/html\r\n\r\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Test Submitted</h1>
    <hr>
    <h2>Name : {name[0]}</h2>
    <h2>Roll No : {s_id}</h2>
    <h2>Number of Questions : {num_ques}</h2>
    <h4>Attempted : {attempted}</h4>
    <h4>Correct : {correct}</h4>
    <h4>Incorrect : {incorrect}</h4>
    <h4>% = {average}%</h4>
    <h4>Result : {result}</h4>


</body>
</html>""")
