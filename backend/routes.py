from flask import jsonify, Blueprint, request
from database import fetch_data_from_db
import pandas as pd
import sqlite3

routes_bp = Blueprint('routes', __name__)

@routes_bp.route("/api/data", methods=["GET"])
def get_all_data():
    """
    Route to fetch everything from 'titanic_data'.
    """
    try:
        query = "SELECT * FROM titanic_data"
        df = fetch_data_from_db(query)
        return jsonify(df.to_dict(orient="records"))
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@routes_bp.route("/api/average_fare", methods=["GET"])
def get_average_fare():
    """
    Route to calculate average (Fare).
    """
    try:
        query = "SELECT AVG(Fare) AS average_fare FROM titanic_data"
        df = fetch_data_from_db(query)
        return jsonify({"average_fare": round(df.iloc[0]['average_fare'], 2)})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500


@routes_bp.route('/api/process', methods=["GET"])
def process_data():
    type_ = request.args.get("type")
    column = request.args.get("column")

    if not type_ or not column:
        return jsonify({"error": "Invalid parameters"}), 400

    query = f"SELECT {column} FROM titanic_data"
    try:
        conn = sqlite3.connect("../db/titanic.sqlite")
        df = pd.read_sql(query, conn)

        if type_ == "average":
            result = df[column].mean()
        elif type_ == "sum":
            result = df[column].sum()
        elif type_ == "min":
            result = df[column].min()
        elif type_ == "max":
            result = df[column].max()
        else:
            return jsonify({"error": "Invalid processing type"}), 400

        return jsonify({"value": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
