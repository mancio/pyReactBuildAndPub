import sys
from ftplib import FTP

import argumets
import ftpcom
import react

ftp = FTP()


def run_program():
    par = argumets.argument_builder(sys.argv[1:])
    print('I start to build your react app')
    react.build_react(par["path"])
    print('connect to: ' + par["host"])
    ftpcom.ftp_connect(ftp, par["host"], par["port"], par["user"], par["pass"])
    print('remove static folder')
    ftpcom.ftp_remove_dir(ftp, 'static')
    print('upload files')
    ftpcom.ftp_upload(ftp, par["path"] + '\\build')
    ftp.quit()


if __name__ == '__main__':
    run_program()
