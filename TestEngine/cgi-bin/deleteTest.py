import cgi
import controller

form = cgi.FieldStorage()

subject = form.getvalue('sub')
grade = form.getvalue('grade')


t_id =form.getvalue('t_id')

controller.deleteTest(subject,grade)
controller.deleteQuestion(t_id,subject)

print("Content-type:text/html\r\n\r\n")
print(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
    <h1>Delete Test : </h1>
    <hr>
    <form action="deleteTest.py">
        <input type="hidden" value={t_id} name="t_id" >
        <table>
                <tr>
                    <td>Choose Subject</td>
                    <td>
                        <select name="sub">
                            <option></option>
                            <option value="Computer Science">Computer</option>
                            <option value="math">Math</option>
                            <option value="General Knowledge">General Knowledge</option>
                            <option value="python">Python</option>
                            <option value = "science">Science</option>
                        </select>
                    </td>
                </tr>

                               <tr>
                    <td>Choose Grade</td>
                    <td>
                        <select name="grade" id="">
                            <option></option>
                            <option value="1">1<sup>st</sup></option>
                            <option value="2">2<sup>nd</sup></option>
                            <option value="3">3<sup>rd</sup></option>
                            <option value="4">4<sup>th</sup></option>
                            <option value="5">5<sup>th</sup></option>
                            <option value="6">6<sup>th</sup></option>
                            <option value="7">7<sup>th</sup></option>
                            <option value="8">8<sup>th</sup></option>
                            <option value="9">9<sup>th</sup></option>
                            <option value="10">10<sup>th</sup></option>
                            <option value="11">11<sup>th</sup></option>
                            <option value="12">12<sup>th</sup></option>
                        </select>
                    </td>
                </tr>
                <tr>
                    
                    <td>
                        <input type="submit" value='Delete Test'>
                    </td>
                    <td>
                        <a href="teachersLogin.py?id={t_id}">Check Test</a>
                    </td>
                </tr>
                
        </table>
    </form>
    <hr>
</body>
</html>
""")