import sqlite3
import pandas as pd

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')


# cursor object
cursor_obj = conn.cursor()


# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")


# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
 
cursor_obj.execute(table)
 
print("Table is Ready")




#insert some rows of data into the table.
#The INSTRUCTOR table we created in the previous step contains 3 rows of data
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')


#single query to insert the remaining two rows of data
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


#Retrieving data that was previously inserted into table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)
  
  
  
## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)
  
  

# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)
  
  
  

#statement that changes the Rav's CITY to MOOSETOWN
query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)



statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)
  
  
  
# retrieve the contents of the INSTRUCTOR table into a Pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

#print the dataframe
print(df)

#printing the name only for the first row in the DataFrame
df.LNAME[0]


#use the shape method to see how many rows and columns are in the dataframe
print(df.shape)

#Makes changes made permanent and saves them in the db
conn.commit()

##close connections so that we can avoid unused connections taking up resources.
conn.close()
