import seaborn as sns
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#läser in csv-filens data till vårt DataFrame-obj
url = "dataFileMap/jcxq-k9xf.csv"
df = pd.read_csv(url)

print("csv-datan:")
print(df.head())

# Steg 2: Skapa SQLite-databas och spara tabell
conn = sqlite3.connect("socioeconomic.db")

df.to_sql("ChicagoSocioEconomicData", conn, if_exists="replace", index=False)

print("\nDatabas skapad!")

# Steg 3: Kör SQL-query
result = pd.read_sql("SELECT * FROM ChicagoSocioEconomicData", conn)

print("\nData från SQL:")
print(result)


#antal rader och kolumner
print("rader och kolumner:")
print(result.shape)

cursor = conn.cursor()

cursor.execute('''select count(community_area_name) as count
               from ChicagoSocioEconomicData
               where hardship_index > 50.0
        
               ''')


result = cursor.fetchone()


#areas with hardship_index over 50.0
print("areas with hardship_index over 50.0")
print(result[0])

#Alternativt lösa det med pandas:
#df = pd.read_sql("""
#SELECT COUNT(*) as count
#FROM ChicagoSocioEconomicData
#WHERE hardship_index > 50.0
#""", conn)

#print(df)


#Retrieving the value with highest hardship_index in the dataset

cursor.execute('''select max(hardship_index)
               from ChicagoSocioEconomicData
               ''')

result = cursor.fetchone()
print("highest hardship_index-value in the dataset:")
print(result[0])

#Retrieving community-area with highest hardship_index in the dataset

cursor.execute('''select community_area_name
           from ChicagoSocioEconomicData
           where hardship_index = (
               select max(hardship_index)
               from ChicagoSocioEconomicData
           )
               ''')

result = cursor.fetchone()
print("community-area with the highest hardship_index-value in the dataset:")
print(result[0])


cursor.execute("SELECT community_area_name FROM ChicagoSocioEconomicData WHERE per_capita_income_ > 60000;")
result = cursor.fetchall()
print("Chicago community areas that have per-capita incomes greater than $60,000:")
for value in result:
   print(value[0])

df = pd.read_sql("""
SELECT per_capita_income_, hardship_index 
FROM ChicagoSocioEconomicData
""", conn)

conn.close()

# Skapa scatter plot
plt.scatter(df['per_capita_income_'], df['hardship_index'])
plt.xlabel("Per Capita Income")
plt.ylabel("Hardship Index")
plt.title("Income vs Hardship Index")

#There is a clear negative correlation between income and hardship. Areas with lower income tend to experience higher levels of hardship.

plt.show()
