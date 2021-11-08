import sys
from ftplib import FTP
import ftpcom
import react

ftp = FTP()

path = sys.argv[1]
host = sys.argv[2]
port = sys.argv[3]
user = sys.argv[4]
pwd = sys.argv[5]


def run_program():
    print('I start to build your react app')
    react.build_react(path)
    print('react built complete')
    ftpcom.ftp_connect(ftp, host, port, user, pwd)
    ftpcom.ftp_remove_dir(ftp, 'static')
    ftpcom.ftp_upload(ftp, path + '\\build')
    ftp.quit()


if __name__ == '__main__':
    run_program()
