# -*- coding: utf-8 -*-
# @Time    : 2022/8/11 20:41
# @Author  : qxcnwu
# @FileName: MCDDownload.py
# @Software: PyCharm

from ModisDownload import visited

if __name__ == '__main__':
    a = visited.search_p()
    # 查询可下载区域
    b = visited.search_area()

    g=visited.getHtml("cXhjMTIzOmNYaGpibmQxUUdkdFlXbHNMbU52YlE9PToxNjYwMjIyMDAwOjVmZDhhYjg5MGY1Y2JhOGQ0ZjNhYTU3NmMxODZjYjhmNTFmZDMzMTk")
    g.download_main("MCD15A2H","2022-07-28..2022-08-11","china","hdf/")