import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


# Funktionen är redan given i uppgiften
def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Aktiepris
    axes[0].plot(pd.to_datetime(stock_data_specific.Date),
                 stock_data_specific.Close.astype("float"),
                 label="Share Price",
                 color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date),
                 revenue_data_specific.Revenue.astype("float"),
                 label="Revenue",
                 color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()


# -----------------------------
# Question 1: Tesla stock data
# -----------------------------
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

print("Tesla stock data:")
print(tesla_data.head())


# --------------------------------------
# Question 2: Tesla revenue web scraping
# --------------------------------------
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text

soup = BeautifulSoup(html_data, "html.parser")

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# Tesla-tabellen är första relevanta tabellen
for row in soup.find_all("tbody")[0].find_all("tr"):
    col = row.find_all("td")
    if len(col) >= 2:
        date = col[0].text
        revenue = col[1].text

        tesla_revenue = pd.concat(
            [tesla_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})],
            ignore_index=True
        )

# Rensa Revenue-kolumnen
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace("$", "", regex=False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.replace(",", "", regex=False)
tesla_revenue["Revenue"] = tesla_revenue["Revenue"].str.strip()

# Ta bort tomma rader och null
tesla_revenue = tesla_revenue[tesla_revenue["Revenue"] != ""]
tesla_revenue = tesla_revenue.dropna()

print("\nTesla revenue data:")
print(tesla_revenue.tail())


# --------------------------------
# Question 3: GameStop stock data
# --------------------------------
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)

print("\nGameStop stock data:")
print(gme_data.head())


# -----------------------------------------
# Question 4: GameStop revenue web scraping
# -----------------------------------------
gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])

# GameStop-tabellen är andra relevanta tabellen
for row in soup.find_all("tbody")[1].find_all("tr"):
    col = row.find_all("td")
    if len(col) >= 2:
        date = col[0].text
        revenue = col[1].text

        gme_revenue = pd.concat(
            [gme_revenue, pd.DataFrame({"Date": [date], "Revenue": [revenue]})],
            ignore_index=True
        )

# Rensa Revenue-kolumnen
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace("$", "", regex=False)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.replace(",", "", regex=False)
gme_revenue["Revenue"] = gme_revenue["Revenue"].str.strip()

# Ta bort tomma rader och null
gme_revenue = gme_revenue[gme_revenue["Revenue"] != ""]
gme_revenue = gme_revenue.dropna()

print("\nGameStop revenue data:")
print(gme_revenue.tail())


# -----------------------------
# Question 5: Tesla stock graph
# -----------------------------
make_graph(tesla_data, tesla_revenue, "Tesla")


# --------------------------------
# Question 6: GameStop stock graph
# --------------------------------
make_graph(gme_data, gme_revenue, "GameStop")
