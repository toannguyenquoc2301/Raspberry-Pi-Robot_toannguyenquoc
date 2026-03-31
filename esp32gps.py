import serial
import time
import mysql.connector

# Bỏ qua mật khẩu, dùng user mặc định hoặc rỗng tùy cấu hình MariaDB của Pi
DB_CONFIG = {
    'host': 'localhost',
    'database': 'robot_db',
    'user': 'root',
    'password': ''
}

def start_gps_logging():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)
        db_conn = mysql.connector.connect(**DB_CONFIG)
        cursor = db_conn.cursor()
        
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                if "," in line:
                    try:
                        lat, lon = line.split(",")
                        sql = "INSERT INTO gps_data (lat, lon) VALUES (%s, %s)"
                        cursor.execute(sql, (float(lat), float(lon)))
                        db_conn.commit()
                    except ValueError:
                        pass
            time.sleep(0.5)
    except Exception as e:
        print(f"Lỗi GPS Logging: {e}")