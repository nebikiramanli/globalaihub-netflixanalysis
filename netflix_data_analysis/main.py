import numpy as np
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pip import main
from csv import reader


# TODO : Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur?

filen = "C:/Users/hakan/OneDrive/Belgeler/globalAiHub/globalaihub-netflix/globalaihub-netflixanalysis/NetflixOriginals.csv"
data = pd.read_csv(filen, encoding = "ISO-8859-1")
#data.head()
sorted = data.sort_values(by = "Runtime")
last = sorted.tail(1)
print(f"En uzun soluklu film: {last.iloc[0]['Language']} dilindedir. Adı: {last.iloc[0]['Title']}")
sorted["Runtime"].value_counts()

# TODO 2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde
#  çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz
list_1 = []
months = ["January","February","March","April","May","June","July",
"August","September","October","November","December"]
sub_months = ["January","February","March","April","May","June"]
with open(filen, "r", encoding="ISO-8859-1") as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row_ in csv_reader:
        # row variable is a list that represents a row in csv
        for j in row_:
            sub_row_2 = row_[2].split()
            if "Documentary" in row_:
                if "2019" in j:
                    if sub_row_2[0] in months:
                        list_1.append(row_)
                if "2020" in j:
                    if sub_row_2[0] in sub_months:
                        list_1.append(row_)

df = pd.DataFrame (list_1, columns = ["Title","Genre","Premiere","Runtime","IMDB Score","Language"])
df.to_excel("df.xlsx")
#hello = pd.DataFrame.from_records(list_1[1:],columns=list_1[0])
#print(hello)
#print(sorted[sorted["Premiere"] == 2021])

# TODO İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?

sorted_imdb = data[data["Language"] == "English"].sort_values(by = "IMDB")

print(sorted_imdb.head())
# TODO 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?

# TODO 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.

# TODO Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.

# TODO IMDB puanı en yüksek olan ilk 10 film hangileridir?
# TODO IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
# TODO IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
# TODO 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
# TODO Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
# TODO Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
# TODO Hangi yılın toplam "runtime" süresi en fazladır?
# TODO Her bir dilin en fazla kullanıldığı "Genre" nedir?
# TODO Veri setinde outlier veri var mıdır? Açıklayınız.




