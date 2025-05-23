import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

import pyv8env
from pyv8env.env.impl import *


def callback(ctx, *arg):
    print(ctx.exec_js('''debugger;  1+1;'''))

    print(ctx.exec_js('''debugger;  window.outerWidth;'''))

    try:
        print(ctx.exec_js('''debugger;  xxx; ''', 'VM1'))
    except pyv8env.JSException as e:
        print(e)


def test():
    win = Window(hook=True, )
    win.start(devtool=False, callback=callback)
    # win.start(devtool=True, callback=callback)


if __name__ == '__main__':
    test()
