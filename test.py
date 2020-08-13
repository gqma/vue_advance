import os

pwd = os.getcwd()
print(pwd)
os.system("cd /d %s") % pwd
