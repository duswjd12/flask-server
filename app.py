from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 서버에 저장된 데이터
data = [
    {"name": "정연정", "dob": "971210", "room": 2, "seat": 23, "exam": 4597},
    {"name": "김현성", "dob": "920826", "room": 4, "seat": 29, "exam": "m7845"},
    {"name": "이승연", "dob": "800318", "room": 4, "seat": 78, "exam": 9810},
    {"name": "김민우", "dob": "860412", "room": 8, "seat": 54, "exam": 7650},
    {"name": "김슬기", "dob": "940420", "room": 5, "seat": 12, "exam": 6454},
    {"name": "이승희", "dob": "951225", "room": 7, "seat": 56, "exam": 6494},
    {"name": "이상혁", "dob": "951226", "room": 8, "seat": 13, "exam": 1485}
]

# 기본 경로
@app.route('/')
def home():
    return "Server is running!"

# 검색 API
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    dob = request.args.get('dob')

    for item in data:
        if item["name"] == name and item["dob"] == dob:
            return jsonify({
                "status": "success",
                "data": {
                    "room": item["room"],
                    "seat": item["seat"],
                    "exam": item["exam"]
                }
            })

    return jsonify({"status": "error", "message": "No matching data found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
