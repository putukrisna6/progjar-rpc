#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import glob
import os
import base64

def ping(*args):
    results = []
    argsLen = len(args[1:])

    if argsLen == 0:
        response = {
            "success": False,
            "errorMsg": "Invalid argument count for ping@FileManageFacade"
        }
        results.append(response)
        return results

    response = {
        "success": True,
        "result": {
            "wordCount": argsLen,
            "messages": args[1:]
        }
    }

    results.append(response)
    return results

def ls(*args):
    results = []
    argsLen = len(args)

    if argsLen == 1:
        globbed = glob.glob('*')
    else:
        globbed = glob.glob(args[1])

    response = {
        "success": True,
        "result": {
            "files": globbed
        }
    }
    results.append(response)
    return results

def count(*args):
    results = []
    argsLen = len(args)

    if argsLen == 1:
        globbed = glob.glob('*')
    else:
        globbed = glob.glob(args[1])

    response = {
        "success": True,
        "result": {
            "fileCount": len(globbed)
        }
    }
    results.append(response)
    return results

def get(*args):
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

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(ping)
    server.register_function(ls)
    server.register_function(count)
    server.register_function(get)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
