# 🤖 Raspberry Pi Telemetry & Robot Controller

Dự án Hệ thống Điều khiển và Giám sát Robot từ xa (Telemetry) sử dụng Raspberry Pi làm máy chủ trung tâm. Hệ thống hỗ trợ chuyển đổi linh hoạt giữa giao diện Web trực quan và tay cầm PS4, tích hợp truyền phát video trực tiếp và theo dõi tọa độ GPS qua vệ tinh.

## 🌟 Tính năng Nổi bật
* **Dual-Control System:** Chuyển đổi an toàn giữa điều khiển bằng Web và tay cầm Bluetooth PS4 với hệ thống ngắt phần cứng.
* **Real-time Video Streaming:** Truyền phát camera mượt mà với độ trễ thấp qua giao thức MJPEG (`multipart/x-mixed-replace`).
* **GPS Telemetry & Mapping:** Thu thập tọa độ từ ESP32/Module GPS qua Serial, lưu trữ vào MariaDB, và hiển thị tự động trên bản đồ Leaflet.
* **Smooth Navigation:** Ứng dụng băm xung PWM trên mạch L298N để điều tốc động cơ trơn tru, chống trượt bánh khi vào cua.
* **Asynchronous Processing:** Tối ưu hóa hiệu suất CPU bằng kiến trúc Đa luồng (Multi-threading).
* **On-board HMI:** Hiển thị thông số hệ thống, FPS và Mode trực tiếp lên màn hình LCD 1602 (giao tiếp I2C).

---

## 📐 Sơ đồ Kiến trúc & Phần cứng

```mermaid
graph TD
    subgraph "Giao tiếp Không dây"
        WEB[Giao diện Web / Smartphone] <-->|Wi-Fi: HTTP / AJAX| PI((Raspberry Pi 3/4\nCentral Hub))
        PS4[Tay cầm PS4 DualShock] <-->|Bluetooth 4.0| PI
    end

    subgraph "Giao diện HMI"
        PI -->|GPIO 17 & 27| BTN[Nút bấm Chuyển Mode]
        PI -->|GPIO 22| BUZ[Còi báo hiệu Buzzer]
        PI -->|I2C (SDA, SCL)| LCD[Màn hình LCD 1602 + PCF8574]
        CAM[Camera Module] -->|CSI / USB| PI
    end

    subgraph "Hệ thống Viễn trắc (Telemetry)"
        GPS[GPS Module NEO-6M] -->|UART| ESP[ESP32 / MCU]
        ESP -->|Cáp USB: /dev/ttyUSB0| PI
        PI <--> DB[(MariaDB/MySQL\nLocal Database)]
    end

    subgraph "Hệ thống Động lực"
        PI -->|PWM & Logic| L298N[Mạch điều khiển L298N]
        L298N --> ML((Động cơ Trái))
        L298N --> MR((Động cơ Phải))
        BATT[Pin Li-Po 12V] --> L298N
    end

    style PI fill:#e63946,stroke:#333,stroke-width:2px,color:#fff
    style DB fill:#457b9d,stroke:#333,stroke-width:2px,color:#fff
    style L298N fill:#2a9d8f,stroke:#333,stroke-width:2px,color:#fff
