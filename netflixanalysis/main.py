import pandas as pd
import os 
import visualization_helper as vh
import analysis_helper as ah
 

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
DATA_FILE_PATH = os.path.join(DATA_PATH, 'NetflixOriginals.csv')
RUNTIME_FOR_LONG_MOVIES = 100
FIGURE_PATH = os.path.join(PROJECT_PATH, 'figures')
print(DATA_FILE_PATH)


def get_data(path):
    """
    This function reads the data from the csv file and returns a dataframe.
    """
    df = pd.read_csv(path, encoding='latin-1')
    return df


def main():
    """
    This function calls the other functions and prints the dataframe.
    """
    dataframe = get_data(DATA_FILE_PATH)
    
    ah.get_data_explore(dataframe)
    clean_dataframe = ah.get_data_clean(dataframe)

    # #! Quesition 1 =  Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? 
    print("*"*25 + " Question 1 Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur?")
    long_movies = ah.get_long_movie(clean_dataframe)
    long_movie_by_lang_fig = vh.get_bar_plot(long_movies, 'Language', 'Runtime', 'Long Movies Grouped by Language')
    vh.save_figure(long_movie_by_lang_fig, FIGURE_PATH, 'long_movie_fig.png')

    #! Quesition 2 =  2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
    print("*"*25, " Question 2 2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.")
    imdb_rating_by_movie_type_for_year = ah.get_imdb_rating_by_movie_type_for_year(clean_dataframe, 'Documentary', "2019-01-01", "2020-06-01")
    imdb_rating_by_movie_type_for_year_fig = vh.get_bar_plot(imdb_rating_by_movie_type_for_year, 'Title', 'IMDB Score', 'Documentary Movies IMDB Rating', x_rotation=90)
    vh.save_figure(imdb_rating_by_movie_type_for_year_fig, FIGURE_PATH, 'imdb_rating_by_movie_type_for_year_fig.png')
    
    #! Quesition 3 =  İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
    print("*"*25, " Question 3 İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?")
    top_imdb_rating_by_lang = ah.find_top_imdb_rating_by_language(clean_dataframe, 'English')
    top_imdb_rating_by_lang_table = vh.create_table(top_imdb_rating_by_lang, 'Top IMDB Rating For English', FIGURE_PATH, 'top_imdb_rating_by_lang_table.html')
    print(top_imdb_rating_by_lang_table)

    #! Quesition 4 =  'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
    print("*"*25, " Question 4 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?")
    avg_runtime_by_lang = ah.get_avg_runtime_by_language(clean_dataframe, 'Hindi')
    avg_runtime_by_lang_frame = pd.DataFrame({'Language': ['Hindi'], 'Runtime': [avg_runtime_by_lang]})
    avg_runtime_by_lang_table = vh.create_table(avg_runtime_by_lang_frame, 'Average Runtime For Hindi', FIGURE_PATH, 'avg_runtime_by_lang_table.html')
    print(avg_runtime_by_lang_table)

    #! Quesition 5 =  'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
    print("*"*25, " Question 5 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.")
    genre_category_count = ah.get_nunique_count_by_column(clean_dataframe, 'Genre')
    print("Genre has of category count: %d" %genre_category_count)
    genre_cat_fig = vh.get_count_bar_plot(clean_dataframe, 'Genre', 'Count', 'Genre Category Count', x_rotation=90)
    vh.save_figure(genre_cat_fig, FIGURE_PATH, 'genre_cat_fig.png')

    #! Quesition 6 =  Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
    print("*"*25, " Question 6 Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.")
    top_3_lang_by_count = ah.get_top_3_lang_by_count(clean_dataframe)
    top_3_lang_by_count_frame = pd.DataFrame({'Language': top_3_lang_by_count.index, 'Count': top_3_lang_by_count.values[:,0][:3]})
    top_3_lang_by_count_table = vh.create_table(top_3_lang_by_count_frame, 'Top 3 Languages By Count', FIGURE_PATH, 'top_3_lang_by_count_table.html')
    print(top_3_lang_by_count_table)

    #! Quesition 7 =  IMDB puanı en yüksek olan ilk 10 film hangileridir?
    print("*"*25, " Question 7 IMDB puanı en yüksek olan ilk 10 film hangileridir?")
    top_10_movies_by_imdb_score = ah.get_top_count_movies_by_imdb_score(clean_dataframe, 10)
    top_10_movies_by_imdb_score_table = vh.create_table(top_10_movies_by_imdb_score, 'Top 10 Movies By IMDB Score', FIGURE_PATH, 'top_10_movies_by_imdb_score_table.html')
    print(top_10_movies_by_imdb_score_table)

    #! Quesition 8 =  IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
    print("*"*25, ": Quesition 8 = IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır?") 
    imdb_runtime_corr = ah.get_column_to_column_corr(clean_dataframe, 'IMDB Score', 'Runtime')
    print(" IMDB Score and Runtime Correlation : ",imdb_runtime_corr)
    imdb_runtime_corr_fig = vh.get_correlation_matrix(dataframe=clean_dataframe, columns=['IMDB Score', 'Runtime'], title='IMDB Score vs Runtime', fig_size=(10,6))
    vh.save_figure(imdb_runtime_corr_fig, FIGURE_PATH, 'imdb_runtime_corr_fig.png')

    #! Quesition 9 =  IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz
    print("*"*25, " :  Quesition 9 = IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz")
    top_10_movies_by_imdb_score_and_genre = ah.get_top_count_movies_by_imdb_score_and_genre(clean_dataframe, 10)
    top_10_movies_by_imdb_score_and_genre_fig = vh.series_to_bar_plot(top_10_movies_by_imdb_score_and_genre, title=" Top 10 Movies By IMDB Score and Genre", fig_size=(10,6))
    vh.save_figure(top_10_movies_by_imdb_score_and_genre_fig, FIGURE_PATH, 'top_10_movies_by_imdb_score_and_genre_fig.png')

    #! Quesition 10 =  Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz
    print("*"*25, " :  Quesition 10 = Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz")
    top_10_movies_by_runtime = ah.get_top_count_movies_by_runtime(clean_dataframe, 10)
    # top_10_movies_by_runtime_fig = vh.get_bar_plot(top_10_movies_by_runtime, title=" Top 10 Movies By Runtime", fig_size=(10,6), x_axis='Runtime', y_axis='Title')
    # vh.save_figure(top_10_movies_by_runtime_fig, FIGURE_PATH, 'top_10_movies_by_runtime_fig.png')

    #! Quesition 11 =  Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
    print("*"*25, " :  Quesition 11 = Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz")
    clean_dataframe_with_year = ah.add_column_with_values(clean_dataframe, "Year", clean_dataframe['Premiere'].dt.year)
    max_count_movies_by_year = ah.get_max_count_movies_by_column(clean_dataframe_with_year, "Year")
    # max_count_movies_by_year_fig = vh.get_count_bar_plot(max_count_movies_by_year, 'Year', 'Title', 'Max Count Movies By Year', x_rotation=45, fig_size=(10,6))
    # vh.save_figure(max_count_movies_by_year_fig, FIGURE_PATH, 'max_count_movies_by_year_fig.png')

    #! Quesition 12 =  Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
    print("*"*25, " :  Quesition 12 = Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz")
    min_imdb_score_by_language = ah.get_min_imdb_score_by_column(clean_dataframe, "Language")
    # min_imdb_score_by_language_fig = vh.series_to_bar_plot(min_imdb_score_by_language, title="Min IMDB Score By Language", fig_size=(10,6), color="blue")
    # vh.save_figure(min_imdb_score_by_language_fig, FIGURE_PATH, 'min_imdb_score_by_language_fig.png')
    print("Answer 12 : ", "min_imdb_score_by_language_fig.png")


    #! Quesition 13 =  Hangi yılın toplam "runtime" süresi en fazladır?
    print("*"*25, " :  Quesition 13 = Hangi yılın toplam \"runtime\" süresi en fazladır?")

    max_runtime_by_year = ah.get_max_runtime_by_column(clean_dataframe_with_year, "Year")
    # max_runtime_by_year_fig = vh.series_to_bar_plot(max_runtime_by_year, title="Max Runtime By Year", fig_size=(10,6), color="red")
    # vh.save_figure(max_runtime_by_year_fig, FIGURE_PATH, 'max_runtime_by_year_fig.png')
    print("Answer 13 : ", "max_runtime_by_year_fig.png")

    #! Quesition 14 =  Her bir dilin en fazla kullanıldığı "Genre" nedir?

    print("*"*25, " :  Quesition 14 = Her bir dilin en fazla kullanıldığı \"Genre\" nedir?")
    max_uses_genre_by_language = ah.get_max_uses_genre_type_by_column(clean_dataframe, "Language")
    max_uses_genre_by_language = pd.DataFrame({'Language': max_uses_genre_by_language.index, 'Genre': max_uses_genre_by_language.values.flatten()})
    max_uses_genre_by_language_table = vh.create_table(max_uses_genre_by_language, ' Max uses genre by language', FIGURE_PATH, 'max_uses_genre_by_language.html')
    print("Answer 14 : ", "max_uses_genre_by_language.html")
    print(max_uses_genre_by_language_table)

    #! Quesition 15 =  Veri setinde outlier veri var mıdır? Açıklayınız.
    print("*"*25, " :  Quesition 15 = Veri setinde outlier veri var mıdır? Açıklayınız.")
    outlier_count = vh.plot_outlier(clean_dataframe)
    ah.outlier_find(clean_dataframe)


if __name__ == "__main__":
    main()