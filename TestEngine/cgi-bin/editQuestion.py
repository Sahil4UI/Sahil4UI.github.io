import cgi
import controller

d = { "%20":' ',"%21":'!',"%22":'"',"%23":'#',"%24":'$',
      "%25":'%',"%26":'&',"%27":"'","%28":'(',"%29":')',"%2A":'*',
        "%2B":'+',"%2C":',',"%2D":'-',"%2E":'.',"%2F":'/','%3D':'=',"%3F":"?"}
form = cgi.FieldStorage()
ques = form.getvalue('ques')
ques1  = form.getvalue('ques1')
opt_1 = form.getvalue("opt_1")
opt_2 = form.getvalue("opt_2")
opt_3 = form.getvalue("opt_3")
opt_4 = form.getvalue("opt_4")
ans = form.getvalue("ans")

for i in d:
    value = d.get(i)
    ques = ques.replace(i,value)
    ques1 = ques1.replace(i,value)

controller.updateQuestion(ques,ques1,opt_1,opt_2,opt_3,opt_4,ans)

print("Content-type:text/html\r\n\r\n")

print(
f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <title>Document</title>
</head></head>
<body></body>
</html>
""")