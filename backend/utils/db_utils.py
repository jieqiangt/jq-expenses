from sqlalchemy import create_engine, URL
from sqlalchemy.sql import text
from jinjasql import JinjaSql
import pandas as pd


SQL_ROOT_FOLDER = './sql'

def create_pgsql_engine():

    connection_url = URL.create(
        "postgresql+psycopg2",
        username="jq-expenses_owner",
        password="zmMAfHCh7Lb5",  
        host="ep-lingering-grass-a19bj0lz-pooler.ap-southeast-1.aws.neon.tech",
        database="jq-expenses",
        query={'sslmode':'require'}
    )
    engine = create_engine(connection_url)
    
    return engine

def get_query_from_sql_file(file_name, params=None):
    jinja = JinjaSql(param_style='pyformat')

    with open(file_name) as my_file:
        template = my_file.read()

    if params:
        query, bind_params = jinja.prepare_query(template, params)
        return text(query % bind_params)

    return text(template)


def execute_in_pgsql(conn, file_path, params=None):

    query = get_query_from_sql_file(file_path, params)
    print(query)
    data = conn.execute(query)
    conn.commit()

    return data


def get_data_from_query(conn, file_path, params=None):

    if params:
        get_data_query = get_query_from_sql_file(file_path, params)
    else:
        get_data_query = get_query_from_sql_file(file_path)

    data = pd.read_sql(get_data_query, conn)

    return data


def drop_table(conn, table):

    drop_query = get_query_from_sql_file(
        f'{SQL_ROOT_FOLDER}/general/drop_table.sql', params={"table": table})
    conn.execute(drop_query)
