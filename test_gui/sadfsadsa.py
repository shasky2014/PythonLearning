import os
import threading
import traceback
from tkinter import *
from ftplib import FTP


class DownloadFtp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.ftp = FTP()
        self.timeout = 30
        self.port = 21
        self.host = '………………'
        self.user = '……'
        self.password = '……'

    def ftp_connect(self):
        try:
            self.ftp.connect(self.host, self.port, self.timeout)
            self.ftp.login(self.user, self.password)
            text.insert(END, self.ftp.getwelcome() + '\n')
            self.ftp.cwd('……/……')
        except:
            traceback.print_exc()

    def start_download(self):
        self.ftp_connect()
        ftp_list = self.ftp.nlst()
        for name in ftp_list:
            text.insert(END, u'获得文件：' + name.decode('gb2312') + '\n')
            if not os.path.exists('py_auto_download/' + name):
                path = 'py_auto_download/' + name
                f = open(path, 'wb')
                filename = 'RETR ' + name
                text.insert(END, u'正在下载：' + name.decode('gb2312') + '\n')
                self.ftp.retrbinary(filename, f.write)
            else:
                text.insert(END, u'文件或者文件夹已存在，忽略\n')
        self.ftp.quit()


def button_ftp():
    if not os.path.exists('py_auto_download'):
        os.makedirs('py_auto_download')
    my_ftp = DownloadFtp()
    my_ftp.start()
    my_ftp.start_download()


def button_exec_sql():

    pass


if __name__ == '__main__':
    root = Tk()
    root.title(u'自助操作端升级')
    root.geometry('300x400')
    root.resizable(width=False, height=False)
    text = Text(root)
    text.pack(side=TOP)

    frameButton = Frame(root)

    frameLButton = Frame(frameButton)
    buttonESQL = Button(frameLButton, text=u'升级本地SQL数据库', command=button_exec_sql)
    buttonESQL.pack(side=LEFT)
    frameLButton.pack(side=LEFT)

    frameRButton = Frame(frameButton)
    buttonFTP = Button(frameRButton, text=u'下载自助操作端升级包', command=button_ftp)
    buttonFTP.pack(side=RIGHT)
    frameRButton.pack(side=RIGHT)

    frameButton.pack()

    root.mainloop()