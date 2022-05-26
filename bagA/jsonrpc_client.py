#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_client.py
# JSON-RPC client needing "pip install jsonrpclib-pelix"

from textwrap import indent
from click import command
from jsonrpclib import Server
import json

class FileManageFacade:
    def __init__(self):
        self.proxy = Server('http://localhost:7002')

    def ping(self, cmd):
        return self.proxy.ping(*cmd)

    def ls(self, cmd):
        return self.proxy.ls(*cmd)

    def count(self, cmd):
        return self.proxy.count(*cmd)

    def get(self, cmd):
        return self.proxy.get(*cmd)

def printHelper(replies):
    for r in replies:
        print(r)

def jsonHelper(response):
    print(json.dumps(response, indent=4))

def main():
    facade = FileManageFacade()

    cmd = ''
    while (cmd != 'quit'):
        cmd = input()
        cmds = cmd.split()

        if cmds[0] == 'ping':
            jsonHelper(facade.ping(cmds))
        elif cmds[0] == 'ls':
            printHelper(facade.ls(cmds))
        elif cmds[0] == 'count':
            printHelper(facade.count(cmds))
        elif cmds[0] == 'get':
            jsonHelper(facade.get(cmds))

if __name__ == '__main__':
    main()
