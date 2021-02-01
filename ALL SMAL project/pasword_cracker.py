import pyodbc 
import numba
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = 'MRG_ROG' 
database = 'Mahnaz test' 
username = 'MRG_TEST'
p=2456767000
while True:
    p+=1
    print(p)
    password = p

    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ str(password))
        cursor = cnxn.cursor()
    except:
        pass
    else:
        print(p)
        break

