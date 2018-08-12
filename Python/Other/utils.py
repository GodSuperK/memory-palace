"""
工具模块

"""
import ssl
import logging

from prettytable import PrettyTable


# 迭代cookie
def show_cookie(cookie):
    """迭代cookie"""
    table = PrettyTable(
        field_names=('name', 'value'), header_style="upper",
        padding_width=5)
    for c in cookie:
        table.add_row((c.name, c.value))

    print(table)


# 取消ssl全局验证
def unverified_ssl():
    ssl._create_default_https_context = ssl._create_unverified_context


# 获取 logger 实例
def get_logger():
    logger = logging.getLogger('monitor')
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter('%(asctime)s - %(message)s')
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)
    return logger

