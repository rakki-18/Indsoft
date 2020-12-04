import pymysql
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def lambda_handler(event, context):
    cursor = connection.cursor()
    cursor.execute('insert into onlineusers values (1.0,"test_name","test_password","9999999999",1.0)')
    cursor.execute('select * from onlineusers')
    details = cursor.fetchall()
    for row in details:
        print(row)
    