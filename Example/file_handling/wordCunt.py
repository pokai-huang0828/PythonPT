# Example: Count words appear times
#  輸入讀取檔案名稱
#  使用例外處理防止檔案不存在錯誤
#  讀入檔案資料，計算各單字出現次數
#  忽略大小寫差異


with open("song.txt") as f:
    newSong = f.read()

print(newSong)
