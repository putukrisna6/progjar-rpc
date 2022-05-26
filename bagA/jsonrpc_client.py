#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_client.py
# JSON-RPC client needing "pip install jsonrpclib-pelix"

from jsonrpclib import Server
import json

def main():
    proxy = Server('http://localhost:7002')

    cmd = ''
    while (cmd != 'quit'):
        cmd = input()
        print(proxy.ping(cmd))

if __name__ == '__main__':
    main()
