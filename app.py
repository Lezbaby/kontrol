from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Render sunucusu ilk açıldığında botlar varsayılan olarak çalışmaya başlar
global_state = {"status": "RUNNING"} 

@app.route('/')
def index():
    # Telefonundan girdiğinde web arayüzünü yükler
    return render_template('index.html')

@app.route('/api/get_status', methods=['GET'])
def get_status():
    # Sanal makinelerindeki (VM) botların sürekli ping atıp durumu okuyacağı link
    return jsonify(global_state)

@app.route('/api/set_status', methods=['POST'])
def set_status():
    # Sen telefondan butona basınca durumu değiştiren link
    data = request.get_json()
    if data and "status" in data:
        global_state["status"] = data["status"]
        print(f"Durum değiştirildi: {global_state['status']}")
        return jsonify({"success": True, "new_status": global_state["status"]})
    return jsonify({"success": False}), 400

if __name__ == '__main__':
    # Render için gerekli port ayarı
    app.run(host='0.0.0.0', port=10000)