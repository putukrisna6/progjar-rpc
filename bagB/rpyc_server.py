#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_server.py
# RPyC server

import rpyc
import glob
import os
import base64

def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        print('Client has invoked exposed_line_counter()')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_ping(self, *args):
        results = []
        words = args[1:]
        argsLen = len(words)

        if argsLen == 0:
            response = {
                "success": False,
                "errorMsg": "Invalid argument count for ping@FileManageFacade"
            }
            results.append(response)
            return results

        msgs = []
        for i in words:
            msgs.append(i)

        response = {
            "success": True,
            "result": {
                "wordCount": argsLen,
                "messages": msgs
            }
        }

        results.append(response)
        return results

    def exposed_ls(self, *args):
        results = []
        argsLen = len(args)

        if argsLen == 1:
            globbed = glob.glob('*')
        else:
            globbed = glob.glob(args[1])

        response = {
            "success": True,
            "result": {
                "contents": globbed
            }
        }
        results.append(response)
        return results

    def exposed_count(self, *args):
        results = []
        argsLen = len(args)

        if argsLen == 1:
            globbed = glob.glob('*')
        else:
            globbed = glob.glob(args[1])

        response = {
            "success": True,
            "result": {
                "count": len(globbed)
            }
        }
        results.append(response)
        return results

if __name__ == '__main__':
    main()
