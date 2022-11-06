from flask import Flask, jsonify, request
from flask_urls import *


app = Flask(__name__)

@app.route("/")
def first_page():
    return "Welcome in DataBase manager."

@app.route("/tables_name")
def flsk_fetch_tables_mane():
    return jsonify(fetch_table_names())

@app.route("/create_table", methods=["POST"])
def flsk_create_new_table():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name", "columns"]

    if len(post_data) != 2:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>", \n' \
               '"columns" : "<col_name col_type>,<col_name col_type>,..." \n'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>", \n' \
                       '"columns" : "<col_name col_type>,<col_name col_type>,..." \n'

    flsk_table_name = post_data["table_name"]
    flsk_columns = post_data["columns"]

    # Method from flask_urls imported module
    create_new_table_flsk(flsk_table_name, flsk_columns)

    return "Parameters are correct. \n" \
           "Send request to create new table!"

@app.route("/add_record", methods=["POST"])
def add_record_to_table():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name", "data_in_columns"]

    if len(post_data) != 2:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>", \n' \
               '"data_in_columns" : "<data>,<data>,..." \n'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>", \n' \
                       '"data_in_columns" : "<data>,<data>,..." \n'

    flsk_table_name = post_data["table_name"]
    flsk_data_in_columns = post_data["data_in_columns"]

    add_new_record_flsk(flsk_table_name, flsk_data_in_columns)

    return "Record added correctly."

@app.route("/fetch_columns_in_table", methods=["POST"])
def fetch_columns_in_table():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name"]

    if len(post_data) != 1:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>" \n'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>" \n'

    flsk_table_name = post_data["table_name"]

    return jsonify(fetch_columns_in_table_flsk(flsk_table_name))

@app.route("/fetch_records_in_table", methods=["POST"])
def fetch_records_in_table():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name"]

    if len(post_data) != 1:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>" \n'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>" \n'

    flsk_table_name = post_data["table_name"]

    print(fetch_records_in_table_flsk(flsk_table_name))
    result_data = fetch_records_in_table_flsk(flsk_table_name)
    res_dict = {}

    for elm in result_data:
        res_dict[f"Record {elm[0]}:"] = elm[1:]

    if res_dict:
        return jsonify(res_dict)
    else:
        return "Table is empty. There is no any record!"

@app.route("/delete_record_by_index", methods=["POST"])
def delete_record_by_index():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name", "index"]

    if len(post_data) != 2:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>", \n' \
               '"index" : "<index>'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>", \n' \
                       '"index" : "<index>" \n'

    flsk_table_name = post_data["table_name"]
    flsk_index = post_data["index"]

    result = delete_record_by_index_flsk(flsk_table_name, flsk_index)

    return jsonify(result)

@app.route("/delete_all_records_in_table", methods=["POST"])
def delete_all_records():
    print(request.get_json())
    post_data = request.get_json()

    mandatory_elements = ["table_name"]

    if len(post_data) != 1:
        return 'Wrong number of parameters! \n' \
               'Write parameters like described below: \n' \
               '"table_name" : "<table_name>", \n'
    else:
        for elm in post_data:
            if not elm in mandatory_elements:
                return 'Wrong parameters! \n' \
                       'Write parameters like described below: \n' \
                       '"table_name" : "<table_name>" \n'

    flsk_table_name = post_data["table_name"]

    result = delete_all_records_in_table(flsk_table_name)
    result = result[1:]

    if result[8] == "0":
        return result + ". " + "Table is already empty!"
    else:
        return jsonify(result)




