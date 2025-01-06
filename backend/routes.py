from flask import Blueprint, jsonify, request
from database import fetch_data_from_db

api = Blueprint('api', __name__)

@api.route('/data', methods=['GET'])
def get_data():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 10))
    start = (page - 1) * per_page
    query = f"SELECT * FROM titanic_data LIMIT {per_page} OFFSET {start}"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))

@api.route('/data/sort', methods=['GET'])
def sort_data():
    column = request.args.get('column', 'Name')
    order = request.args.get('order', 'asc')
    query = f"SELECT * FROM titanic_data ORDER BY {column} {'ASC' if order == 'asc' else 'DESC'}"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))

@api.route('/data/search', methods=['GET'])
def search_data():
    query_param = request.args.get('query', '').lower()
    query = f"SELECT * FROM titanic_data WHERE LOWER(Name) LIKE '%{query_param}%'"
    data = fetch_data_from_db(query)
    return jsonify(data.to_dict(orient='records'))