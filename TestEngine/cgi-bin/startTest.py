import cgi,controller

form = cgi.FieldStorage()

test_id = form.getvalue('t_id')
sub = form.getvalue('sub')
grade = form.getvalue('grade')
questions = controller.getQuestions(test_id)
s_id = form.getvalue('s_id')
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
    <h1>Start Test</h1>
    <hr>""")

print("<form action='submitTest.py' method='post'>")
print(f"""
            <input type="hidden" value={s_id} name="s_id">
            <input type="hidden" value={sub} name="sub">
            <input type="hidden" value={test_id} name="test_id">
            <input type="hidden" value={grade} name="grade">
            <input type="hidden" value={len(questions)} name="num_ques">
            
""")
opt_id=0
for i in range(len(questions)):
    print(
        f"""
            <h4>{questions[i][1]}</h4>
            <ul>
        """)
    for j in range(2,6):
        opt_id+=1
        print(f"""
            <li>
                <input type="radio" value={questions[i][j].replace(' ','+')} name='ques_{i+1}' id='{opt_id}'>
                <label for='{opt_id}'>{questions[i][j]}</label>
           
        """)
    print("""
     </li>
        </ul>
    """)
print("""
        
        <input type="submit">
    </form>
</body>
</html>
""")