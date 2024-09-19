from utils.db_utils import create_pgsql_engine, execute_in_pgsql, get_data_from_query
import pandas as pd
import os


DATABASE_TABLES = ['trs_users','dim_dates','dim_categories','trs_recur_expenses','trs_expenses']

def drop_tables():
    pg_engine = create_pgsql_engine()
    with pg_engine.connect() as pgsql_conn:
        for table in DATABASE_TABLES:
            params = {'table': table}
            execute_in_pgsql(
                pgsql_conn, f'./sql/general/drop_table.sql', params)

def create_tables():    
    pg_engine = create_pgsql_engine()
    with pg_engine.connect() as pgsql_conn:
        root_folder = './sql/create_table'
        for table in DATABASE_TABLES:
            create_table_file_path = os.path.join(root_folder,f'{table}.sql')
            execute_in_pgsql(pgsql_conn,create_table_file_path)
            
def seed_tables():
    
    pg_engine = create_pgsql_engine()
    with pg_engine.connect() as pgsql_conn:
        root_folder = './backup'
        for table in DATABASE_TABLES:
            file_path = os.path.join(root_folder,f'{table}.csv')
            data = pd.read_csv(file_path)
            date_cols = ['exp_date','recurring_start','recurring_end','created_on', 'updated_on']
            for col in data.columns:                
                if col in date_cols:
                    data[col] = pd.to_datetime(data[col],dayfirst=True)

            data.to_sql(table, con=pgsql_conn, if_exists='append', index=False)
            
def backup_tables():
    
    pg_engine = create_pgsql_engine()
    with pg_engine.connect() as pgsql_conn:
        root_folder = './backup'
        for table in DATABASE_TABLES:
            params = {'table': table}
            data = get_data_from_query(pgsql_conn, f'./sql/general/query_all_from_table.sql', params)
            file_path = os.path.join(root_folder,f'{table}.csv')
            data.to_csv(file_path,index=False)
        
        
