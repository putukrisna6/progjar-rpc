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
            "contents": globbed
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
            "count": len(globbed)
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
    
def send(*args):
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

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(ping)
    server.register_function(ls)
    server.register_function(count)
    server.register_function(get)
    server.register_function(send)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
