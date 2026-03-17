Funktionen
def make_graph(stock_data, revenue_data, stock):

Det här definierar en funktion med namnet make_graph.

Den tar emot tre parametrar:

stock_data → en DataFrame med aktiedata, till exempel datum och stängningspris

revenue_data → en DataFrame med omsättningsdata

stock → ett textvärde, till exempel "Tesla" eller "GameStop", som används i rubrikerna

Syftet med funktionen är att rita två grafer:

historiskt aktiepris

historisk omsättning

1. Filtrera aktiedata
stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']

Här skapas en ny variabel: stock_data_specific.

Vad som händer:

stock_data.Date <= '2021-06-14' jämför varje rad i kolumnen Date

bara de rader där datumet är mindre än eller lika med 2021-06-14 behålls

resultatet blir en filtrerad version av stock_data

Varför gör man detta?

För att begränsa grafen till en viss tidsperiod. Då visas inte data efter det datumet.

2. Filtrera revenue-data
revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

Här görs exakt samma typ av filtrering, men för omsättningsdatan.

endast rader med datum upp till och med 2021-04-30 sparas

den filtrerade datan läggs i revenue_data_specific

Anledningen är återigen att man vill visa data fram till ett bestämt datum.

3. Skapa figur och två delgrafer
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

Den här raden skapar själva ritområdet för graferna med hjälp av Matplotlib.

Vad betyder delarna?

plt.subplots(...) skapar en figur med en eller flera delgrafer

2, 1 betyder:

2 rader

1 kolumn

alltså två grafer ovanpå varandra

Variablerna:

fig → hela figuren

axes → en lista/array med de två axelobjekten:

axes[0] = övre grafen

axes[1] = nedre grafen

Övriga argument:

figsize=(12, 8) → figurens storlek blir 12 tum bred och 8 tum hög

sharex=True → båda graferna delar samma x-axel, alltså datumaxeln

Det gör att graferna blir lättare att jämföra.

Kommentar: Aktiepris
# Aktiepris

Detta är bara en kommentar för läsbarhet. Den påverkar inte programmet.

4. Rita första grafen: aktiepris
axes[0].plot(pd.to_datetime(stock_data_specific.Date),
             stock_data_specific.Close.astype("float"),
             label="Share Price",
             color="blue")

Den här delen ritar linjen i den övre grafen.

Del för del:
axes[0].plot(...)

använder den första delgrafen, alltså den översta

plot(...) ritar en linjegraf

pd.to_datetime(stock_data_specific.Date)

tar kolumnen Date

omvandlar den till ett datumformat som Matplotlib kan förstå ordentligt

viktigt eftersom datum annars ibland behandlas som text

stock_data_specific.Close.astype("float")

tar kolumnen Close, alltså stängningspriset för aktien

astype("float") omvandlar värdena till decimaltal (float)

detta säkerställer att värdena går att plotta numeriskt

label="Share Price"

anger etiketten för linjen

används om man senare skulle vilja visa en legend

color="blue"

gör linjen blå

Sammanfattning:
Den här raden ritar aktiens historiska stängningspris över tid.

5. Sätt y-axelns etikett för första grafen
axes[0].set_ylabel("Price ($US)")

Den här raden sätter texten på y-axeln i den översta grafen.

set_ylabel(...) betyder “sätt etikett på y-axeln”

"Price ($US)" berättar att värdena representerar pris i amerikanska dollar

6. Sätt rubrik för första grafen
axes[0].set_title(f"{stock} - Historical Share Price")

Här sätts titeln för den första grafen.

Viktigt:

f"..." är en f-string

{stock} ersätts med värdet som skickades in till funktionen

Exempel:

om stock = "Tesla" blir titeln:
"Tesla - Historical Share Price"

Det gör funktionen återanvändbar för olika företag.

Kommentar: Revenue
# Revenue

Detta är bara en kommentar som markerar att nästa block handlar om omsättning.

7. Rita andra grafen: omsättning
axes[1].plot(pd.to_datetime(revenue_data_specific.Date),
             revenue_data_specific.Revenue.astype("float"),
             label="Revenue",
             color="green")

Den här raden ritar den nedre grafen.

Del för del:
axes[1].plot(...)

använder andra delgrafen, alltså den nedersta

pd.to_datetime(revenue_data_specific.Date)

omvandlar Date-kolumnen till datumformat

revenue_data_specific.Revenue.astype("float")

tar kolumnen Revenue

omvandlar den till float

Detta är viktigt eftersom revenue ofta kommer in som text efter webbskrapning.
Exempel: "31536" måste vara ett numeriskt värde för att kunna ritas som graf.

label="Revenue"

sätter etiketten till "Revenue"

color="green"

gör linjen grön

Sammanfattning:
Den här raden ritar företagets historiska omsättning över tid.

8. Sätt y-axelns etikett för andra grafen
axes[1].set_ylabel("Revenue ($US Millions)")

Den här raden sätter etiketten på y-axeln för den nedre grafen.

Texten visar att värdena är omsättning i miljoner amerikanska dollar.

9. Sätt x-axelns etikett
axes[1].set_xlabel("Date")

Här sätts etiketten på x-axeln för den nedersta grafen.

Eftersom båda graferna delar x-axel (sharex=True) räcker det ofta att sätta etiketten längst ner.

"Date" visar att x-axeln innehåller datum.

10. Sätt rubrik för andra grafen
axes[1].set_title(f"{stock} - Historical Revenue")

Här sätts rubriken för den andra grafen.

Exempel:

om stock = "GameStop" blir titeln:
"GameStop - Historical Revenue"

Även här används f-string så att samma funktion kan användas för flera företag.

11. Justera layout automatiskt
plt.tight_layout()

Den här raden gör att Matplotlib automatiskt försöker justera avståndet mellan grafer, rubriker och etiketter.

Varför behövs det?

Utan tight_layout() kan:

texter överlappa varandra

rubriker hamna för nära

etiketter klippas av

Så denna rad förbättrar utseendet.

12. Visa graferna
plt.show()

Detta visar den färdiga figuren på skärmen.

Utan denna rad kan grafen ibland inte visas alls, särskilt i vanliga Python-skript.

Kort sammanfattning av hela funktionen

Funktionen make_graph:

tar emot aktiedata och omsättningsdata

filtrerar bort datum efter vissa gränser

skapar två grafer ovanpå varandra

ritar aktiepris i den översta grafen

ritar revenue i den nedersta grafen

lägger till rubriker och axeltexter

visar resultatet
