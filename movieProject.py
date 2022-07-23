import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math 
import sys
import locale

import chardet


#1 kısım baş (uzun soluklu filmler hangi dilde oluşturulmuştur)

# Creating autocpt arguments
def func(pct, data):
    absolute = int(pct / 100.*np.sum(data))
    return "{:.1f}%\n({:d})".format(pct, absolute)


datas_file = open("datas.txt","w")
csv_file_name = 'NetflixOriginals.csv'

with open(csv_file_name, 'rb') as rawdata:
    char_detect_result = chardet.detect(rawdata.read(100000))

movies_data = pd.read_csv(csv_file_name,encoding=char_detect_result['encoding'])
movies_data_frame = pd.DataFrame(movies_data)


pd.set_option("display.max_rows", 999)
# datas_file.write(str(movies_data[['Runtime','Language']].sort_values(by='Runtime',ascending=False))+'\n')
# datas_file.write(str(movies_data[['Runtime']].sort_values(by='Runtime',ascending=False))+'\n')
# datas_file.write(str(movies_data['Runtime'].between(89, 101))+'\n')
languages_list = movies_data['Language'].unique()

matching_languages_list = np.array([])
for language in languages_list:
    if "/" in language:
        matching_languages_list =  np.append(matching_languages_list,language.split("/"))
    else:
        matching_languages_list = np.append(matching_languages_list,language)

matching_languages_list = np.unique(matching_languages_list)





# datas_file.write(str(movies_data['Language'].unique())+'\n')
runtime_min = movies_data['Runtime'].min()
runtime_max = movies_data['Runtime'].max()
runtime_value_counts = movies_data['Runtime'].value_counts().sort_index(ascending=False)
runtime_mean = movies_data['Runtime'].mean()
runtime_std = movies_data['Runtime'].std().round() #istenirse burası dğiştirilebilir 
ranges = range(int(runtime_min),int(runtime_max),int(runtime_std))

between_ranges = []
temp = runtime_min
for index in range(1,math.ceil(runtime_max/runtime_std)):
    between_ranges.append([temp,temp+runtime_std])
    temp += runtime_std

if between_ranges[-1][-1] < runtime_max:
    between_ranges[-1][-1] = runtime_max


