from flask import Blueprint, render_template, request
from db_connect import ConnectDB
import math

dataviewer = Blueprint('dataviewer', __name__)

@dataviewer.route('/dataviewer', defaults={'page': 1}, methods=['GET'])
@dataviewer.route('/dataviewer/<int:page>', methods=['GET'])
def dataviewerfun(page):
    #페이지당 목록 개수(가변)
    records_per_page = 10

    dataset_type = request.args.get('dataset_type')
    start_index = request.args.get('start_index')
    end_index = request.args.get('end_index')
    description = request.args.get('description')

    if start_index is not None and start_index.isdigit():
        start_index = '{:06d}'.format(int(start_index))

    if end_index is not None and end_index.isdigit():
        end_index = '{:06d}'.format(int(end_index))
    sql_query = "SELECT idx, deschan, frame, time FROM mo_dataset WHERE 1"

    if dataset_type:
        sql_query += f" AND kind = {dataset_type}"
    if start_index:
        sql_query += f" AND idx >= '{start_index}'"
    if end_index:
        sql_query += f" AND idx <= '{end_index}'"
    if description:
        sql_query += f" AND deschan LIKE '%{description}%'"

    count_query = f"SELECT COUNT(*) FROM mo_dataset WHERE 1"
    if dataset_type:
        count_query += f" AND kind = {dataset_type}"
    if start_index:
        count_query += f" AND idx >= '{start_index}'"
    if end_index:
        count_query += f" AND idx <= '{end_index}'"
    if description:
        count_query += f" AND deschan LIKE '%{description}%'"

    db_count = ConnectDB(count_query)
    total_count_result = db_count.fetch()
    
    total_count_num = total_count_result[0]['COUNT(*)'] if total_count_result and total_count_result[0] else 0

    total_page_num = max(1, math.ceil(total_count_num / records_per_page))
    end_num = total_count_num % records_per_page
    limit_index = (page - 1) * records_per_page
    sql_query += f" LIMIT {limit_index}, {records_per_page}"

    db = ConnectDB(sql_query)
    dataset = db.fetch()

    max_pagination_links = 9
    start_page = max(1, page - max_pagination_links // 2)

    return render_template('dataviewer.html', dataset=dataset, total_count=total_count_num, total_pages=total_page_num,
                        current_page=page, start_page=start_page, dataset_type=dataset_type, start_index=start_index, 
                        end_index=end_index, description=description)

