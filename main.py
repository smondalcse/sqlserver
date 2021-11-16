import pyodbc
import pandas as pd

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ITDEV22;'
                      'Database=NMLCustomerInfo;'
                      'Trusted_connection=yes;')

cursor = conn.cursor()

#   How to execute the line query in python
# cursor.execute('select * from tblUsers')
# for row in cursor:
#     print(row)

#   How to execute the store procedure in python
sp = 'EXEC sp_getAllUsers @EmpID = {0}, @IsActive = {1}'.format('null', 0)
result = pd.read_sql_query(sp, conn)
print(result)

result.to_csv("Users.csv", index=False)
conn.close()

