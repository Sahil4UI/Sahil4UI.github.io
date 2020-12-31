import cgi
import controller

form = cgi.FieldStorage()
s_id = form.getvalue('s_id')
grade = form.getvalue('grade')
sub = form.getvalue('sub')
test = controller.getTestInfo(grade,sub)


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
if len(test)==0:
    print("<h2>No Test Available for This Subject</h2>")
else:
    print("""
        <h2>Test Available</h2>
        <table width='100%' border=2px cellpadding=10px>
            
            <tr>
                <th>Test ID</th>
                <th>Subject</th>
                <th>Grade</th>
                <th>Start Test</th>
            </tr>""")
    for i in range(len(test)):
        print(f"""
            <tr>
                <td>{test[i][0]}</td>
                <td>{test[i][1]}</td>
                <td>{test[i][2]}</td>
                <td>
                    <a href="startTest.py?t_id={test[i][0]}&s_id={s_id}&grade={grade}&sub={sub}">Start Test</a>
                </td>
            </tr>
        """)

print("""
        </table>
</body>
</html>
""")