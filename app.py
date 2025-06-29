from flask import Flask, jsonify, request
from event_manager import EventManager

app = Flask(__name__)
manager = EventManager()

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(manager.get_all_events())

@app.route('/events', methods=['POST'])
def create_event():
    data = request.get_json()
    return jsonify(manager.create_event(data)), 201

@app.route('/events/<int:event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.get_json()
    return jsonify(manager.update_event(event_id, data))

@app.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    return jsonify(manager.delete_event(event_id))

if __name__ == '__main__':
    print("✅ Flask server is starting...")
    app.run(debug=True)
