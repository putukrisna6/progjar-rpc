#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import glob
import os

def ping(*args):
    results = []
    argLen = len(args[1:])

    response = {
        "success": True,
        "result": {
            "wordCount": argLen,
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

    if argsLen != 2:
        response = {
            "success": False,
            "errorMsg": "Not enough argument passed into get@FileManageFacade",
        }
        results.append(response)
        return results

    if os.path.exists(args[1]):
        fileSize = os.path.getsize(args[1]) / 1024
        fileName = (args[1].split('/'))[-1]

        response = {
            "success": True,
            "result": {
                "fileSize": fileSize,
                "fileName" : fileName
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
