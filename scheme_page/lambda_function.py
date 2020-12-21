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

""" given the date, the function adds x months to the date and returns the new date """
def add_x_month(date_time_str,x):
    date_time_str = date_time_str[:6] + date_time_str[8:]
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
    one_month = date_time_obj + relativedelta(months=+x)
    year = one_month.strftime("%Y")
    month = one_month.strftime("%m")
    day = one_month.strftime("%d")
    date_time = one_month.strftime("%d/%m/%Y")
    return date_time

""" given the cgrp_key, the function returns the name of the scheme"""
def get_scheme_name(cgrp_key):
    
    cursor = connection.cursor()
    query = 'select * from chitgroup where CGrp_Key = %s'
    cursor.execute(query,(cgrp_key))

    details = cursor.fetchall()
    return details[0][2]

""" a dummy debug function """
def print_data():
    cursor = connection.cursor()
    cursor.execute('select * from mchitrcptmast')
    details  = cursor.fetchall()
    for row in details:
        print(row)

""" given the cgrp_key, the function returns if the scheme is fixed or flexible """
def check_is_fixed_scheme(cgrp_key):
    cursor = connection.cursor()
    query = 'select Scheme_Key from chitgroup where CGrp_Key = %s'
    cursor.execute(query,(cgrp_key,))
    details = cursor.fetchall()
    if(details[0][0] <= 2):
        return  True
    else:
        return False

""" function inputs the chit_key and returns the details of the scheme """
def lambda_handler(event, context):

    chit_key = event['queryStringParameters']['chit_key']

    """ querying the chit_key """
    cursor = connection.cursor()
    query = 'select * from chitmast where Chit_Key = %s'
    cursor.execute(query,(chit_key,))
    details = cursor.fetchall()

    """ getting the details of the particular scheme """
    total_installments = details[0][7]
    installments_paid = details[0][10]
    amount = details[0][8]
    date_of_joining = details[0][6]
    scheme_name = get_scheme_name(details[0][1])
    due_date = add_x_month(date_of_joining,installments_paid + 1)
    due_month = "Due month " + str(int(installments_paid + 1))
    brnch_key = details[0][12]
    cgrp_key = details[0][1]
    is_fixed_scheme = check_is_fixed_scheme(cgrp_key)

    """ storing and returning the details """
    response = {}
    response['scheme_name']  =  scheme_name
    response['amount'] =   amount
    response['due_date'] =   due_date
    response['due_months'] =   due_month
    response['date_of_joining'] =   date_of_joining
    response['brnch_key'] =  brnch_key
    response['chit_key'] =   chit_key
    response['is_fixed_scheme']  = is_fixed_scheme

    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(response)

    
    return responseObject