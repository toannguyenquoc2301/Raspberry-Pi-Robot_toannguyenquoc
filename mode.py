from gpiozero import Button, Buzzer
import time

# Khởi tạo phần cứng (bounce_time=0.02 là chống dội 20ms)
btn_ps4 = Button(17, bounce_time=0.02) 
btn_web = Button(27, bounce_time=0.02) 
buzzer = Buzzer(22)

CURRENT_MODE = "PS4"

def beep_5_times():
    for _ in range(5):
        buzzer.on()
        time.sleep(0.1)
        buzzer.off()
        time.sleep(0.1)

def set_mode_ps4():
    global CURRENT_MODE
    if CURRENT_MODE != "PS4":
        CURRENT_MODE = "PS4"
        print("Chuyển Mode: PS4")
        beep_5_times()

def set_mode_web():
    global CURRENT_MODE
    if CURRENT_MODE != "WEB":
        CURRENT_MODE = "WEB"
        print("Chuyển Mode: WEB")
        beep_5_times()

# Bắt ngắt trực tiếp (Interrupt)
btn_ps4.when_pressed = set_mode_ps4
btn_web.when_pressed = set_mode_web

def get_current_mode():
    return CURRENT_MODE