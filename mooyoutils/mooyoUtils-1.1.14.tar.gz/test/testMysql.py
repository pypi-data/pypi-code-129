# -*- coding: UTF-8 -*-
# @Time     : 2022/8/12 19:07
# @Author   : Jackie
# @File     : testMysql.py
from mooyoUtils.handlerMysql import MyDB


if __name__ == '__main__':
    db_handler = MyDB()
    sql_stmt = 'select id, mobile from tb_u_user where id < 10;'
    # print(db_handler, type(db_handler))
    # db_handler.execute_sql(sql_stmt)
    # result = db_handler.get_all()

    result = db_handler.explain_sql(sql_stmt)
    print(result)

    print('Done')
