import cgi
import controller

form = cgi.FieldStorage()
role = form.getvalue("role")
name = form.getvalue("u_name")
id = form.getvalue("u_id")
pwd = form.getvalue("u_pwd")
grade = form.getvalue("grade")

controller.registerUser(role,name,id,pwd,grade)

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
    <h1>Registration Successfull</h1>
    <h2>Welcome {name}</h2>
""")
if role =="teacher":
    print(f"<a href='teachersLogin.py?id={id}'>Go to Teachers Page </a>")
else:
    print(f"<a href='studentsLogin.py?s_id={id}'>Go to Student Page </a>")
print("""</body>
</html>
""")