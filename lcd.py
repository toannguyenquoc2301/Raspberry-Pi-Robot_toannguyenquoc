from RPLCD.i2c import CharLCD
import time
import datetime
import mode
import camera

lcd = CharLCD('PCF8574', 0x27) 

def start_lcd():
    while True:
        lcd.clear()
        now = datetime.datetime.now()
        lcd.write_string(now.strftime("%d/%m/%Y %H:%M\r\n"))
        lcd.write_string(f"Mode:{mode.get_current_mode()} FPS:{camera.get_fps()}")
        time.sleep(1)