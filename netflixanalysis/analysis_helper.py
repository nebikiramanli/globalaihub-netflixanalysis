from textwrap import indent
import pandas as pd
RUNTIME_FOR_LONG_MOVIES = 100
def get_data_explore(dataframe):
    """
    This function prints the dataframe explanation 
    """
    print("*/"*10  + " Dataframe Exploration  " + "*/"*10)
    print("*"*10  + " Dataframe Head  " + "*"*10)
    print("\n",dataframe.head())
    print("*"*10  + " Dataframe Info  " + "*"*10)
    print("\n",dataframe.info())
    print("*"*10  + " Dataframe Describe  " + "*"*10)
    print("\n",dataframe.describe())
    print("*"*10  + " Dataframe Shape  " + "*"*10)
    print("\n",dataframe.shape)
    print("*"*10  + " Dataframe Columns  " + "*"*10)
    print("\n",dataframe.columns)
    print("*"*10  + " Dataframe Index  " + "*"*10)
    print("\n",dataframe.index)


def get_data_clean(dataframe):
    """
    This function cleans the dataframe and returns a cleaned dataframe.
    """
    dataframe.dropna(inplace=True)
    dataframe.drop_duplicates(inplace=True)
    dataframe.reset_index(drop=True, inplace=True)
    return dataframe


def get_long_movie(dataframe, runtime=RUNTIME_FOR_LONG_MOVIES):
    """
    This function returns a dataframe with the long movies grouped by language.
    """
    long_movies = dataframe[dataframe['Runtime'] > runtime]
    return long_movies


def get_imdb_rating_by_movie_type_for_year(dataframe, movie_type, start_year, end_year):
    """
    This function returns a dataframe with the IMDB rating for the given movie type and year.
    """
    dataframe["Premiere"] = pd.to_datetime(dataframe["Premiere"])
    imdb_rating_by_movie_type_for_year = dataframe[(dataframe['Genre'] == movie_type) & (dataframe['Premiere'] >= start_year) & (dataframe['Premiere'] <= end_year)]
    return imdb_rating_by_movie_type_for_year


def find_top_imdb_rating_by_language(dataframe, language):
    """
    This function returns the top IMDB rating for the given language.
    """
    dataframe = dataframe[dataframe['Language'] == language]
    dataframe = dataframe.sort_values(by='IMDB Score', ascending=False)
    return dataframe.iloc[0].to_frame()

def get_avg_runtime_by_language(dataframe, language):
    """
    This function returns the average runtime for the given language.
    """
    dataframe = dataframe[dataframe['Language'] == language]
    avg_runtime = dataframe['Runtime'].mean()
    return avg_runtime

def get_nunique_count_by_column(dataframe, column_name):
    """
    This function returns the number of unique genres.
    """
    return dataframe[column_name].nunique()


def get_top_3_lang_by_count(dataframe):
    """
    This function returns the top 3 languages by count.
    """
    dataframe = dataframe.groupby('Language').count()
    dataframe = dataframe.sort_values(by='Title', ascending=False)
    return dataframe.iloc[:3]

def get_top_count_movies_by_imdb_score(dataframe, count):
    """
    This function returns the top count movies by IMDB score.
    """
    dataframe = dataframe.sort_values(by='IMDB Score', ascending=False, inplace=False)
    return dataframe.iloc[:count]

def get_column_to_column_corr(dataframe, column1, column2):
    """
    This function returns the correlation between two columns.
    """
    return dataframe[column1].corr(dataframe[column2])
