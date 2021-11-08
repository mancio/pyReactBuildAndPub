import os
from ftplib import error_perm


def ftp_connect(ftp, host, port, user, pwd):
    ftp.connect(host, port)
    ftp.login(user, pwd)


def ftp_remove_dir(ftp, path):
    try:
        for (name, properties) in ftp.mlsd(path=path):
            currentpath = f"{path}/{name}"
            if name in ['.', '..']:
                continue
            elif properties['type'] == 'file':
                print('file: ' + name + ' deleted')
                ftp.delete(currentpath)
            elif properties['type'] == 'dir':
                ftp_remove_dir(ftp, currentpath)

        ftp.rmd(path)
        print('removed: ' + path)

    except Exception as inst:
        print(type(inst))
        print(inst.args)


def ftp_upload(ftp, path):
    for name in os.listdir(path):
        localpath = os.path.join(path, name)
        if os.path.isfile(localpath):
            print("STOR", name, localpath)
            ftp.storbinary('STOR ' + name, open(localpath, 'rb'))
        elif os.path.isdir(localpath):
            print("MKD", name)

            try:
                ftp.mkd(name)

            # ignore "directory already exists"
            except error_perm as e:
                if not e.args[0].startswith('550'):
                    raise

            print("CWD", name)
            ftp.cwd(name)
            ftp_upload(ftp, localpath)
            print("CWD", "..")
            ftp.cwd("../")


