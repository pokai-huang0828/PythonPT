# Example: Count words appear times
#  輸入讀取檔案名稱
#  使用例外處理防止檔案不存在錯誤
#  讀入檔案資料，計算各單字出現次數
#  忽略大小寫差異
import yaml

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

try:
    with open("exFiles/song.txt") as f:
        newSong = f.read()

    word_dict = {}
    reformatSong = newSong.lower()

    for letter in reformatSong:
        if letter in punctuation:
            reformatSong = reformatSong.replace(letter, "")

    songList = reformatSong.split()

    for word in songList:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    print("單字出現次數: ")
    print(yaml.dump(word_dict))

except Exception as ex:
    print(f"Error message: {ex}")
