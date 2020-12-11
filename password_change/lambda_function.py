import pymysql
import json
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)
username = 'test_password'
def lambda_handler(event, context):
    old_password = event['queryStringParameters']['old']
    new_password = event['queryStringParameters']['new']
    confirm_password = event['queryStringParameters']['con']

    cursor = connection.cursor()
   
    query = 'select User_password from onlineusers where User_name = %s'
    cursor.execute(query,(username, ))
    details = cursor.fetchall()
   
    if(old_password != details[0][0]):
     response = 1
    elif(new_password != confirm_password):
     response = 2
    else:
        response = 3
        query = 'update onlineusers set User_password = %s where User_name = %s'
        cursor.execute(query,(new_password,username, ))
        connection.commit()
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject