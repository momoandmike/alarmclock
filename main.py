import pygame.mixer
import schedule
import time
import os
import random
import sys

# 目覚まし設定時間取得
print("目覚ましをセットする時間を指定してください")
hour = input("時間（hour）：")
minute = input("分（minute）：")
target = f"{hour.zfill(2)}:{minute.zfill(2)}"
print(target + "にアラームをセットしました")


# アラーム処理
def Alarm():
    print("時間です")
    # Sound()
    exit()


folder = r"C:\Users\momoa\PycharmProjects\day8\alarnclock\alarm"  # 音楽ファイルが格納されたフォルダを指定
alarmList = os.listdir(folder)
random.shuffle(alarmList)

# 音再生処理
# def Sound():
pygame.mixer.init()

for alarm in alarmList:
    pygame.mixer.music.load("alarm\\" + alarm)  # 読み込み
    pygame.mixer.music.play(1)  # ループ再生（引数を1にすると1回のみ再生）
    input("aaaaa")
    pygame.mixer.music.stop()  # 終了




# アラーム時間設定
schedule.every().day.at(target).do(Alarm)

# アラーム待ち
while True:
    print("aaa")
    schedule.run_pending()
    time.sleep(1)
