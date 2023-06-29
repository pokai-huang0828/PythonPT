import time
import pyautogui
import subprocess

# 打开游戏
game_path = "D:\\Program Files\\Steam\\steamapps\\common\\NBA 2K23\\NBA2K23.exe"  # 替换为您的游戏路径
subprocess.Popen(game_path)

# 等待游戏启动并加载
time.sleep(60)  # 这里等待60秒钟，让游戏完全加载

# 进入 MyCareer 模式
pyautogui.moveTo(1000, 600)  # 替换为您需要点击的屏幕坐标
pyautogui.click()
time.sleep(1)
pyautogui.moveTo(1200, 700)  # 替换为您需要点击的屏幕坐标
pyautogui.click()

# 创建角色
pyautogui.moveTo(800, 500)  # 替换为您需要点击的屏幕坐标
pyautogui.click()
time.sleep(1)
pyautogui.typewrite("Player Name")  # 替换为您的球员名称
pyautogui.moveTo(1000, 600)  # 替换为您需要点击的屏幕坐标
pyautogui.click()

# 开始比赛
pyautogui.moveTo(1200, 700)  # 替换为您需要点击的屏幕坐标
pyautogui.click()