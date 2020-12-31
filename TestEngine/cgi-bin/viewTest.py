import cgi
import controller

form = cgi.FieldStorage()

t_id =form.getvalue('t_id')

questions = controller.fetchQuestions(t_id)

print("Content-type:text/html\r\n\r\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="..\stylesheet\main.css">
</head>
<body>
    <h1>Test</h1>
    <hr>""")
print("<div>")

for i in range(len(questions)):
    print(f"""
        <h4>{questions[i][1]}</h4>
        <ul>
            <li>Option 1 : {questions[i][2]}</li>
            <li>Option 2 : {questions[i][3]}</li>
            <li>Option 3 : {questions[i][4]}</li>
            <li>Option 4 : {questions[i][5]}</li>
            <li>Answer : {questions[i][6]}</li>            
        </ul>
    """)


print("""
    </div>
</body>
</html>
""")