import logging


class SchemaRegistryDB:
    def __init__(self, schema_name, db_conn):
        self.schema_name = schema_name
        self.db_cur = db_conn.cursor()

    def check_sc_exists(self):
        """
        Check if schema registry table exists
        :return: True if exists, False if not
        """
        try:
            self.db_cur.execute(f"SELECT 1 FROM schema_registry.{self.schema_name};")
            if self.db_cur.fetchone():
                return True
            else:
                return False
        except:
            return False

    def create_sc(self):
        """
        Create schema sql_schema_registry and schema registry table for schema_name if doesn't exists
        :return: None
        """
        try:
            self.db_cur.execute("CREATE SCHEMA IF NOT EXISTS schema_registry;")
            self.db_cur.execute(
                f"CREATE TABLE IF NOT EXISTS schema_registry.{self.schema_name} (id int, db_name varchar(30) NOT NULL, object_name varchar(50) NOT NULL, DDL varchar(100) NOT NULL, user_name varchar(30), create_ts timestamp NOT NULL, PRIMARY KEY (id));")
            logging.info("Schema registry initialized")
        except Exception as e:
            logging.error("Error: " + str(e))

    def reinit_sc(self):
        """
        Truncate schema registry table to reinitialize process
        :return:
        """
        try:
            self.db_cur.execute(f"TRUNCATE TABLE schema_registry.{self.schema_name};")
        except Exception as e:
            logging.error("Error: " + str(e))

    def get_db_last_id(self):
        """
        Get last id in the schema registry table
        :return: max id in database
        """
        try:
            self.db_cur.execute(f"SELECT MAX(id) FROM schema_registry.{self.schema_name};")
            max_id = self.db_cur.fetchone()[0]
            if not max_id:
                return 0
            else:
                return max_id
        except Exception as e:
            logging.error("Error: " + str(e))

    def insert_sc_record(self, db_name, user, sql_id, ddl, object_name):
        """
        Insert new record in schema registry table
        :param user: Username
        :param object_name: Database object name
        :param ddl: DDL statement in the file and code
        :param db_name: Database name or instance
        :param sql_id: ID for the new record
        :return: None
        """
        try:
            self.db_cur.execute(
                f"INSERT INTO schema_registry.{self.schema_name} (id, db_name, object_name, DDL, user_name, create_ts) VALUES ('{sql_id}', '{db_name}', '{object_name}', '{ddl}', '{user}', now() );")
            logging.info(f'Schema registry table updated with {ddl} {object_name}.')
        except Exception as e:
            logging.error("Error: " + str(e))

    def execute_sql(self, code):
        try:
            self.db_cur.execute(code)
        except Exception as e:
            logging.error("Error: " + str(e))
            exit(1)
