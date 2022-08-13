import json
from pyecharts.charts import Grid, Page
from pyecharts import options as opts

def render_html_from_ec_option_json(jsn, html_name='ec', save_path='./', return_format='html', **kwargs):
    """
    Render a echarts chart from a json object.
    return_format: 'html' or 'pyecharts'
    """
    ec_grid = (
        Grid(init_opts=opts.InitOpts())
    )
    ec_grid.options = jsn

    page = Page(page_title=html_name, interval=1)
    page.add(ec_grid)
    html_filename = save_path+html_name+'.html'
    page.render(html_filename)

    if return_format == 'html':
        with open(html_filename, "rb") as f:
            html = f.read()
            return html
    else:
        return page

def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        jsn = json.load(f)
    return jsn

def read_json_str(str):
    jsn = json.loads(str)
    return jsn

if __name__ == '__main__':

    import sys
    render_html_from_ec_option_json(*sys.argv)