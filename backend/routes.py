from flask import Blueprint, jsonify, request
from database import fetch_data_from_db

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    """
    Retrieves a paginated list of data from the Titanic dataset.

    Query Parameters:
        page (int): The page number of data to retrieve. Defaults to 1.
        per_page (int): The number of records per page. Defaults to 10.

    Returns:
        Response: A JSON response containing the requested data records.
    """

    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    query = f"SELECT * FROM titanic_data LIMIT {per_page} OFFSET {start}"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))

@api.route('/data/sort', methods=['GET'])
def sort_data():
    """
    Sorts the Titanic dataset by a specified column in ascending or descending order.

    Query Parameters:
        column (str): The column to sort by. Defaults to 'Name'.
        order (str): The order of the sort. Defaults to 'asc'.

    Returns:
        Response: A JSON response containing the sorted data records.
    """
    column = request.args.get('column', 'Name')
    order = request.args.get('order', 'asc')
    query = f"SELECT * FROM titanic_data ORDER BY {column} {'ASC' if order == 'asc' else 'DESC'}"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))

@api.route('/data/search', methods=['GET'])
def search_data():
    """
    Searches for records in the Titanic dataset by name.

    Query Parameters:
        query (str): The search query to match in the Name column.

    Returns:
        Response: A JSON response containing the search results.
    """
    query_param = request.args.get('query', '').lower()
    query = f"SELECT * FROM titanic_data WHERE LOWER(Name) LIKE '%{query_param}%'"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))