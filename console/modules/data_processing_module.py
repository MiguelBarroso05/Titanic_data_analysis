def calculate_average(data):
    print(f"\nAverage: {data.mean():.2f}")


def calculate_sum(data):
    print(f"\nTotal sum: {data.sum():.2f}")


def count_column(data, condition):
    filtered_data = data[data == condition]
    print(f"Total: {len(filtered_data)}")
