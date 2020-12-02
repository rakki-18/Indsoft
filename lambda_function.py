# Configuration
import pymysql
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'


# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

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
    
    
    

    return {
        'name': details[0][3],
        'branch': branch_dict[details[0][12]],
        'scheme' : scheme_dict[details[0][1]],
        'amount' : details[0][8]
    }

