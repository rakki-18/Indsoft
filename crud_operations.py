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
    """ 
    Create Operation
    """
    print("create operation")
    cursor.execute('insert into branchmast(BRNCH_KEY,BRNCH_NAME) values (22.0,"test_branch_name")')
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1}".format(row[0],row[1]))
        
    """
    Read Operation
    """
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1}".format(row[0],row[1]))
    
    """
    Update Operation
    """
    print("update operation")
    cursor.execute('update branchmast set BRNCH_NAME = "test_branch_name" where BRNCH_KEY = 2.0')
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} ".format(row[0],row[1]))

    """
    Delete Operation
    """
    print("delete operation")
    cursor.execute('delete from branchmast where BRNCH_KEY = 1.0')
    cursor.execute('select * from branchmast')
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} ".format(row[0],row[1]))
    
    response = "success"
    return response

