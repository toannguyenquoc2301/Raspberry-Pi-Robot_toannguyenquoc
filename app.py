from flask import Flask, render_template, Response, request, jsonify
import threading
import datetime
import mysql.connector

import mode
import motor
import camera
import ps4
import esp32gps
import lcd

app = Flask(__name__)

threading.Thread(target=ps4.start_ps4_listener, daemon=True).start()
threading.Thread(target=esp32gps.start_gps_logging, daemon=True).start()
threading.Thread(target=lcd.start_lcd, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gps')
def gps_page():
    return render_template('gps.html')

@app.route('/video_feed')
def video_feed():
    return Response(camera.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/api/status')
def status():
    return jsonify({
        "mode": mode.get_current_mode(),
        "fps": camera.get_fps(),
        "time": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    })

# ======== API MỚI: NHẬN LỆNH CHUYỂN MODE TỪ WEB ========
@app.route('/api/set_mode', methods=['POST'])
def set_mode():
    new_mode = request.json.get('mode')
    if new_mode == "PS4":
        mode.set_mode_ps4()
    elif new_mode == "WEB":
        mode.set_mode_web()
    return jsonify({"status": "ok", "current_mode": mode.get_current_mode()})

@app.route('/api/control', methods=['POST'])
def control():
    if mode.get_current_mode() == "WEB":
        direction = request.json.get('direction', 'stop')
        motor.move(direction)
        return jsonify({"status": "ok"})
    return jsonify({"status": "ignored"}), 403

@app.route('/api/gps_data')
def get_gps():
    db_conn = mysql.connector.connect(**esp32gps.DB_CONFIG)
    cursor = db_conn.cursor(dictionary=True)
    cursor.execute("SELECT lat, lon FROM gps_data ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    db_conn.close()
    
    if row:
        return jsonify(row)
    return jsonify({"lat": 20.962650, "lon": 105.747150})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)