for ranges in between_ranges:
    print(ranges)
    range_movies = movies_data[movies_data['Runtime'].between(ranges[0], ranges[1])][['Runtime','Language']].sort_values(by='Runtime',ascending=False)
    
    languages_list = range_movies['Language'].unique()
    matching_languages_list = np.array([])
    same_languages_list = np.array([])
    for language in languages_list:
        if "/" in language:
            matching_languages_list =  np.append(matching_languages_list,language.split("/"))
            same_languages_list = np.append(same_languages_list,language)
        else:
            matching_languages_list = np.append(matching_languages_list,language)

    matching_languages_list = np.unique(matching_languages_list)

    #her dil için filmlerin sayısını bul
    movies_counts = range_movies['Language'].value_counts().sort_index(ascending=False)

    
    #verileri düzelt ve temizle
    for language,movie_count in movies_counts.items():
        # birden fazla dili için herdile aynı sayıyı ekle
        if "/" in language:
            for same_count in language.split("/"):
                try:
                    movies_counts[same_count] += movies_counts[language]
                except KeyError as error:
                    new = pd.Series([movies_counts[language]], index=[same_count])
                    movies_counts = pd.concat([movies_counts,new])
            # birden fazla dili sil
            movies_counts = movies_counts.drop(labels=language)
    
    # plt.bar(movies_counts.index,movies_counts.values,label=str(ranges))

    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }

    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(movies_counts.values,
                                    autopct = lambda pct: func(pct, movies_counts.values),
                                    labels = movies_counts.index,
                                    startangle = 90,
                                    wedgeprops = wp,
                                   )

    # Adding legend
    ax.legend(wedges, movies_counts.index,
            title ="Languages",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    plt.setp(autotexts, size = 8, weight ="bold")
    ax.set_title(f"Chart for total {np.sum(movies_counts.values)} movie count runtime between {ranges[0]} and {ranges[1]} min.")

    # # show plot
    # plt.show()
    #burayı aç

    # plt.pie(movies_counts.values, labels = movies_counts.index, autopct='%1.1f%%',)
    # plt.show()

    # print(same_languages_list,range_movies[range_movies['Language'].isin(same_languages_list)])

    # datas_file.write(str(ranges)+'\n')
    # datas_file.write(str(movies_data[movies_data['Runtime'].between(ranges[0], ranges[1])][['Runtime','Language']].sort_values(by='Runtime',ascending=False))+'\n')
    # plt.pie(educational_level , labels = educational_level.index)




# print(runtime_min,runtime_max,runtime_value_counts,runtime_mean,runtime_std)
# datas_file.write(str(movies_data[movies_data['Runtime'].between(89, 101)][['Runtime','Language']])+'\n')

# datas_file.write(str(movies_data[movies_data.Language == 'English'])+'\n')

# datas_file.write(str(movies_data.where((movies_data.Language == 'English') & (movies_data['Runtime'] < 50)).dropna().reset_index(drop=True))+'\n')




#1 kısım son (uzun soluklu filmler hangi dilde oluşturulmuştur)



#2 kısım baş (2019 Ocak ile 2020 Haziran Documentary IMDB)


datas_file.write('\n'+'\n'+str('2019 Ocak ile 2020 Haziran Documentary IMDB')+'\n')
# ingilizce tarih yazsın diye 
locale.setlocale(locale.LC_TIME,'en_US.UTF-8')
# tarihi formatlaki eşleştirebileyim
premiere_dates = [ d.strftime('%B %d, %Y').replace(' 0', ' ') for d in pd.date_range('20190101','20200630')]

# txt fileye yazdır
datas_file.write(str(movies_data[(movies_data['Genre'] == 'Documentary') & (movies_data['Premiere'].isin(premiere_dates))][['Genre','IMDB Score','Premiere']])+'\n')

#2 kısım son (2019 Ocak ile 2020 Haziran Documentary IMDB)


#3 kısım baş (İngilizce olanlardan hangi tür en yüksek IMDB IMDB)


datas_file.write('\n'+'\n'+str('İngilizce olanlardan hangi tür en yüksek IMDB IMDB')+'\n')

results =movies_data[movies_data['Language'] == 'English'][['Language','Genre','IMDB Score']].groupby(['Genre']).max().sort_values(by='IMDB Score',ascending=False)
datas_file.write(str(results)+'\n')

#3 kısım son (İngilizce olanlardan hangi tür en yüksek IMDB IMDB)


#4 kısım baş (Hindi ortalama runtime)
datas_file.write('\n'+'\n'+str('Hindi ortalama runtime')+'\n')
min = movies_data[movies_data['Language'].str.contains("Hindi")][['Runtime']].min()
max = movies_data[movies_data['Language'].str.contains("Hindi")][['Runtime']].max()
size = movies_data[movies_data['Language'].str.contains("Hindi")][['Runtime']].size
mean = movies_data[movies_data['Language'].str.contains("Hindi")][['Runtime']].mean()
sum = movies_data[movies_data['Language'].str.contains("Hindi")][['Runtime']].sum()
result = sum/size
print(min,max,size,sum,mean,result)
datas_file.write('min :'+str(min.values)+'\n')
datas_file.write('max :'+str(max.values)+'\n')
datas_file.write('size :'+str(size)+'\n')
datas_file.write('sum :'+str(sum.values)+'\n')
datas_file.write('mean :'+str(mean.values)+'\n')
datas_file.write('result :'+str(result.values)+'\n')

#4 kısım son (Hindi ortalama runtime)

#5 kısım baş (Genre kategoriler)
datas_file.write('\n'+'\n'+str('Genre kategoriler')+'\n')
result = movies_data['Genre'].value_counts()
label = 'Genre have got '+str(result.size)+' catagories'

plt.rcdefaults()
fig, ax = plt.subplots()
y_pos = np.arange(len(result.index))


ax.barh(y_pos, result.values,  align='center')
ax.set_yticks(y_pos, labels=result.index)
ax.invert_yaxis() 
ax.set_xlabel('Film count')
ax.set_title('Genre catagories and movie count')

# plt.show()
# burayı aç

#5 kısım son (Genre kategoriler)


#6 kısım baş (En çok kullanılan 3 dil)
datas_file.write('\n'+'\n'+str('En çok kullanılan 3 dil ')+'\n')

result = movies_data['Language'].value_counts().sort_values(ascending=False).head(3)
datas_file.write(str(result)+'\n')

#6 kısım son (En çok kullanılan 3 dil)

#7 kısım baş (IMDB En yüksek 10 film)
datas_file.write('\n'+'\n'+str('IMDB En yüksek 10 film')+'\n')
result = movies_data.sort_values(by='IMDB Score',ascending=False).head(10)
datas_file.write(str(result)+'\n')

#7 kısım son (IMDB En yüksek 10 film)

#8 kısım baş (IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır?)
pass
#8 kısım son (IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır?)



#9 kısım baş (IMDB Puanı ilk 10 'Genre')
datas_file.write('\n'+'\n'+str('IMDB Puanı ilk 10 Genre')+'\n')

results = movies_data[['Genre','IMDB Score']].groupby(['Genre']).max().sort_values(by='IMDB Score',ascending=False).head(10)
datas_file.write(str(results)+'\n')
#eksik Görselleştiriniz

#9 kısım son (IMDB Puanı ilk 10 'Genre')

#10 kısım baş (Runtime yüksek ilk 10 film)
datas_file.write('\n'+'\n'+str('Runtime yüksek ilk 10 film')+'\n')

results = movies_data.sort_values(by='Runtime',ascending=False).head(10)
datas_file.write(str(results)+'\n')
#eksik Görselleştiriniz

#10 kısım son (Runtime yüksek ilk 10 film)


#11 kısım baş (En fazla film yayımlanmış yıl)
datas_file.write('\n'+'\n'+str('En fazla film yayımlanmış yıl')+'\n')
movies_data['Year'] = pd.DatetimeIndex(movies_data['Premiere']).year
results = movies_data['Year'].value_counts().sort_values(ascending=False)
datas_file.write(str(results)+'\n')

# Creating plot
fig, ax = plt.subplots()
wedges, texts, autotexts = ax.pie(results.values,
                                autopct = lambda pct: func(pct, results.values),
                                labels = results.index,
                                startangle = 90,
                                wedgeprops = wp,
                                )

# Adding legend
ax.legend(wedges, results.index,
            title ="Years",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
plt.setp(autotexts, size = 8, weight ="bold")
ax.set_title(f"Years and total film count {np.sum(results.values)}")

# # show plot
# plt.show()
#burayı aç
#11 kısım son (En fazla film yayımlanmış yıl)

#12 kısım son (En düşük ortalama IMBD dilleri)
datas_file.write('\n'+'\n'+str('En düşük ortalama IMBD dilleri')+'\n')

movies_data_copy = movies_data[['IMDB Score','Language']].copy()
multi_lingual_movies = movies_data[movies_data['Language'].str.contains("/")][['IMDB Score','Language']].set_index('Language')
movies_data_copy = movies_data_copy.drop(movies_data[movies_data['Language'].str.contains("/")].index,axis=0)
movies_data_copy = movies_data_copy[['IMDB Score','Language']].set_index('Language')
for languages,imdb_score in multi_lingual_movies.iterrows():
    for language in languages.split('/'):
        new_row = pd.DataFrame({'IMDB Score':imdb_score['IMDB Score']}, index=[language])
        movies_data_copy = pd.concat([movies_data_copy,new_row], axis=0)
movies_data_copy['Language'] = movies_data_copy.index
movies_data_copy = movies_data_copy.groupby(['Language']).mean()
print(movies_data_copy.sort_index(ascending=False))

# ax.bar(movies_data_copy.index,movies_data_copy.values.flatten(),label='Dillerin IMBD puan ortalamaları')
# plt.show()
    #     new_row = pd.Series([row['IMDB Score'],lang],columns=['IMDB Score','Language'])
    #     movies_data_copy = pd.concat([movies_data_copy,new_row], axis=0)
    #     print(movies_data_copy.tail(10))
    #     break
    #     # print(str(movies_data_copy.tail(5))+'\n',str(new_row)+'\n')
    #     # print("*****"+'\n')
    # # print(index,'ok',row['IMDB Score'],row['Language'])
    # # print("*****")
    # break
# for imdb_score,language in movies_data[['IMDB Score','Language']].items:
#     print(imdb_score,language)
#     # if "/" in language:
#     #         for same_count in language.split("/")
#     # print(imdb_score,language)
#     break;
# changed_movies_data = movies_data[['IMDB Score','Language']]
# datas_file.write(str(results)+'\n')

# print(results)
sys.exit()

results = movies_data['Year'].value_counts().sort_values(ascending=False)
datas_file.write(str(results)+'\n')
#12 kısım son (En düşük ortalama IMBD dilleri)











pd.set_option("display.max_rows", None)
sys.exit()


datas_file.write(str(movies_data['IMDB Score'].size)+'\n')

datas_file.write(str(movies_data.index.duplicated())+'\n')
datas_file.write(str(movies_data.columns.is_unique)+'\n')


datas_file.write(str(movies_data['IMDB Score'].duplicated())+'\n')
datas_file.write(str(movies_data['IMDB Score'].value_counts().sort_index(ascending=False)))
datas_file.write(str(movies_data['IMDB Score'].value_counts().sort_values(ascending=False)))



pd.set_option("display.max_rows", None)


