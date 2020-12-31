import cgi
import controller
form = cgi.FieldStorage()

id = form.getvalue('id')

if form.getvalue('test'):
    form_state = True
    subject = form.getvalue('sub')
    grade = form.getvalue('grade')
    controller.insertTest(id,subject,grade)
else:
    form_state = False

if form.getvalue('test_id'):
    subject = form.getvalue('sub')
    test_id = form.getvalue('test_id')
    ques = form.getvalue('ques')
    opt_1 = form.getvalue('opt_1')
    opt_2 = form.getvalue('opt_2')
    opt_3 = form.getvalue('opt_3')
    opt_4 = form.getvalue('opt_4')
    ans = form.getvalue('ans')
    controller.insertQuestion(test_id,ques,opt_1,opt_2,opt_3,opt_4,ans,subject)

test = controller.getTest(id)
print("Content-type:text/html\r\n\r\n")

print(
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="..\stylesheet\main.css">

</head>
<body>
    <h1>Create Test</h1>
""")
if form_state==False:
    print(f"""
        <form action="createTest.py">
            <input type="hidden" value={id} name='id'>
            <input type="hidden" value='create' name='test'>
            <table>
                <tr>
                    <td>Choose Subject</td>
                    <td>
                        <select name="sub">
                            <option>Choose Subject</option>
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
                    <td></td>
                    <td>
                        <input type="submit" value='Insert Question'>
                    </td>
                </tr>
            <table>
        </form>
    """)
print(
        f"""
        <h2>Start Inserting Questions</h2>
        <form action="createTest.py">
            <input type='hidden' value ={id} name='id'>""")

sub = controller.getSub(id)

print(f"""           <input type='hidden' value ={sub[0]} name='sub'>

            <table cellpadding=10px>
                <tr>
                    <td>Enter Test ID</td>
                    <td>
                        <select name="test_id">
                        """)
for i in range(len(test)):
    print(
        f"""<option value={test[i][0]}>{test[i][0]}</option>"""
    )
print(
        """
                        </select>
                    </td>
                </tr>
                <tr>
                    <td>Enter Question</td>
                    <td>
                        <textarea name="ques" rows=5 cols=50 placeholder="Enter Question">
                        </textarea>
                    </td>
                </tr>
                <tr>
                    <td>Enter Option 1</td>
                    <td>
                        <input type="text" placeholder="Enter Option 1" name="opt_1">
                    </td>
                </tr>
                <tr>
                    <td>Enter Option 2</td>
                    <td>
                        <input type="text" placeholder="Enter Option 2" name="opt_2">
                    </td>
                </tr>
                <tr>
                    <td>Enter Option 3</td>
                    <td>
                        <input type="text" placeholder="Enter Option 3" name="opt_3">
                    </td>
                </tr>
                <tr>
                    <td>Enter Option 4</td>
                    <td>
                        <input type="text" placeholder="Enter Option 4" name="opt_4">
                    </td>
                </tr>
                <tr>
                    <td>Enter Answer</td>
                    <td>
                        <input type="text" placeholder="Enter Answer" name="ans">
                    </td>
                </tr>
                <tr>
                    <td>
                        <input type="submit" value = "Submit">
                    </td>
                    <td>
                        <input type="reset" value = "Reset">
                        
                    </td>
                </tr>
            </table>
        </form>
</body>
</html>
"""
)