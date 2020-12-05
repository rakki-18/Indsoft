# Configuration
import pymysql
endpoint = 'database-1.c1reo38y2ygs.ap-south-1.rds.amazonaws.com'
username = 'admin'
password = 'silent123'
database_name = 'mygssjms'

# Connection
connection = pymysql.connect(endpoint, user = username, passwd = password, db = database_name)

def lambda_handler(event, context):

    """ 
    Create Operation
    """
    cursor = connection.cursor()
    cursor.execute('insert into branchmast(BRNCH_KEY,BRNCH_NAME) values (20.0,test_branch_name)')
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0],row[1],row[2]))



