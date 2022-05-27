#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_client.py
# RPyC client

import rpyc
import os
import base64

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

def printHelper(replies):
    for r in replies:
        print(r)

def getHelper(response):
    printHelper(response)

    if not response[0]['success']:
        return

    result = response[0]['result']
    fileEncoded = result['fileEncoded']
    fileTarget = result['fileTarget']
    
    decoded = base64.b64decode(fileEncoded)
    f = open('client_files/' + fileTarget, 'wb')
    f.write(decoded)
    f.close()

def sendHelper(cmds):
    fileData = []
    if len(cmds) != 3:
        return fileData

    if os.path.exists(cmds[1]):
        fileTarget = cmds[2]
        
        f = open(cmds[1], 'rb').read()
        fileEncoded = base64.b64encode(f)

        fileData.append(fileTarget)
        fileData.append(fileEncoded)
        return fileData

    fileData.append('FILE_NOT_FOUND')
    return fileData

def makeDirIfNotExist(path):
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)

def main():
    facade = FileManageFacade()
    makeDirIfNotExist('client_files')
    makeDirIfNotExist('server_files')

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
        elif cmds[0] == 'get':
            getHelper(facade.get(cmds))
        elif cmds[0] == 'send':
            fileData = sendHelper(cmds)
            printHelper(facade.send(fileData))

def noisy(string):
    print('Noisy:', repr(string))

if __name__ == '__main__':
    main()
