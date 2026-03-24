import pandas as pd
import numpy as np
import sqlite3

# =========================================================
# 1. LÄS IN DATA
# =========================================================

# Läser in CSV-filen till en DataFrame
df = pd.read_csv("dirty_data_100.csv")

print("===== FÖRSTA 5 RADER =====")
print(df.head())

print("\n===== INFO OM DATA =====")
print(df.info())

print("\n===== ANTAL SAKNADE VÄRDEN PER KOLUMN =====")
print(df.isna().sum())


# =========================================================
# 2. KOLLA DUBLETTER
# =========================================================

# Räknar hur många exakta dubletter som finns. Kommer att få 0 eftersom alla rader har sin unika Primary-key
print("\n===== ANTAL EXAKTA DUBLETTER =====")
print(df.duplicated().sum())

# Räknar dubletter baserat på vissa kolumner exkluderat primary-key
# Vi ignorerar id eftersom id är unikt i filen
#subset i pandas används för att ange vilka kolumner som ska tas hänsyn till när en operation utförs, 
#till exempel när man tar bort dubletter eller saknade värden.
print("\n===== ANTAL DUBLETTER UTAN ID =====")
print(df.duplicated(subset=["name", "age", "city", "salary", "signup_date"]).sum())


# =========================================================
# 3. TA BORT DUBLETTER
# =========================================================

# Tar bort dubletter baserat på innehåll, inte id
#dropna() används för att hantera saknade värden (NaN). Den tar bort rader (eller kolumner) där det finns tomma värden.
#drop_duplicates() används istället för att ta bort dubbletter, alltså rader som innehåller samma data flera gånger. 
# Den behåller bara en version av varje unik rad.
df = df.drop_duplicates(subset=["name", "age", "city", "salary", "signup_date"])
print("\n===== EFTER ATT DUBLETTER TAGITS BORT =====")
print(df.shape)  # visar antal rader och kolumner


# =========================================================
# 4. HANTERA SAKNADE VÄRDEN (NaN)
# =========================================================

# Fyll saknade värden i age med medelvärdet
df["age"] = df["age"].fillna(df["age"].mean())

# Fyll saknade city med "Unknown"
df["city"] = df["city"].fillna("Unknown")

# Fyll saknade salary med medianen
df["salary"] = df["salary"].fillna(df["salary"].median())

# Fyll saknade datum med ett standardvärde
df["signup_date"] = df["signup_date"].fillna("2000-01-01")

print("\n===== SAKNADE VÄRDEN EFTER FYLLNING =====")
print(df.isna().sum())


# =========================================================
# 5. KONVERTERA DATATYPER
# =========================================================

# Säkerställer att age och salary är numeriska
# errors='coerce' betyder att felaktiga värden blir NaN
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Konverterar signup_date till riktigt datumformat
df["signup_date"] = pd.to_datetime(df["signup_date"], errors="coerce")

print("\n===== DATATYPER EFTER KONVERTERING =====")
print(df.dtypes)


# =========================================================
# 6. STÄDA TEXTKOLUMNER
# =========================================================

# Tar bort onödiga mellanslag före/efter text
df["name"] = df["name"].str.strip()
df["city"] = df["city"].str.strip()

# Standardiserar text så att första bokstaven blir stor
df["name"] = df["name"].str.title()
df["city"] = df["city"].str.title()

print("\n===== UNIKA STÄDER EFTER TEXTSTÄDNING =====")
print(df["city"].unique())


# =========================================================
# 7. HANTERA EVENTUELLA OUTLIERS
# =========================================================

# Exempel: behåll bara rimliga åldrar
df = df[(df["age"] >= 0) & (df["age"] <= 100)]

# Exempel: behåll bara rimliga löner
df = df[(df["salary"] >= 0) & (df["salary"] <= 100000)]

print("\n===== EFTER FILTRERING AV ORIMLIGA VÄRDEN =====")
print(df.describe())


# =========================================================
# 8. SKAPA NYA KOLUMNER
# =========================================================

# Skapar en ny kolumn med lön i tusental
df["salary_k"] = df["salary"] / 1000

# Skapar en ny kolumn med år från signup_date
df["signup_year"] = df["signup_date"].dt.year

print("\n===== DATA MED NYA KOLUMNER =====")
print(df.head())


# =========================================================
# 9. SORTERA DATA
# =========================================================

# Sorterar efter salary från högst till lägst
df = df.sort_values(by="salary", ascending=False)

print("\n===== SORTERAD DATA =====")
print(df.head())


# =========================================================
# 10. SPARA CLEANAD DATA TILL NY CSV
# =========================================================

df.to_csv("clean_data.csv", index=False)
print("\nCleanad CSV-fil skapad: clean_data.csv")


# =========================================================
# 11. SPARA CLEANAD DATA TILL SQLITE
# =========================================================

conn = sqlite3.connect("data_cleaning.db")

# Sparar den cleanade datan som en tabell i databasen
df.to_sql("clean_data", conn, if_exists="replace", index=False)

print("Cleanad data sparad i databasen som tabellen 'clean_data'")


# =========================================================
# 12. KONTROLLERA TABELLSTRUKTUREN I SQLITE
# =========================================================

table_info = pd.read_sql("PRAGMA table_info(clean_data);", conn)

print("\n===== TABELLSTRUKTUR I SQLITE =====")
print(table_info)


# =========================================================
# 13. EXEMPEL PÅ SQL-QUERIES FÖR ATT FÖRSTÅ DATAN
# =========================================================

# Hämtar de första 5 raderna från databasen
query1 = pd.read_sql("SELECT * FROM clean_data LIMIT 5;", conn)
print("\n===== FÖRSTA 5 RADERNA FRÅN SQLITE =====")
print(query1)

# Medelålder
query2 = pd.read_sql("SELECT AVG(age) AS average_age FROM clean_data;", conn)
print("\n===== MEDELÅLDER =====")
print(query2)

# Medellön per stad
query3 = pd.read_sql("""
SELECT city, AVG(salary) AS avg_salary
FROM clean_data
GROUP BY city;
""", conn)
print("\n===== MEDELLÖN PER STAD =====")
print(query3)

# Antal personer per stad
query4 = pd.read_sql("""
SELECT city, COUNT(*) AS antal_personer
FROM clean_data
GROUP BY city;
""", conn)
print("\n===== ANTAL PERSONER PER STAD =====")
print(query4)

#Dubbelkollar var filen finns
import os
print(os.path.abspath("data_cleaning.db"))

conn.close()
print("\nDatabasanslutning stängd.")
