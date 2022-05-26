#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import glob

def ping(*args):
    results = []
    results.append(('Size', len(args)))

    i = 1
    for arg in args:
        results.append(('Message_{}'.format(i), arg))
        i += 1

    return results

def ls(*args):
    results = []
    argSize = len(args)

    if argSize == 1:
        globbed = glob.glob('*')
    else:
        globbed = glob.glob(args[1])

    for i in globbed:
        results.append(i)

    return results

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(ping)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
