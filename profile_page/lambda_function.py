# Configuration
import pymysql
import json
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'


# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

""" given a date, the function adds x months to the date and returns the new date"""
def add_x_month(date_time_str,x):
    date_time_str = date_time_str[:6] + date_time_str[8:]
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
    one_month = date_time_obj + relativedelta(months=+x)
    year = one_month.strftime("%Y")
    month = one_month.strftime("%m")
    day = one_month.strftime("%d")
    date_time = one_month.strftime("%d/%m/%Y")
    return date_time

""" given the username, the function returns the phone no: of the user """
def get_phone_no(username):
    cursor = connection.cursor()
    query = 'select Phone_No from onlineusers where User_name = %s'
    cursor.execute(query,(username,))
    details = cursor.fetchall()
    print(len(details))

    return details[0][0]

""" function inputs the username and returns all the details of the scheme registered under the username """
def lambda_handler(event, context):

    """ find the Phone_No from the username """
    username = event['queryStringParameters']['username']
    Phone_No = get_phone_no(username)

    cursor = connection.cursor()

    """ a dictionary that maps branch_key to branch name """
    branch_dict = {}
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()
    for row in rows:
        branch_dict[row[0]] = row[1]
    
    """ a dictionary that maps scheme_key to scheme name """
    scheme_dict = {}
    cursor.execute('select * from chitgroup')
    rows = cursor.fetchall()
    for row in rows:
        scheme_dict[row[0]] = row[2]

    """ qeuerying the Phone_No to the database """
    query = 'select * from chitmast where Phone_No = %s'
    cursor.execute(query, (Phone_No, ))
    details = cursor.fetchall()
    
    length = len(details)
    name = []
    branch = []
    scheme = []
    amount = []
    date = []
    chit_key = []
    
    """ storing the  branch name, scheme name, amount , date of each scheme into a list """
    for i in range(length):
        name.append(details[i][3])
        branch.append(branch_dict[details[i][12]])
        scheme.append(scheme_dict[details[i][1]])
        amount.append(details[i][8])
        chit_key.append(details[i][0])
        date.append(add_x_month(details[i][6],1))
     
    response = {}
    
    """ returning the details of each scheme """
    response['name'] = name
    response['branch'] = branch
    response['scheme'] = scheme
    response['amount'] = amount
    response['chit_key'] = chit_key
    response['date'] = date

    
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject

