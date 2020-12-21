import pymysql
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

""" a dummy function """
def lambda_handler(event, context):
    cursor = connection.cursor()
    
    cursor.execute('select * from onlineusers')
    details = cursor.fetchall()
    for row in details:
        print(row)
    