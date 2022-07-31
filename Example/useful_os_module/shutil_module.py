import os
import shutil

#  shutil 模組
#    檔案和目錄管理任務
#        shutil.move(src, dst, copy_function=copy2)：檔案移動或改名
#        shutil.copy(src, dst, *, follow_symlinks=True)：檔案或目錄複製
#        shutil.copyfile(src, dst, *, follow_symlinks=True)：檔案複製
#        shutil.copytree(src, dst, symlinks=False, ignore=None, copy_funct=copy2,
#           ignore_dangling_symlinks=False) ：複製目錄及其目錄內檔案
#        shutil.rmtree(path, ignore_err=False, onerr=None) ：刪除目錄及其內檔案

print(os.getcwd())  # 顯示當前目錄
print(os.listdir(r"D:\Learning\Python"))  # 列出目錄內容

shutil.copyfile('abc.txt', 'test.txt')  # 檔案複製
shutil.move('test.txt', r'D:\Learning\Python')  # 檔案移動
print(os.listdir(r"D:\Learning\Python"))  # 列出目錄內容

# shutil.rmtree(r"D:\Learning\Python")  # 刪除目錄及其內檔案