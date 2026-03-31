from gpiozero import Robot, OutputDevice

# Bật ENA, ENB liên tục để cấp phép cho L298N
ena = OutputDevice(12)
enb = OutputDevice(18)
ena.on()
enb.on()

# Điều khiển 4 chân IN bằng băm xung PWM
robot = Robot(left=(5, 6), right=(13, 19))

def move(direction):
    if direction == "up":
        robot.forward(0.8) # Chạy 80% công suất
    elif direction == "down":
        robot.backward(0.8)
    elif direction == "left":
        robot.left(0.6)
    elif direction == "right":
        robot.right(0.6)
    else:
        robot.stop()