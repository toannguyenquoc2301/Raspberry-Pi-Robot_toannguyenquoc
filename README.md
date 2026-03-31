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
