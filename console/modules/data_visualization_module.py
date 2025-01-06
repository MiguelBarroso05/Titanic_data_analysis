import matplotlib.pyplot as plt

### Pie Charts ###

def pie_chart(data, title):
    """
    Creates a pie chart with the given data and title.

    Parameters:
        data (pd.Series): The data to be plotted. The index will be used as the labels and the values will be used to calculate the size of each slice.
        title (str): The title of the chart.

    Returns:
        None
    """
    counts = data.value_counts()
    labels = counts.index
    plt.pie(counts.values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title(title)
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()

def survival_by_category_pie(df, category, title):
    
    """
    Creates a pie chart showing the distribution of a specific category among only the rows where 'Survived' is 'Survived'.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        category (str): The name of the column to be used as the category.
        title (str): The title of the chart.

    Returns:
        None
    """
    survival_counts = df[df['Survived'] == 'Survived'][category].value_counts()
    labels = survival_counts.index
    plt.pie(survival_counts.values, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title(title)
    plt.axis('equal')  
    plt.tight_layout()
    plt.show()


### Bar Charts ###


def bar_chart(data, title, xlabel, ylabel):
    
    """
    Creates a bar chart with the given data, title, and axis labels.

    Parameters:
        data (pd.Series): The data to be plotted. The index will be used as the labels, and the values will determine the height of each bar.
        title (str): The title of the chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None
    """

    counts = data.value_counts()
    plt.bar(counts.index, counts.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def survival_by_category(df, category, title, xlabel, ylabel):
    """
    Creates a bar chart showing the distribution of 'Survived' among the rows for each unique value in the given category.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        category (str): The name of the column to be used as the category.
        title (str): The title of the chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None
    """
    survival_count = df.groupby([category, 'Survived']).size().unstack(fill_value=0)
    
    survival_count.plot(kind='bar', stacked=False, colormap='viridis')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig('data/graphs/survival_by_category.png')
    plt.show()


def category_comparison(df, category1, category2, title, xlabel, ylabel):
    """
    Creates a bar chart comparing the distribution of 'Survived' among the rows for each unique value in category1 and category2.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        category1 (str): The name of the first column to be used for grouping.
        category2 (str): The name of the second column to be used for grouping.
        title (str): The title of the chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None
    """
    comparison = df.groupby([category1, category2, 'Survived']).size().unstack(fill_value=0)
    
    comparison.plot(kind='bar', stacked=False, colormap='viridis')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=category2, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
   

def average_value_by_category(df, value_column, category_column, title, xlabel, ylabel):
    """
    Creates a bar chart showing the average value of a given column, grouped by the unique values in another column.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        value_column (str): The name of the column to be used as the value.
        category_column (str): The name of the column to be used as the category.
        title (str): The title of the chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None
    """
    averages = df.groupby(category_column)[value_column].mean()
    averages.plot(kind='bar', color='lightcoral')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.show()

def stacked_bar_chart(df, value_column, category_column, title, xlabel, ylabel):
    """
    Creates a stacked bar chart showing the distribution of a given column, grouped by the unique values in another column.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data.
        value_column (str): The name of the column to be used as the value.
        category_column (str): The name of the column to be used as the category.
        title (str): The title of the chart.
        xlabel (str): The label for the x-axis.
        ylabel (str): The label for the y-axis.

    Returns:
        None
    """
    stacked_data = df[value_column].groupby(df[category_column]).value_counts().unstack()
    stacked_data.plot(kind='bar', stacked=True, colormap='coolwarm')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title=value_column, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
