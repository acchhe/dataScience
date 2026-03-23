import sqlite3,csv
import pandas as pd
import prettytable


prettytable.DEFAULT = 'DEFAULT'


conn = sqlite3.connect("ChicagoData.db")
cursor = conn.cursor()

df = pd.read_csv("dataFileMap/ChicagoPublicSchools.csv")

df.to_sql("ChicagoPublicSchools", conn, if_exists="replace", index=False)

# Lista tabeller. Den hämtar namnen på alla tabeller i databasen
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

print("//////////////////n")

# Metadata om kolumner
columns = pd.read_sql("PRAGMA table_info(ChicagoPublicSchools);", conn)
print(columns)

print(f"number of columns in db-table: {len(columns)}")


query = """
SELECT COUNT(*) 
FROM ChicagoPublicSchools
WHERE "Elementary, Middle, or High School" = 'ES'
"""

result = pd.read_sql(query, conn)
print(f" number of elementary schools: {result}")



query = " select max(SAFETY_SCORE) from ChicagoPublicSchools"

result = pd.read_sql(query,conn)

print(f" highest safety score: {result}")


query = '''
SELECT NAME_OF_SCHOOL, SAFETY_SCORE
FROM ChicagoPublicSchools
WHERE SAFETY_SCORE = (
    SELECT MAX(SAFETY_SCORE)
    FROM ChicagoPublicSchools
)
'''

result = pd.read_sql(query,conn)

print(f" schools with highest safety-score: {result}")

#print(columns["name"].tolist())

query = ''' select NAME_OF_SCHOOL,AVERAGE_STUDENT_ATTENDANCE
from ChicagoPublicSchools
order by AVERAGE_STUDENT_ATTENDANCE desc 
limit 10
'''

result = pd.read_sql(query,conn)

print(f"Schools witht the highest student-attendance: {result}")

query = ''' select NAME_OF_SCHOOL,AVERAGE_STUDENT_ATTENDANCE
from ChicagoPublicSchools
order by AVERAGE_STUDENT_ATTENDANCE asc 
limit 5
'''
result = pd.read_sql(query,conn)

print(f"Schools witht the lowest student-attendance: {result}")

#Displaying the same dataset as above but without the '%' sign

query = ''' select NAME_OF_SCHOOL,replace(AVERAGE_STUDENT_ATTENDANCE,"%","")
from ChicagoPublicSchools
order by AVERAGE_STUDENT_ATTENDANCE asc 
limit 5
'''

result = pd.read_sql(query,conn)

print(f"Schools witht the lowest student-attendance: {result}")

query = ''' select NAME_OF_SCHOOL,AVERAGE_STUDENT_ATTENDANCE
from ChicagoPublicSchools
where cast(replace(AVERAGE_STUDENT_ATTENDANCE,"%","") as double) < 70
order by AVERAGE_STUDENT_ATTENDANCE asc

'''
result = pd.read_sql(query,conn)

print(f"Schools that have Average Student Attendance lower than 70%: {result}")
