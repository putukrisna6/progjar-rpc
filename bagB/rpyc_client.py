#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc
import os
import json

class FileManageFacade:
    def __init__(self):
        config = {'allow_public_attrs': True}
        self.proxy = rpyc.connect('localhost', 18861, config=config)

    def line_counter(self, fileobj, noisy):
        return self.proxy.root.line_counter(fileobj, noisy)

    def ping(self, cmd):
        return self.proxy.root.ping(*cmd)

    def ls(self, cmd):
        return self.proxy.root.ls(*cmd)

    def count(self, cmd):
        return self.proxy.root.count(*cmd)

    def get(self, cmd):
        return self.proxy.root.get(*cmd)

    def send(self, cmd):
        return self.proxy.root.send(*cmd)

def jsonHelper(response):
    print(json.dumps(response, indent=4))

def printHelper(replies):
    for r in replies:
        print(r)

def main():
    facade = FileManageFacade()

    # fileobj = open('testfile.txt')
    # linecount = facade.line_counter(fileobj, noisy)
    # print('The number of lines in the file was', linecount)
    cmd = ''
    while (cmd != 'quit'):
        cmd = input()
        cmds = cmd.split()

        if cmds[0] == 'ping':
            printHelper(facade.ping(cmds))
        elif cmds[0] == 'ls':
            printHelper(facade.ls(cmds))
        elif cmds[0] == 'count':
            printHelper(facade.count(cmds))
        # elif cmds[0] == 'get':
        #     getHelper(facade.get(cmds))
        # elif cmds[0] == 'send':
        #     fileData = sendHelper(cmds)
        #     jsonHelper(facade.send(fileData))

def noisy(string):
    print('Noisy:', repr(string))

if __name__ == '__main__':
    main()
