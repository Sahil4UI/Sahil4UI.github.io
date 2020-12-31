import cgi
import controller
form= cgi.FieldStorage()
t_id = form.getvalue("t_id")

questions = controller.getQuestions(t_id)
index=0

if form.getvalue("index"):
    index = form.getvalue("index")





print("Content-type:text/html\r\n\r\n")
print(
f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="..\stylesheet\main.css">

</head>
    <h1>Edit Test</h1>
    <h2>Total No of Questions : {len(questions)}</h2>
    <form action='editTest.py'>
        <input type="hidden"  name="t_id" value={t_id}>
        
        <table>
            <tr>
                <td>Enter Question No You want to Edit : </td>
                <td>
                    <select name='index'>
""")
for i in range(len(questions)):
    print(
        f"""
        <option value={i+1}>{i+1}</option>
        """
    )

print("""                    </select>
                <input type="submit" value="GO">
                </td>
            </tr>

        </table>
    </form>
""")

if form.getvalue("index"):
    
    question = questions[int(index)-1][1]
    opt_1 = questions[int(index)-1][2]
    opt_2 = questions[int(index)-1][3]
    opt_3 = questions[int(index)-1][4]
    opt_4 = questions[int(index)-1][5]
    ans = questions[int(index)-1][6]


    print(f"""
        <form action="editQuestion.py">
            <input type="hidden" value={question} name="ques">
            <table>
                    <tr>
                        <td>Enter Question</td>
                        <td>
                            <textarea name="ques1" rows=5 cols=50 placeholder="Enter Question">{question}</textarea>
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Option 1</td>
                        <td>
                            <input type="text" placeholder="Enter Option 1" name="opt_1"  value="{opt_1}">
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Option 2</td>
                        <td>
                            <input type="text" placeholder="Enter Option 2" name="opt_2" value="{opt_2}">
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Option 3</td>
                        <td>
                            <input type="text" placeholder="Enter Option 3" name="opt_3" value="{opt_3}">
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Option 4</td>
                        <td>
                            <input type="text" placeholder="Enter Option 4" name="opt_4" value="{opt_4}">
                        </td>
                    </tr>
                    <tr>
                        <td>Enter Answer</td>
                        <td>
                            <input type="text" placeholder="Enter Answer" name="ans" value="{ans}">
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

    """)





    
("""
<body>
</body>
</html>
""")