import pymysql
import json
import time

endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'


# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

""" function returns the last serial number in the mchitrcptmast table """
def get_serial_no():
    cursor = connection.cursor()
    cursor.execute('select * from mchitrcptmast order by Serial_No desc limit 1')
    details = cursor.fetchall()

    if(len(details) == 0):
        return 1
    else:
        return details[0][0] + 1

""" function updates the database when the user pays the scheme amount """
def lambda_handler(event,context):
   
    """
    getting the details of the user who paid the scheme
    """
    chit_key = event['queryStringParameters']['chit_key']
    amount = event['queryStringParameters']['amount']
    brnch_key = event['queryStringParameters']['brnch_key']
    today = time.strftime("%d/%m/%Y")
    installments_paid = 1
    txn_ref = 100    # a random number as of now
    serial_no = get_serial_no()
    ref_no = serial_no

    """ 
    querying the chit_key
    """
    cursor = connection.cursor()
    query = 'select * from chitmast where Chit_Key = %s'
    cursor.execute(query,(chit_key,))
    details = cursor.fetchall()
    total_installments_paid = details[0][0]
    total_installments_paid += installments_paid

    """ 
    updating the installments paid in chit_key table
    """
    query = 'update chitmast set Paid_No = %s where Chit_Key = %s'
    cursor.execute(query,(total_installments_paid,chit_key,))
    connection.commit()


    """
    storing the details of the payment in mchitrcptmast table
    """
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


