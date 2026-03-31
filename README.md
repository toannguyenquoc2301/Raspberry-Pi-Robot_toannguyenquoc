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
## 📐 Sơ đồ Kiến trúc & Kết nối Hệ thống
Dưới đây là bảng nối dây tiêu chuẩn (BCM) giữa Raspberry Pi và các module :

| Thiết bị / Module | Chân trên Module | Chân trên Raspberry Pi (BCM) | Ghi chú |
| :--- | :--- | :--- | :--- |
| **Mạch L298N** | ENA (Băm xung Trái) | `GPIO 12` | Bắt buộc tháo Jumper |
| | ENB (Băm xung Phải) | `GPIO 18` | Bắt buộc tháo Jumper |
| | IN1, IN2 (Chiều quay Trái) | `GPIO 5`, `GPIO 6` | |
| | IN3, IN4 (Chiều quay Phải) | `GPIO 13`, `GPIO 19` | |
| **Màn hình LCD** | SDA (Dữ liệu I2C) | `SDA (GPIO 2)` | Kèm module PCF8574 |
| | SCL (Xung nhịp I2C) | `SCL (GPIO 3)` | |
| **Nút bấm & Còi** | Nút PS4 Mode | `GPIO 17` | Kéo xuống GND (Pull-down) |
| | Nút WEB Mode | `GPIO 27` | Kéo xuống GND (Pull-down) |
| | Còi Buzzer (VCC) | `GPIO 22` | |
| **GPS (ESP32)** | Cổng USB / TX-RX | Cổng USB của Pi | Nhận dạng là `/dev/ttyUSB0`
•	Module I2C SDA -> Pi 5 GPIO 2 (SDA)
•	Module I2C SCL -> Pi 5 GPIO 3 (SCL)
4. Kết nối Khối Vị trí (ESP32 -> GPS NEO-7M và Pi 5)
•	ESP32 với GPS NEO-7M: 
o  GPS VCC -> ESP32 3.3V 
o	GPS GND -> ESP32 GND
o	GPS TX -> ESP32 GPIO 16 (RX)
o	GPS RX -> ESP32 GPIO 17 (TX)
•	ESP32 với Raspberry Pi 5: Kết nối trực tiếp qua cáp truyền dữ liệu USB Type-C cắm vào cổng USB của Pi 5.
## 🔌 Bảng Kết Nối Chân (Pinout Mapping)

Dưới đây là bảng nối dây tiêu chuẩn (BCM) giữa Raspberry Pi và các module dựa trên mã nguồn:

| Thiết bị / Module | Chân trên Module | Chân trên Raspberry Pi (BCM) | Ghi chú |
| :--- | :--- | :--- | :--- |
| **Mạch L298N** | ENA (Băm xung Trái) | `GPIO 12` | Bắt buộc tháo Jumper |
| | ENB (Băm xung Phải) | `GPIO 18` | Bắt buộc tháo Jumper |
| | IN1, IN2 (Chiều quay Trái) | `GPIO 5`, `GPIO 6` | |
| | IN3, IN4 (Chiều quay Phải) | `GPIO 13`, `GPIO 19` | |
| **Màn hình LCD** | SDA (Dữ liệu I2C) | `SDA (GPIO 2)` | Kèm module PCF8574 |
| | SCL (Xung nhịp I2C) | `SCL (GPIO 3)` | |
| **Nút bấm & Còi** | Nút PS4 Mode | `GPIO 17` | Kéo xuống GND (Pull-down) |
| | Nút WEB Mode | `GPIO 27` | Kéo xuống GND (Pull-down) |
| | Còi Buzzer (VCC) | `GPIO 22` | |
| **GPS (ESP32)** | Cổng USB / TX-RX | Cổng USB của Pi | Nhận dạng là `/dev/ttyUSB0` |
