# Configuration
import pymysql
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'


# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def add_one_month(date_time_str):
    date_time_str = date_time_str[:6] + date_time_str[8:]
    date_time_obj = datetime.strptime(date_time_str, '%d/%m/%y')
    one_month = date_time_obj + relativedelta(months=+1)
    year = one_month.strftime("%Y")
    month = one_month.strftime("%m")
    day = one_month.strftime("%d")
    date_time = one_month.strftime("%d/%m/%Y")
    return date_time
def lambda_handler(event, context):

    
    cursor = connection.cursor()

    branch_dict = {}
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()
    for row in rows:
        branch_dict[row[0]] = row[1]
    
    scheme_dict = {}
    cursor.execute('select * from chitgroup')
    rows = cursor.fetchall()
    for row in rows:
        scheme_dict[row[0]] = row[2]
    cursor.execute('select * from chitmast where Phone_No = "9916490232"')
    details = cursor.fetchall()
    
    length = len(details)
    name = []
    branch = []
    scheme = []
    amount = []
    date = []
    
    for i in range(length):
        name.append(details[i][3])
        branch.append(branch_dict[details[i][12]])
        scheme.append(scheme_dict[details[i][1]])
        amount.append(details[i][8])
        
        date.append(add_one_month(details[i][6]))


    
    
    

    return {
        'name': name,
        'branch': branch,
        'scheme' : scheme,
        'amount' : amount,
        'date' : date
    }

