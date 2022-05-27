#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc
import os

class FileManageFacade:
    def __init__(self):
        config = {'allow_public_attrs': True}
        self.proxy = rpyc.connect('localhost', 18861, config=config)

    def line_counter(self, fileobj, noisy):
        return self.proxy.root.line_counter(fileobj, noisy)

    def ping(self, cmd):
        return self.proxy.ping(*cmd)

    def ls(self, cmd):
        return self.proxy.ls(*cmd)

    def count(self, cmd):
        return self.proxy.count(*cmd)

    def get(self, cmd):
        return self.proxy.get(*cmd)

    def send(self, cmd):
        return self.proxy.send(*cmd)

def main():
    facade = FileManageFacade()

    fileobj = open('testfile.txt')
    linecount = facade.line_counter(fileobj, noisy)
    print('The number of lines in the file was', linecount)

def noisy(string):
    print('Noisy:', repr(string))

if __name__ == '__main__':
    main()
