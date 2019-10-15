# psycopg2 needs to be installed 
from getpass import getpass
import psycopg2


def connect(connInfo):
    conn = None
    connString = 'host={} port={}dbname={} user={} password={}'.format(connInfo[0], connInfo[1], connInfo[2], connInfo[3], connInfo[4])
    try:
        conn = psycopg2.connect(connString)
        dbCursor = conn.cursor()
        dbCursor.execute('SELECT version()')
        print(dbCursor.fetchone())
        
        # Single class add test
        # sqlAddClass = "INSERT INTO classes (class_id, description) VALUES (\'ACCT 102\', \'Practical Accounting I\');"
        
        # Multi class add test
        sqlAddClass = "INSERT INTO classes (class_id, description) VALUES "
        args = [("TST 1", "Test Class I"), ("TST 2", "Test Class II")]
        sql_args = ','.join(dbCursor.mogrify("(%s, %s)", x).decode("utf-8") for x in args)
        dbCursor.execute(sqlAddClass + sql_args)
        conn.commit()
        dbCursor.close()
        conn.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Connection closed')

('ACCT 101', 'Practical Accounting I')
def getConnectionInfo():
    # List of default values
    host = 'localhost'
    port = 5432
    database = 'postgres'
    username = 'postgres'
    password = 'password'

    # get the DB connection info 
    print('Input connection info [default value]:')
    inputHost = input('Hostname [{}]: '.format(host)).strip()
    inputPort = input('Port [{}]: '.format(port))
    inputDB = input('Database [{}]: '.format(database))
    inputUser = input('Username [{}]: '.format(username))
    inputPass = getpass(prompt='Password [{}]: '.format(password), stream=None)
    
    # check for changes
    if len(inputHost) > 0:
        host = inputHost
    if len(inputPort) > 0:
        port = inputPort
    if len(inputDB) > 0:
        database = inputDB
    if len(inputUser) > 0:
        username = inputUser
    if len(inputPass) > 0:
        password = inputPass
    
    return [host, port, database, username, password]


connInfo = getConnectionInfo()
connect(connInfo)

