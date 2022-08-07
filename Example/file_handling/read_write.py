# 檔案讀取 / 存取

#  mode：檔案開啟模式
#  r：讀取模式開啟，未指定模式時的預設模式
#  w：寫入模式開啟，原檔案內容被覆蓋
#  a：寫入模式開啟，內容附加在原檔案內容之後
#  x：建立新檔案模式，檔案已存在則開啟失敗
#  +：打開磁碟上的檔案進行更新，可讀可寫
#  b：資料以二進位模式存取

poem = '''
你站在橋上看風景
看風景的人在樓上看你
明月裝飾了你的窗子
你裝飾了別人的夢
'''

# try:
#     f = open("output.txt", "x")  # x：建立新檔案模式，檔案已存在則開啟失敗
#     f.write(poem)
#     print("資料填寫至: output.txt")
#     f.flush()
#     f.close()
# except Exception as e:
#     print("資料填寫失敗: ", e)


try:
    with open("exFiles/output2.txt", "a") as f:  # a: 寫入模式開啟，內容附加在原檔案內容之後
        f.write(poem)
    print("資料填寫至: output2.txt")
except Exception as e:
    print("資料填寫失敗: ", e)
