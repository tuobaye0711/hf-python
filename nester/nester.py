"""这个函数用来深度遍历并且打印列表"""
import sys


def print_lol(the_list, indent=False, tab_num=0, fn=sys.stdout):
    for l in the_list:
        if isinstance(l, list):
            print_lol(l, indent, tab_num+1, fn)
        else:
            if indent:
                for num in range(tab_num):
                    print("\t", end='', file=fn)
            print(l, file=fn)