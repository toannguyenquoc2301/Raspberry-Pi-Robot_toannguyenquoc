# Raspberry-Pi-Robot_toannguyenquoc
Đề tài : Thiết kế Robot thám hiểm giám sát đa chế độ điều khiển tích hợp định vị GPS sử dụng cloudflare tunnel 
# 🤖 Raspberry Pi Telemetry & Robot Controller

Dự án Hệ thống Điều khiển và Giám sát Robot từ xa (Telemetry) sử dụng Raspberry Pi làm máy chủ trung tâm. Hệ thống hỗ trợ chuyển đổi linh hoạt giữa giao diện Web trực quan và tay cầm PS4, tích hợp truyền phát video trực tiếp và theo dõi tọa độ GPS qua vệ tinh.

## 🌟 Tính năng Nổi bật
* **Dual-Control System:** Chuyển đổi an toàn (Fault-Tolerant) giữa điều khiển bằng Web và tay cầm Bluetooth PS4 với hệ thống ngắt phần cứng (Hardware Interrupts).
* **Real-time Video Streaming:** Truyền phát camera mượt mà với độ trễ thấp qua giao thức MJPEG (`multipart/x-mixed-replace`).
* **GPS Telemetry & Mapping:** Thu thập tọa độ từ ESP32/Module GPS qua Serial, lưu trữ vào MariaDB, và hiển thị tự động trên bản đồ Leaflet/OpenStreetMap.
* **Smooth Navigation:** Ứng dụng băm xung PWM trên mạch L298N để điều tốc động cơ trơn tru, chống trượt bánh khi vào cua.
* **Asynchronous Processing:** Tối ưu hóa hiệu suất CPU Raspberry Pi bằng kiến trúc Đa luồng (Multi-threading) cho các tác vụ nặng như thu thập GPS và giao tiếp tay cầm.
* **On-board HMI:** Hiển thị thông số hệ thống, FPS và Mode trực tiếp lên màn hình LCD 1602 (giao tiếp I2C).

## 🛠️ Công nghệ & Phần cứng sử dụng
* **Backend:** Python 3, Flask, MySQL/MariaDB, Threading.
* **Frontend:** HTML5/CSS3, JavaScript (AJAX Polling), Leaflet.js.
* **Hardware Interfacing:** `gpiozero`, `RPLCD.i2c`, `pyPS4Controller`, `pyserial`.
* **Linh kiện:** Raspberry Pi 5, Mạch công suất L298N ( Hoặc Diver XY 160D ), Màn hình LCD 1602 + Module I2C , Tay cầm PS4 DualShock 4, ESP32 + Module GPS Neo-7M.

## 🚀 Hướng dẫn Cài đặt
1. Clone kho lưu trữ này về Raspberry Pi của bạn:
   `git clone https://github.com/toannguyenquoc2301/Raspberry-Pi-Robot_toannguyenquoc`
2. Cài đặt các thư viện cần thiết:
   `pip install -r requirements.txt`
3. Cấu hình Database MariaDB với cơ sở dữ liệu `robot_db` và bảng `gps_data`.
4. Chạy máy chủ:
   `python3 app.py`
5. Truy cập `http://<IP_CỦA_PI>:5000` trên trình duyệt.
## Sơ đồ nối 
1.Sử dụng 6 chân GPIO để điều khiển độc lập 2 bên bánh xe (Trái và Phải) kèm băm xung tốc độ:
•	L298N IN1 -> Pi 5 GPIO 5 (Tiến bên trái)
•	L298N IN2 -> Pi 5 GPIO 6 (Lùi bên trái)
•	L298N ENA -> Pi 5 GPIO 12 (Băm xung PWM bên trái - Rút Jumper trên L298N)
•	L298N IN3 -> Pi 5 GPIO 13 (Tiến bên phải)
•	L298N IN4 -> Pi 5 GPIO 19 (Lùi bên phải)
•	L298N ENB -> Pi 5 GPIO 18 (Băm xung PWM bên phải - Rút Jumper trên L298N)
•	L298N GND -> Pi 5 GND (Bắt buộc nối chung Mass)
2. Kết nối Khối nút nhấn và Còi báo (Raspberry Pi 5 -> Nút & Buzzer) Sử dụng điện trở kéo lên nội bộ (Internal Pull-up) của Pi 5 để tối giản mạch:
•	Nút nhấn 1 (Mode PS4): Một chân nối GPIO 17, một chân nối GND.
•	Nút nhấn 2 (Mode Web): Một chân nối GPIO 27, một chân nối GND.
•	Còi chip (Active Buzzer): Chân dương (VCC/+) nối GPIO 22, chân âm (-) nối GND.
3. Kết nối Khối Hiển thị (Raspberry Pi 5 -> LCD 1602 I2C) Giao tiếp I2C giúp tiết kiệm chân GPIO:
•	Module I2C VCC -> Pi 5 5V (Chân số 2 hoặc 4)
•	Module I2C GND -> Pi 5 GND
•	Module I2C SDA -> Pi 5 GPIO 2 (SDA)
•	Module I2C SCL -> Pi 5 GPIO 3 (SCL)
4. Kết nối Khối Vị trí (ESP32 -> GPS NEO-7M và Pi 5)
•	ESP32 với GPS NEO-7M: 
o  GPS VCC -> ESP32 3.3V 
o	GPS GND -> ESP32 GND
o	GPS TX -> ESP32 GPIO 16 (RX)
o	GPS RX -> ESP32 GPIO 17 (TX)
•	ESP32 với Raspberry Pi 5: Kết nối trực tiếp qua cáp truyền dữ liệu USB Type-C cắm vào cổng USB của Pi 5.

