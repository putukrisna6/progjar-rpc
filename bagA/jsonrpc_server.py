#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import glob

def ping(*args):
    results = []
    parse = args[0].split()
    parseLen = len(parse[1:])

    results.append(('Size', parseLen))
    results.append(('Message', parse[1:]))

    return results

def ls(*args):
    results = []
    parse = args[0].split()
    parseLen = len(parse)

    if parseLen == 1:
        globbed = glob.glob('*')
    else:
        globbed = glob.glob(parse[1])

    for i in globbed:
        results.append(i)

    return results

def count(*args):
    results = []
    parse = args[0].split()
    parseLen = len(parse)

    if parseLen == 1:
        globbed = glob.glob('*')
    else:
        globbed = glob.glob(parse[1])

    results.append(('Size', len(globbed)))

    return results

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(ping)
    server.register_function(ls)
    server.register_function(count)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()
