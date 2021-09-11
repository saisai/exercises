import cx_Oracle
print(cx_Oracle.version)  
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_9")
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\wan\Downloads\instantclient-basic-windows.x64-11.2.0.4.0\instantclient_11_2")
cx_Oracle.clientversion()  

connection = cx_Oracle.connect(
    user="demopython",
    password="demopython",
    dsn="localhost/orcl3")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()

# Create a table
'''
cursor.execute("""
    begin
        execute immediate 'drop table todoitem';
        exception when others then if sqlcode <> -942 then raise; end if;
    end;""")

cursor.execute("""
    create table todoitem (
        id number generated always as identity,
        description varchar2(4000),
        creation_ts timestamp with time zone default current_timestamp,
        done number(1,0),
        primary key (id))""")
        
        

# Insert some data

rows = [ ("Task 1", 0 ),
         ("Task 2", 0 ),
         ("Task 3", 1 ),
         ("Task 4", 0 ),
         ("Task 5", 1 ) ]

cursor.executemany("insert into todoitem (description, done) values(:1, :2)", rows)
print(cursor.rowcount, "Rows Inserted")

connection.commit()
'''
# Now query the rows back
#for row in cursor.execute('select description, done from todoitem'):
for row in cursor.execute('select description, done from todoitem'):
    if (row[1]):
        print(row[0], "is done")
    else:
        print(row[0], "is NOT done")
