import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
#server = 'tcp:myserver.database.windows.net' 
server = 'localhost' 
database = 'db' 
username = 'username' 
password = 'root' 
SERVER = '{server},{port}'.format(server='localhost', port=1433)
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
result = cursor.execute("SELECT @@VERSION")
result.fetchone()


# https://stackoverflow.com/questions/25505081/python-pyodbc-how-to-connect-to-a-specific-instance
# https://pypi.org/project/django-mssql-backend/
# https://stackoverflow.com/questions/72477477/python-error-column-names-in-each-table-must-be-unique-how-to-solve
# https://stackoverflow.com/questions/32770942/how-to-use-django-with-sql-server
# https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/

# https://github.com/mkleehammer/pyodbc/issues/971
import pyodbc

print(pyodbc.drivers())