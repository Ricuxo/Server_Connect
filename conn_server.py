#!/usr/bin/python


from paramiko import SSHClient
import paramiko
import sys

class SSH:
    def __init__(self,host,username,passwd):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host,username=username,password=passwd)

    def exec_cmd(self,host,cmd):
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print (stderr.read())
        else:
            return stdout.read().decode("utf-8")

if __name__ == '__main__':
    host = '192.168.0.150'
    souser = 'root'
    sopass = 'oracle'
    ssh = SSH(host=host, username=souser, passwd=sopass)
    cmd = "yum list"
    sid = ssh.exec_cmd(host, cmd)
    print(sid)
    print(type(sid))
