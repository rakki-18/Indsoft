import pymysql
import json
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)
""" function inputs the username and password and checks if it is a valid credential"""
def lambda_handler(event, context):
    username = event['queryStringParameters']['username']
    password = event['queryStringParameters']['passwd']
    
    cursor = connection.cursor()
    query = 'select User_password from onlineusers where User_name = %s'
    cursor.execute(query,(username, ))
    details = cursor.fetchall()
    

    if(len(details) == 0):                             # if username is not present in the database
        response = "username doesn't exist"
    elif(details[0][0] != password):                  #if the corresponding password to the username is different 
        response = "wrong password"
    else:                                             # given credentials are correct
        response = "logged in"

   
    """ debug message """
    cursor.execute('select * from onlineusers')
    details  = cursor.fetchall()
    for row in details:
        print(row)

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject
