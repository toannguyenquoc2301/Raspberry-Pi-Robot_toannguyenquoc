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
* **Linh kiện:** Raspberry Pi (3/4), Mạch công suất L298N, Màn hình LCD 1602 + PCF8574, Tay cầm PS4 DualShock 4, ESP32 + Module GPS Neo-6M.

## 🚀 Hướng dẫn Cài đặt
1. Clone kho lưu trữ này về Raspberry Pi của bạn:
   `git clone https://github.com/TenCuaBan/Robot-Controller-Project.git`
2. Cài đặt các thư viện cần thiết:
   `pip install -r requirements.txt`
3. Cấu hình Database MariaDB với cơ sở dữ liệu `robot_db` và bảng `gps_data`.
4. Chạy máy chủ:
   `python3 app.py`
5. Truy cập `http://<IP_CỦA_PI>:5000` trên trình duyệt.
