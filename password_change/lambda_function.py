import pymysql
import json
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

""" function inputs the username, old password, new and confirmed passwords and changes the password in the database"""
def lambda_handler(event, context):
    old_password = event['queryStringParameters']['old']
    new_password = event['queryStringParameters']['new']
    confirm_password = event['queryStringParameters']['con']
    username = event['queryStringParameters']['username']

    """
    querying the given username in the database
    """
    cursor = connection.cursor()
    query = 'select User_password from onlineusers where User_name = %s'
    cursor.execute(query,(username, ))
    details = cursor.fetchall()
   
    if(old_password != details[0][0]):                      # given old password is wrong
     response = "wrong password"
    elif(new_password != confirm_password):                 # new password and the confirm password do not match
     response = "passwords don't match"
    else:                                                   # update the password in the database
        response = "password updated"
        query = 'update onlineusers set User_password = %s where User_name = %s'
        cursor.execute(query,(new_password,username, ))
        connection.commit()

    
    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject