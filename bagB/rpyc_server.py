#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_server.py
# RPyC server

import rpyc
import glob
import os

def main():
    from rpyc.utils.server import ThreadedServer
    server = ThreadedServer(MyService, port = 18861)
    server.start()

class MyService(rpyc.Service):
    # def exposed_line_counter(self, fileobj, function):
    #     print('Client has invoked exposed_line_counter()')
    #     for linenum, line in enumerate(fileobj.readlines()):
    #         function(line)
    #     return linenum + 1
    def ls(self, input):
        return input

    def count(self, input):
        return input

    def put(self, input):
        return input

    def get(self, input):
        return input

    def quit(self, input):
        return input

if __name__ == '__main__':
    main()
