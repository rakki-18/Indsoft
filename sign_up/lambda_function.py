import pymysql
import json
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def get_user_key():
    cursor = connection.cursor()
    cursor.execute('select * from onlineusers order by User_key desc limit 1')
    details = cursor.fetchall()

    if(len(details) == 0):
        return 1
    else:
        return details[0][0] + 1

def check_already_present(phone):
    query = 'select * from onlineusers where Phone_No = %s'
    cursor = connection.cursor()
    cursor.execute(query,(phone, ))
    details = cursor.fetchall()
    if(len(details) == 0):
        return False
    else:
        return True

def username_exists(username):
    query = 'select * from onlineusers where User_name = %s'
    cursor = connection.cursor()
    cursor.execute(query,(username,))
    details = cursor.fetchall()
    if(len(details) == 0):
        return False
    else:
        return True

""" given the details the user entered while signing up, the function checks the validity and then updates the database """  
def lambda_handler(event, context):
    """ getting all the information that the user entered """
    phone = event['queryStringParameters']['Phone']
    password = event['queryStringParameters']['passwd']
    username = event['queryStringParameters']['username']
    confirm_password = event['queryStringParameters']['confirm']
    email = event['queryStringParameters']['email']
    branch = event['queryStringParameters']['branch']
    otp = event['queryStringParameters']['otp']
    cursor = connection.cursor()
    
    
    response = ""
    

    if(confirm_password != password):                              # if the password and confirmed password do not match
        response = "passwords do not match"
    else:  
        """ querying the phone no: to the database """                                                        
        query = 'select * from chitmast where Phone_No  = %s'
        cursor.execute(query,(phone, ))
        details = cursor.fetchall()

        if(len(details) == 0):                                     # if the phone no: has not been registered in any scheme
            response = "phone number not signed up for any scheme"
        else:
            
            if(username_exists(username) == True):                  # if the given username already exists
                response = "username exists"
            else:
                user_key = get_user_key()
                brnch_key = details[0][12]
                if(check_already_present(phone) == False):          # if the phone no: has already been signed up
                    
                    """ updating the database """
                    query = 'insert into onlineusers values (%s,%s,%s,%s,%s)'
                    cursor.execute(query,(user_key,username,password,phone,brnch_key, ))
                    connection.commit()
                    response = "data updated"
                else:
                    response = "user has already signed up"
    
    
    """ debug message """
    cursor.execute('select * from onlineusers')
    details  = cursor.fetchall()
    for row in details:
        print(row)
        
        
    



    
    """ returning the output """

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject