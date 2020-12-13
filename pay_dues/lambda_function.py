import pymysql
import json
import time

endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'


# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def get_serial_no():
    cursor = connection.cursor()
    cursor.execute('select * from mchitrcptmast order by Serial_No desc limit 1')
    details = cursor.fetchall()

    if(len(details) == 0):
        return 1
    else:
        return details[0][0] + 1

def lambda_handler(event,context):
    chit_key = event['queryStringParameters']['chit_key']
    amount = event['queryStringParameters']['amount']
    brnch_key = event['queryStringParameters']['brnch_key']
    today = time.strftime("%d/%m/%Y")
    installments_paid = 1
    txn_ref = 100    # a random number as of now
    serial_no = get_serial_no()
    ref_no = serial_no

    
    cursor = connection.cursor()
    query = 'select * from chitmast where Chit_Key = %s'
    cursor.execute(query,(chit_key,))
    details = cursor.fetchall()
    total_installments_paid = details[0][0]
    total_installments_paid += installments_paid

    query = 'update chitmast set Paid_No = %s where Chit_Key = %s'
    cursor.execute(query,(total_installments_paid,chit_key,))
    connection.commit()


    
    query  = 'insert into mchitrcptmast values(%s,%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query,(serial_no,ref_no,today,installments_paid,amount,chit_key,brnch_key,txn_ref ))
    connection.commit()

    

    response = "successful"

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject


