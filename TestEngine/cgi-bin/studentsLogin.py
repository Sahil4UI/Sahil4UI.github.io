import cgi,controller

form = cgi.FieldStorage()
s_id = form.getvalue("s_id")
my_data = controller.fetchStudentData(s_id)

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
    <h1>Student Dashboard</h1>
    <h4>Name : {my_data[0][0]}</h4>
    <h4>Grade : {my_data[0][3]}</h4>
    <nav>
        <ul>
            <li>
                <a href="giveTest.py?s_id={s_id}&grade={my_data[0][3]}">Give Test</a>
            </li>
            <li>
                <a href="viewResults.py?s_id={s_id}">View Results</a>
            </li>
        </ul>
    </nav>
    
    <h2>Test Given By You : </h2>
    <table ws_idth="100%" border=2px cellpadding=12px>
        <tr>
            <th>Test s_ID </th>
            <th>Subject</th>
            <th>Grade</th>
            <th>Visit Test</th>
        </tr>
    </table>

</body>
</html>
""")