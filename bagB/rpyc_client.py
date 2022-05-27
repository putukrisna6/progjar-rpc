#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc
import os

def main():
    config = {'allow_public_attrs': True}
    proxy = rpyc.connect('localhost', 18861, config=config)
    # fileobj = open('testfile.txt')
    # linecount = proxy.root.line_counter(fileobj, noisy)
    # print('sek')

    def ls(cmd):
        print(proxy.root.ls(cmd))

    def count(cmd):
        print(proxy.root.count(cmd))

    def put(cmd):
        print(proxy.root.put(cmd))

    def get(cmd):
        print(proxy.root.get(cmd))

    def quit(cmd):
        print(proxy.root.quit(cmd))

if __name__ == '__main__':
    main()
