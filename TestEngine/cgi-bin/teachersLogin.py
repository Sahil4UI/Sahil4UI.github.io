import cgi
import controller


form = cgi.FieldStorage()

id = form.getvalue("id")
my_test = controller.fetchMyTest(id)

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
    <h1>Teacher Dashboard</h1>
    <nav>
        <ul>
            <li>
                <a href="createTest.py?id={id}">Create Test</a>
            </li>
            <li>
                <a href="viewTest.py">View Test</a>
            </li>
            <li>
                <a href="editTest.py?t_id={id}">Edit Test</a>
            </li>
            <li>
                <a href="deleteTest.py?t_id={id}">Delete Test</a>
            </li>
            <li>
                <a href="viewResults.py?t_id={id}">View Result</a>
            </li>
        </ul>
    </nav>
    
    <h2>Test Created By You : </h2>
    <table width="100%" border=2px cellpadding=12px>
        <tr>
            <th>Test ID </th>
            <th>Subject</th>
            <th>Grade</th>
            <th>Visit Test</th>
        </tr>
""")

for i in range(len(my_test)):
    print(f"""
    <tr>
        <td>{my_test[i][0]}</td>
        <td>{my_test[i][1]}</td>
        <td>{my_test[i][2]}</td>
        <td>
            <a href="viewTest.py?t_id={my_test[i][0]}">Visit Test</a>
        </td>
    </tr>
    """)


print("""
    </table>

</body>
</html>
""")