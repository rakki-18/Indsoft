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
    query  = 'insert into mchitrcptmast values(%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(query,(serial_no,ref_no,today,installments_paid,amount,chit_key,brnch_key, ))
    connection.commit()

    

    response = "successful"

    return response


