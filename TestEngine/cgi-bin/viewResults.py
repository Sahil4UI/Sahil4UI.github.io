import cgi
import controller

form = cgi.FieldStorage()

if form.getvalue('s_id'):
    role = "student"
    s_id = form.getvalue('s_id')
    result = controller.fetch_Student_Res(s_id,role)

if form.getvalue('t_id'):
    role="teacher"
    t_id = form.getvalue('t_id')
    result = controller.fetch_Student_Res(t_id,role)

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
    <h1>RESULT Page</h1>
    <table border="2px" cellpadding="12px" width="100%">
        <tr>
            <th>S_No.</th>
            <th>Student ID</th>
            <th>Teacher ID</th>
            <th>Student Name</th>
            <th>Subject</th>
            <th>Grade</th>
            <th>Average</th>
            <th>Result</th>
        </tr>""")
for i in range(len(result)):
    print(f"""<tr>
                    <td>{i+1}.</td>
                    <td>{result[i][0]}</td>
                    <td>{result[i][1]}</td>
                    <td>{result[i][2]}</td>
                    <td>{result[i][4]}</td>
                    <td>{result[i][3]}</td>
                    <td>{result[i][5]}%</td>
                    <td>{result[i][6]}</td>
            </tr>
    """)
print("""    </table>
</body>
</html>""")
