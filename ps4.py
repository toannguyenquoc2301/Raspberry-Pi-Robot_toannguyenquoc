from pyPS4Controller.controller import Controller
import motor
import mode

class PS4RobotController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # ==== CHUYỂN MODE BẰNG NÚT BẤM ====
    def on_triangle_press(self):
        # Bấm Tam Giác -> Kích hoạt chế độ PS4
        mode.set_mode_ps4()

    def on_square_press(self):
        # Bấm Vuông -> Kích hoạt chế độ WEB
        mode.set_mode_web()

    # ==== ĐIỀU KHIỂN DI CHUYỂN ====
    def on_up_arrow_press(self):
        if mode.get_current_mode() == "PS4": motor.move("up")

    def on_down_arrow_press(self):
        if mode.get_current_mode() == "PS4": motor.move("down")

    def on_left_arrow_press(self):
        if mode.get_current_mode() == "PS4": motor.move("left")

    def on_right_arrow_press(self):
        if mode.get_current_mode() == "PS4": motor.move("right")

    def on_up_down_arrow_release(self):
        if mode.get_current_mode() == "PS4": motor.move("stop")

    def on_left_right_arrow_release(self):
        if mode.get_current_mode() == "PS4": motor.move("stop")

def start_ps4_listener():
    try:
        controller = PS4RobotController(interface="/dev/input/js0", connecting_using_ds4drv=False)
        controller.listen(timeout=60)
    except:
        print("Chưa kết nối tay cầm PS4.")