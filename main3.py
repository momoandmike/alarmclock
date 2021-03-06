import pygame.mixer
import schedule
import time
import random

# アラーム処理
def Alarm():
    print("時間です")
    Sound()
    exit()


# 音再生処理
def Sound():
    pygame.mixer.init()  # 初期化

    alarm_a = "C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/asadayo_01.wav"
    alarm_b = "C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/hayakuokite_01.wav"
    alarm_c = "C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/chikokushichauyo_01.wav"  # 読み込み
    result = random.choice(["alarm_a", "alarm_b", "alarm_c"])
    pygame.mixer.music.load("result")
    pygame.mixer.music.play(-1)  # ループ再生（引数を1にすると1回のみ再生）
    input()
    pygame.mixer.music.stop()  # 終了


# 目覚まし設定時間取得
print("目覚ましをセットする時間を指定してください")
hour = input("時間（hour）：")
minute = input("分（minute）：")
target = f"{hour.zfill(2)}:{minute.zfill(2)}"
print(target + "にアラームをセットしました")

# アラーム時間設定
schedule.every().day.at(target).do(Alarm)

# アラーム待ち
while True:
    schedule.run_pending()
    time.sleep(1)
