import pandas
import numpy


def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Läs in alla tabeller från sidan
df_tables = pandas.read_html(url)

# Välj rätt tabell
df = df_tables[3]

# Byt kolumnrubriker till kolumnnummer
df.columns = range(df.shape[1])

# Behåll endast kolumn 0 och 2
df = df[[0, 2]]

# Behåll rader med index 1 till 10
df = df.iloc[1:11, :]

# Byt namn på kolumnerna
df.columns = ["Country", "GDP (Million USD)"]

# Skriv ut resultatet
print(df)

print("/////////////////////////////\n")
print("/////////////////////////////\n")



# ändra datatyp
df["GDP (Million USD)"] = df["GDP (Million USD)"].astype(int)

# konvertera million -> billion
df["GDP (Million USD)"] = df["GDP (Million USD)"] / 1000

# avrunda
df["GDP (Million USD)"] = numpy.round(df["GDP (Million USD)"], 2)

# byt namn på kolumn
df.rename(columns={"GDP (Million USD)": "GDP (Billion USD)"}, inplace=True)

print(df)

print("/////////////////////////////\n")
print("/////////////////////////////\n")

df.to_csv("Largest_economies.csv", index=False)