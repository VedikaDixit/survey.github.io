import uuid
import mysql.connector as sql
from flask import jsonify as json

db = sql.connect(
    host="localhost",
    user="root",
    database="servey" 
)

cursor = db.cursor()

def getquesfir():
    cursor.execute("SELECT q.quesid,q.question, o.optid, o.option FROM question q JOIN option o ON q.quesid = o.quesid WHERE q.quesid = 1;")
    data = cursor.fetchall()
    option=[]
    for i in data:
        option.append({'optid':i[2],'opt':i[3]})
    quesid=data[0][0]
    ques=data[0][1]
    return {'options':option,'question_id':quesid,'question':ques}

def getnext(data):
    id=int(data['question_id'])
    optionid=int(data['selected_option_id'])
    cursor.execute('SELECT q2.quesid AS next_quesid, q2.question AS next_question,o2.optid AS next_optid,o2.option AS next_option FROM option o1 JOIN question q1 ON o1.quesid = q1.quesid LEFT JOIN nextques n ON o1.quesid = n.quesid AND o1.optid = n.optid LEFT JOIN question q2 ON n.nextquesid = q2.quesid LEFT JOIN option o2 ON q2.quesid = o2.quesid WHERE o1.quesid = %s AND o1.optid = %s;',(id,optionid))
    result=cursor.fetchall()
    option=[]
    for i in result:
        option.append({'optid':i[2],'opt':i[3]})
    quesid=result[0][0]
    ques=result[0][1] 
    return {'options':option,'question_id':quesid,'question':ques}