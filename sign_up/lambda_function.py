import pymysql
import json
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def lambda_handler(event, context):
    phone = event['queryStringParameters']['Phone']
    password = event['queryStringParameters']['passwd']
    username = event['queryStringParameters']['username']
    confirm_password = event['queryStringParameters']['confirm']
    email = event['queryStringParameters']['email']
    branch = event['queryStringParameters']['branch']
    otp = event['queryStringParameters']['otp']
    cursor = connection.cursor()
    
    
    response = ""
    

    if(confirm_password != password):
        response = "passwords do not match"
    else:
        query = 'select * from chitmast where Phone_No  = %s'
        cursor.execute(query,(phone, ))
        details = cursor.fetchall()
        if(len(details) == 0):
            response = "user does not exist"
        else:
            for row in details:
                user_key = '10'
                brnch_key = row[12]
                query = 'insert into onlineusers values (%s,%s,%s,%s,%s)'
                cursor.execute(query,(user_key,username,password,phone,brnch_key, ))
        cursor.execute('select * from onlineusers')
        details  = cursor.fetchall()
        for row in details:
            print(row)
        response = "data updated"
        
    



    


    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject