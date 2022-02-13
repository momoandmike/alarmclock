import pygame.mixer
import schedule
import time
import os
import random


# アラーム処理
def alarm():
    print("時間です")
    sound()
    exit()


# 音再生処理
def sound():
    pygame.mixer.init()  # 初期化
    folder = r"C:\Users\momoa\PycharmProjects\day8\alarnclock\alarm"  # 音楽ファイルが格納されたフォルダを指定
    alarmList = os.listdir(folder)
    random.shuffle(alarmList)
    for alarm in alarmList:
        pygame.mixer.music.load("alarm\\" + alarm)
    [{ "alarm": "asadayo_01.wav", "image": "***.jpg"}]
    # pygame.mixer.music.load("C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/asadayo_01.wav")
    # pygame.mixer.music.load("C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/hayakuokite_01.wav")
    # pygame.mixer.music.load("C:/Users/momoa/PycharmProjects/day8/alarnclock/alarm/chikokushichauyo_01.wav")  # 読み込み

    pygame.mixer.music.play(-1)  # ループ再生（引数を1にすると1回のみ再生）
    input()
    pygame.mixer.music.stop()  # 終了


def set_alarm(target):
    # アラーム時間設定
    schedule.every().day.at(target).do(alarm)
    # アラーム待ち
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    # 目覚まし設定時間取得
    print("目覚ましをセットする時間を指定してください")
    hour = input("時間（hour）：")
    minute = input("分（minute）：")
    target = f"{hour.zfill(2)}:{minute.zfill(2)}"
    print(target + "にアラームをセットしました")
    set_alarm(target)


if __name__ == '__main__':
    main()
