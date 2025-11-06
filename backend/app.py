from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
flights = [
    {"id": 1, "airline": "IndiGo", "price": 5000},
    {"id": 2, "airline": "Air India", "price": 6500}
]

@app.route('/')
def home():
    return "Travel Booking Backend Running!"

@app.route('/flights', methods=['GET'])
def get_flights():
    return jsonify(flights)

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    return jsonify({"message": "Booking Confirmed!", "data": data}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
