RED = 0
YELLOW = 0
BLACK = 0
GREEN = 0
MAGENTA = 0
CYAN = 0
WHITE = 0  # 可用颜色


def echo(something, color=WHITE, end="\n") -> None:
    """
    建议使用的输出\n
    Eg.\n
    echo("标准色",GREEN)\n
    echo("十六进制","f35336")\n
    echo("256色",72)\n
    echo("RGB",(30, 144, 255))\n
    \n
    echo("通过256色设置 前景色，后景色",(23,145))\n
    echo("通过十六进制设置 前景色，后景色",("2add9c","eaff56"))\n
    echo("通过RGB设置 前景色，后景色",((20, 144, 234),(234, 78, 23)))\n
    \n
    echo("混搭",((30, 144, 255),"c93756"))\n
    :param something: 可以为任意类型，如果是字典，列表将输出他们在go中的结构
    :param color: 输出的颜色，可省略，默认为utils.WHITE。
    :param end: 输出的结尾，可省略，默认为换行符
    :return:
    """
    ...


def select(title: str, items: list) -> (int, str):
    """
    生成一个选择菜单，方向键选择，Enter确认 \n
    :param title: 标题
    :param items: 可选择的项目，字符串列表，若为空则不会阻塞
    :return: 返回选项序号与选项文本
    """
    ...


def walk_dir(path: str, recursion=False) -> list:
    """
    遍历文件夹\n
    :param path: 路径
    :param recursion: 递归，可省略，默认false
    :return: 所有文件与文件夹
    """
    ...


def unzip(src: str, passwd: str, dest: str) -> None:
    """
    解压zip \n
    :param src: zip文件路径
    :param passwd: 密码，可省略，默认为空字符串
    :param dest: 目标路径，可省略，默认解压在zip同目录下
    :return:
    """
    ...


def zip(src: str, passwd: str, dest: str) -> None:
    """
    压缩zip \n
    :param src: 文件夹路径
    :param passwd: 密码，可省略，默认为空字符串
    :param dest: 目标路径，可省略，默认为最后文件夹.zip
    :return:
    """
    ...


def notice(title: str, msg: str, png_path="", beep=False) -> bool:
    """
    弹出通知\n
    :param title: 标题
    :param msg: 消息
    :param png_path: 显示图片，可省略，默认为空字符串
    :param beep: 是否蜂鸣，可省略，默认false
    :return:
    """
    ...


def read_file(file_path: str) -> bytes:
    """
    读取文件\n
    :param file_path:
    :return:
    """
    ...


def save_file(file_path: str, content: str, cover=False) -> None:
    """
    保存文件\n
    :param file_path: 保存文件路径
    :param content: 内容
    :param cover: 是否覆盖，可省略，默认false
    :return:
    """
    ...


def input(prefix=">", color=WHITE, items={}) -> str:
    """
    带有补全提示的输入\n
    :param prefix: 前缀，可省略，默认为">"
    :param color: 颜色，前缀的颜色，可省略，默认为utils.WHITE
    :param items: 字典，键为提示词，值为描述。e.g.{"hello":"你好"}，可省略，默认空
    :return:
    """
    ...


def search(text: str, items: list, fuzzy=False) -> dict:
    """
    在字符串列表中搜索字符串\n
    :param text: 需要搜索的字符串
    :param items: 被搜索的字符串列表
    :param fuzzy: 是否启用模糊搜索，可省略，默认False
    :return: 返回一个字符串字典，值为搜索到的结果，键为结果所在行
    """
    ...


def fuzzy_match(text1: str, text2: str) -> bool:
    """
    在文本2中模糊匹配文本1\n
    :param text1: 文本1
    :param text2: 文本2
    :return:
    """
    ...


def fuzzy_search(text1: str, text_list: list) -> list:
    """
    在文本列表中模糊匹配文本\n
    :param text1: 文本
    :param text_list: 文本列表
    :return:
    """
    ...


def exec_js(script: str) -> str:
    """
   执行JavaScript代码\n
   :param script: js代码
   :return:
   """
    ...


def exec_js_file(file_path: str) -> str:
    """
   执行js文件\n
   :param file_path: js文件路径
   :return:
   """
    ...


def format(format_str: str, *args) -> str:
    """
    格式化字符串\n
    :return:
    """


class ProgressBar:
    def __init__(self, max_int: int):
        """
        生成一个进度条\n
        :param max_int: 最大进度值
        """
        ...

    def set(self):
        """
        设置进度\n
        :return:
        """
        ...

    def add(self):
        """
        增加进度\n
        :return:
        """
        ...


def now() -> str:
    """
    返回当前时间字符串\n
    :return:
    """


def center(something, color=WHITE, end="\n") -> None:
    """
    居中输出，拥有和echo同样的多种颜色格式支持\n
    :param something: 字符串
    :param color: 输出的颜色，可省略，默认为utils.WHITE。
    :param end: 输出的结尾，可省略，默认为换行符
    :return:
    """
    ...
