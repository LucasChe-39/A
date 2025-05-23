import machine
import time
import random

# 設定 GPIO 腳位
led_pin = machine.Pin(12, machine.Pin.OUT)  # LED 腳位
joystick_up_pin = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)  # Joystick 向上方向腳位

def start_game():
    print("ready...")
    wait_time = random.uniform(2, 5)  # 隨機延遲 2 到 5 秒
    time.sleep(wait_time)  
    led_pin.on()  # 點亮 LED

    start_time = time.ticks_ms()  # 記錄開始時間
    print("start...")

    while True:
        joystick_state = joystick_up_pin.value()
        if joystick_state == 0:  # Joystick 向上推動
            reaction_time = time.ticks_diff(time.ticks_ms(), start_time)  # 計算反應時間
            led_pin.off()  # 熄滅 LED
            print("反應時間: {} 毫秒".format(reaction_time))
            break
           
        time.sleep(0.01)  # 防止 CPU 過度佔用

while True:
    input("press Enter to start the game...")
    start_game()
