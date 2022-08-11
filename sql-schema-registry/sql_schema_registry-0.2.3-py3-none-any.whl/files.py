import logging
from pathlib import Path
import sqlparse


class SchemaRegistryFiles:
    def __init__(self, schema_name):
        self.schema_name = schema_name

    def get_file_list_ordered(self, sql_path):
        """
        Get list of sql files ordered in ascended order
        :param sql_path: path to sql files
        :return: sql list files ordered
        """
        try:
            sql_list = []
            for filename in sorted(Path(sql_path + "/" + self.schema_name).glob('*.sql'),
                                   key=lambda path: int(path.stem.rsplit('-')[0])):
                sql_list.append(filename)
            return sql_list
        except Exception as e:
            logging.error("Error: " + str(e))

    @staticmethod
    def _read_file(filepath):
        """
        Read file as text
        :param filepath: path to file
        :return: file text
        """
        return Path(filepath).read_text()

    @staticmethod
    def _write_file(filepath, code):
        """
        Write code in file
        :param filepath: path to file
        :param code: SQL code
        :return: Path object
        """
        return Path(filepath).write_text(code)

    @staticmethod
    def parse_sql_file(sql_file):
        """
        Parse sql file name
        :param sql_file: File name
        :return: dll and object_name from the file name
        """
        ddl = ' '.join(sql_file.split('-')[1].split('_')[:2])
        object_name = '_'.join(''.join(sql_file.split('-')[1]).split('_')[2:]).split('.')[0]
        return ddl, object_name

    def check_qa_sql_file(self, sql_file, rewrite=True):
        """
        Rewrites sql file with formatted SQL code and checks that file name info is same as in code
        :param rewrite: Rewrite sql file with formatted standard code
        :param sql_file: file name
        :return: SQL code processed
        """
        try:
            code = self._read_file(sql_file)
            # Reformat code and save in same file
            code = sqlparse.format(code, keyword_case="upper")
            ddl, object_name = self.parse_sql_file(sql_file=sql_file)
            if ddl in code and object_name in code:
                if rewrite:
                    self._write_file(filepath=sql_file, code=code)
                return code
            else:
                logging.error("File name and code doesn't match.")
        except Exception as e:
            logging.error("Error: " + str(e))
