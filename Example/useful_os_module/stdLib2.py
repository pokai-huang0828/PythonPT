import os
import shutil

print(os.name)  # 顯示系統名稱 'posix'/'nt'/'ce'/'java'
print(os.getcwd())  # 顯示當前目錄 (cwd)current working directory
os.chdir(r"D:\Learning\Python")  # 切換路徑
print(os.getcwd())  # 顯示當前目錄
print(os.listdir(r"D:\Learning\Python"))  # 列出目錄內容
os.system('mkdir TestingDir')  # 執行系統命令
print(os.listdir(r"D:\Learning\Python"))  # 列出目錄內容


# shutil.copyfile('abc.txt', 'test.txt')  # 檔案複製
# shutil.move('test.txt', r'C:\Python38\tmp')  # 檔案移動
