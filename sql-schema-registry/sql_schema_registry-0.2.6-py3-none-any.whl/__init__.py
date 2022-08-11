import logging

from . import database, files

logging.getLogger().setLevel(logging.INFO)


def deploy(schema_name, files_path, db_name, db_conn, user_name=None, schema_restart=False):
    """
    Schema registry deployment
    :param user_name: Name of the user
    :param db_name: Database or instance name
    :param db_conn: Connection to the database
    :param schema_name: Name of the schema to deploy
    :param files_path: Path of sql files
    :param schema_restart: Restart deployment from scratch
    :return: None
    """

    sc_db = database.SchemaRegistryDB(schema_name=schema_name, db_conn=db_conn)
    sc_files = files.SchemaRegistryFiles(schema_name=schema_name)
    # Check if SC exists and init if not
    if not sc_db.check_sc_exists():
        sc_db.create_sc()
    # Check reinitialize option
    if schema_restart:
        sc_db.reinit_sc()
    db_last_id = sc_db.get_db_last_id()
    sql_files_list = sc_files.get_file_list_ordered(sql_path=files_path)
    sql_id = 0
    for sql_file in sql_files_list:
        # QA file name and sql cod  e
        sql_code = sc_files.check_qa_sql_file(sql_file=sql_file)
        sql_id = int(sql_file.name.split('-')[0])
        # Only deploy ids bigger than currently deployed
        if db_last_id < sql_id:
            sc_db.execute_sql(sql_code)
            logging.info(f'ID {sql_id} SQL file executed.')
            ddl, object_name = sc_files.parse_sql_file(sql_file=sql_file.name)
            sc_db.insert_sc_record(db_name=db_name, user=user_name, sql_id=sql_id, ddl=ddl, object_name=object_name)
    if db_last_id > sql_id:
        logging.error('Max database id is bigger than max files id.')
    else:
        logging.info('Deployment up to date.')
