import matplotlib.pyplot as plt
import seaborn as sns
import os

def get_bar_plot(dataframe, x_axis, y_axis, title, fig_size=(15,15), x_rotation=45):
    """
    This function returns a bar plot.
    """
    figure = plt.figure(figsize=fig_size)
    figure.suptitle(title, fontsize=20)
    sns.barplot(x=x_axis, y=y_axis, data=dataframe)
    plt.xticks(rotation=x_rotation)
    plt.title(title)
    plt.show()
    return figure

def get_count_bar_plot(dataframe, x_axis, y_axis, title, fig_size=(15,15), x_rotation=45):
    """
    This function returns a count bar plot.
    """
    figure = plt.figure(figsize=fig_size)
    figure.suptitle(title, fontsize=20)
    sns.countplot(x=x_axis, data=dataframe)
    plt.xticks(rotation=x_rotation)
    plt.title(title)
    plt.show()
    return figure

def save_figure(figure, figure_path, figure_name):
    """
    This function saves the figure.
    """
    figure.savefig(os.path.join(figure_path, figure_name))
    plt.close()

def create_table(dataframe, title, table_path, table_name):
    """
    This function creates a table.
    """
    print(title)
    dataframe.to_html(os.path.join(table_path, table_name), index=False)
    return dataframe

def get_correlation_matrix(dataframe, title, fig_size=(15,10), columns=[]):
    """
    This function returns a correlation plot.
    """
    figure = plt.figure(figsize=fig_size)
    figure.suptitle(title, fontsize=20)
    sns.heatmap(dataframe[columns].corr(), annot=True, cmap='YlGnBu')
    plt.title(title)
    plt.show()
    return figure