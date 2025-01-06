def calculate_average(data):
    """
    Prints the average of a given column of data.

    Parameters:
        data (pandas.Series): The column of data to be averaged.

    Returns:
        None
    """
    print(f"\nAverage: {data.mean():.2f}")


def calculate_sum(data):
    """
    Prints the total sum of a given column of data.

    Parameters:
        data (pandas.Series): The column of data to be summed.

    Returns:
        None
    """
    print(f"\nTotal sum: {data.sum():.2f}")


def count_column(data, condition):
    """
    Prints the total count of a given column of data that matches a condition.

    Parameters:
        data (pandas.Series): The column of data to be counted.
        condition (object): The condition to filter the data by.

    Returns:
        None
    """
    filtered_data = data[data == condition]
    print(f"Total: {len(filtered_data)}")
