import cgi
import controller

form =  cgi.FieldStorage()
role = form.getvalue('role')
id = form.getvalue('u_id')
pwd = form.getvalue('u_pwd')

user = controller.loginUser(role,id,pwd)
name = user[0][0]
all_test = controller.fetchAllTest()

print("Content-type:text/html\r\n\r\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
   </style>
    <link rel="stylesheet" href="..\stylesheet\main.css">
</head>
# <body>
    <h1>Registration Successfull</h1>
    <h2>Welcome {name}</h2>
""")
if role =="teacher":
    print(f"<a href='teachersLogin.py?id={id}'>Go to Teachers Page </a>")
else:
    print(f"<a href='studentsLogin.py?s_id={id}'>Go to Student Page </a>")

print("""
<h2>Test Created by you : </h2>
<table width="100%" border=2px cellpadding=10px>
    <tr>
        <th>Test ID </th>
        <th>Subject</th>
        <th>Grade</th>
        <th>Visit Test</th>
    </tr>
</table>
""")






print("""</body>
</html>
""")