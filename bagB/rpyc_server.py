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

    def exposed_get(self, *args):
        results = []
        argsLen = len(args)

        if argsLen != 3:
            response = {
                "success": False,
                "errorMsg": "Invalid argument count for get@FileManageFacade",
            }
            results.append(response)
            return results

        if os.path.exists(args[1]):
            fileSize = os.path.getsize(args[1]) / 1024
            fileName = (args[1].split('/'))[-1]
            fileTarget = args[2]
            
            f = open(args[1], 'rb').read()
            fileEncoded = base64.b64encode(f)

            response = {
                "success": True,
                "result": {
                    "fileSize": fileSize,
                    "fileName": fileName,
                    "fileTarget": fileTarget,
                    "fileEncoded": fileEncoded
                }
            }
            results.append(response)
            return results

        response = {
            "success": False,
            "errorMsg": "File not found"
        }
        results.append(response)
        return results

    def exposed_send(self, *args):
        results = []
        argsLen = len(args)

        if argsLen == 1 and args[0] == 'FILE_NOT_FOUND':
            response = {
                "success": False,
                "errorMsg": "Unable to receive file"
            }
            results.append(response)
            return results

        if argsLen != 2:
            response = {
                "success": False,
                "errorMsg": "Invalid argument count for send@FileManageFacade",
            }
            results.append(response)
            return results

        decoded = base64.b64decode(args[1])
        f = open('server_files/' + args[0], 'wb')
        f.write(decoded)
        f.close

        response = {
            "success": True,
        }
        results.append(response)
        return results

if __name__ == '__main__':
    main()
