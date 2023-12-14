import os,shutil

x = os.getcwd()

for i in range(1,10):
    shutil.move(f'{x}\\day{i}',f'{x}\\day0{i}') 
    