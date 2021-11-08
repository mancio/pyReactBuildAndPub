import subprocess


def build_react(path):
    subprocess.Popen('cd ' + path + ' && ' + 'npm run build', shell=True).wait()
