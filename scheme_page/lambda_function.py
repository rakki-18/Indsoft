import pymysql
import json
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def add_x_month(date_time_str,x):
    date_time_str = date_time_str[:6] + date_time_str[8:]
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
    one_month = date_time_obj + relativedelta(months=+x)
    year = one_month.strftime("%Y")
    month = one_month.strftime("%m")
    day = one_month.strftime("%d")
    date_time = one_month.strftime("%d/%m/%Y")
    return date_time

def get_scheme_name(cgrp_key):
    
    cursor = connection.cursor()
    query = 'select * from chitgroup where CGrp_Key = %s'
    cursor.execute(query,(cgrp_key))

    details = cursor.fetchall()
    return details[0][2]

def print_data():
    cursor = connection.cursor()
    cursor.execute('select * from chitmast')
    details = cursor.fetchall()
    for row in details:
        print(row)
    
def lambda_handler(event, context):

    chit_key = '388'

    cursor = connection.cursor()
    query = 'select * from chitmast where Chit_Key = %s'
    cursor.execute(query,(chit_key,))
    details = cursor.fetchall()

    total_installments = details[0][7]
    installments_paid = details[0][10]
    amount = details[0][8]
    date_of_joining = details[0][6]
    scheme_name = get_scheme_name(details[0][1])

    payments_to_be_made = []
    for i in range(int(total_installments - installments_paid)):
        payments_to_be_made.append(add_x_month(date_of_joining,installments_paid + i + 1))
    

    response = {}
    response['scheme_name'] = scheme_name
    response['amount'] = amount
    response['installments_left'] = total_installments - installments_paid
    response['due_months'] = payments_to_be_made

    print_data()


    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    return responseObject