import cgi
import controller

form = cgi.FieldStorage()

s_id = form.getvalue('s_id')
grade = form.getvalue('grade')
subjects = controller.getSubjects(grade)

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
    <hr>
    <form action="showTest.py">
        <input type="hidden" value={grade} name='grade'>
        <input type="hidden" value={s_id} name='s_id'>
        <table>
            <tr>
                <td>Choose Subject</td>
                <td>
                    <select name='sub'>
                    <option>Choose Subject</option>""")

for i in range(len(subjects)):
    print(f""" <option value={subjects[i][0]}>{subjects[i][0]}</option>""")

print("""
                    </select>
                </td>
            </tr>
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="submit">
                </td>
            </tr>
        </table>
    </form>
</body>
</html>
""")
