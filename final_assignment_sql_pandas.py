import pandas as pd
import sqlite3
import csv

conn = sqlite3.Connection("finaldB.db")

df_census = pd.read_csv("dataFileMap/ChicagoCensusData.csv")
df_pbSchools = pd.read_csv("dataFileMap/ChicagoPublicSchools.csv")
df_crime = pd.read_csv("dataFileMap/ChicagoCrimeData.csv")

# Ladda in dataframes till SQLite-tabeller
df_census.to_sql("CENSUS_DATA", conn, if_exists="replace", index=False)
df_pbSchools.to_sql("CHICAGO_PUBLIC_SCHOOLS", conn, if_exists="replace", index=False)
df_crime.to_sql("CHICAGO_CRIME_DATA", conn, if_exists="replace", index=False)

print("CSV-filerna har laddats in i finaldB.db")


#displaying meta-data about the crime-table
columns = pd.read_sql("PRAGMA table_info(CHICAGO_CRIME_DATA);", conn)
print(columns)

query = ''' select count(*) as tot_number_of_crimes
from CHICAGO_CRIME_DATA
'''

result = pd.read_sql(query,conn)

print(result)


query = ''' select COMMUNITY_AREA_NUMBER,COMMUNITY_AREA_NAME
from CENSUS_DATA
where PER_CAPITA_INCOME < 11000

'''

result = pd.read_sql(query,conn)

print(result)



query = """
SELECT CASE_NUMBER
FROM CHICAGO_CRIME_DATA
WHERE DESCRIPTION LIKE '%MINOR%';
"""

result = pd.read_sql(query, conn)

print(result)

query = """
SELECT *
FROM CHICAGO_CRIME_DATA
WHERE PRIMARY_TYPE = 'KIDNAPPING'
AND DESCRIPTION LIKE '%CHILD%';
"""

result = pd.read_sql(query, conn)

print(result)


query = """
SELECT DISTINCT PRIMARY_TYPE
FROM CHICAGO_CRIME_DATA
WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%';
"""

result = pd.read_sql(query, conn)

print(result)


query = '''
select"select Elementary, Middle, or High School" as school_type,
       AVG(SAFETY_SCORE) AS avg_safety_score
FROM CHICAGO_PUBLIC_SCHOOLS
GROUP BY "Elementary, Middle, or High School";
'''

result = pd.read_sql(query, conn)

print(result)
