from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 서버에 저장된 데이터
data = [
    {"name": "정연정", "dob": "971210", "room": 2, "seat": 23, "exam": 4597},
    {"name": "이승연", "dob": "800318", "room": 4, "seat": 78, "exam": 9810},
    {"name": "김민우", "dob": "860412", "room": 8, "seat": 54, "exam": 7650},
    {"name": "김슬기", "dob": "940420", "room": 5, "seat": 12, "exam": 6454},
    {"name": "강수현", "dob": "991105", "room": 23, "seat": 1, "exam": "MC001"},
    {"name": "강지수", "dob": "980911", "room": 23, "seat": 2, "exam": "MC002"},
    {"name": "권지현", "dob": "990714", "room": 23, "seat": 3, "exam": "MC003"},
    {"name": "김남준", "dob": "960116", "room": 23, "seat": 4, "exam": "MC004"},
    {"name": "김대규", "dob": "961213", "room": 23, "seat": 5, "exam": "MC005"},
    {"name": "김민우", "dob": "970921", "room": 23, "seat": 6, "exam": "MC006"},
    {"name": "김서원", "dob": "990519", "room": 23, "seat": 7, "exam": "MC007"},
    {"name": "김소은", "dob": "000324", "room": 23, "seat": 8, "exam": "MC008"},
    {"name": "김영우", "dob": "980727", "room": 23, "seat": 9, "exam": "MC009"},
    {"name": "김준홍", "dob": "950725", "room": 23, "seat": 10, "exam": "MC010"},
    {"name": "김지민", "dob": "980310", "room": 23, "seat": 11, "exam": "MC011"},
    {"name": "김지윤", "dob": "981120", "room": 23, "seat": 12, "exam": "MC012"},
    {"name": "김호준", "dob": "980220", "room": 23, "seat": 13, "exam": "MC013"},
    {"name": "남수민", "dob": "000723", "room": 23, "seat": 14, "exam": "MC014"},
    {"name": "류제건", "dob": "960116", "room": 23, "seat": 15, "exam": "MC015"},
    {"name": "류준호", "dob": "980319", "room": 23, "seat": 16, "exam": "MC016"},
    {"name": "문종민", "dob": "961105", "room": 23, "seat": 17, "exam": "MC017"},
    {"name": "소현지", "dob": "001107", "room": 23, "seat": 18, "exam": "MC018"},
    {"name": "손명지", "dob": "000609", "room": 23, "seat": 19, "exam": "MC019"},
    {"name": "손영빈", "dob": "960830", "room": 23, "seat": 20, "exam": "MC020"},
    {"name": "송영주", "dob": "990105", "room": 23, "seat": 21, "exam": "MC021"},
    {"name": "심다은", "dob": "000104", "room": 23, "seat": 22, "exam": "MC022"},
    {"name": "심소연", "dob": "000401", "room": 23, "seat": 23, "exam": "MC023"},
    {"name": "심재강", "dob": "960727", "room": 23, "seat": 24, "exam": "MC024"},
    {"name": "안혜원", "dob": "981030", "room": 23, "seat": 25, "exam": "MC025"},
    {"name": "안홍찬", "dob": "940408", "room": 23, "seat": 26, "exam": "MC026"},
    {"name": "오화랑", "dob": "990120", "room": 24, "seat": 1, "exam": "MC027"},
    {"name": "이금규", "dob": "970321", "room": 24, "seat": 2, "exam": "MC028"},
    {"name": "이상재", "dob": "940307", "room": 24, "seat": 3, "exam": "MC029"},
    {"name": "이서영", "dob": "990325", "room": 24, "seat": 4, "exam": "MC030"},
    {"name": "이수빈", "dob": "010901", "room": 24, "seat": 5, "exam": "MC031"},
    {"name": "이지현", "dob": "000821", "room": 24, "seat": 6, "exam": "MC032"},
    {"name": "이현탁", "dob": "950814", "room": 24, "seat": 7, "exam": "MC033"},
    {"name": "임수완", "dob": "991021", "room": 24, "seat": 8, "exam": "MC034"},
    {"name": "장윤지", "dob": "000111", "room": 24, "seat": 9, "exam": "MC035"},
    {"name": "장재동", "dob": "970401", "room": 24, "seat": 10, "exam": "MC036"},
    {"name": "전인호", "dob": "970929", "room": 24, "seat": 11, "exam": "MC037"},
    {"name": "조상혁", "dob": "960805", "room": 24, "seat": 12, "exam": "MC038"},
    {"name": "조유니", "dob": "000724", "room": 24, "seat": 13, "exam": "MC039"},
    {"name": "조윤성", "dob": "950317", "room": 24, "seat": 14, "exam": "MC040"},
    {"name": "조윤호", "dob": "991215", "room": 24, "seat": 15, "exam": "MC041"},
    {"name": "지민수", "dob": "991209", "room": 24, "seat": 16, "exam": "MC042"},
    {"name": "진민호", "dob": "980101", "room": 24, "seat": 17, "exam": "MC043"},
    {"name": "천상민", "dob": "971212", "room": 24, "seat": 18, "exam": "MC044"},
    {"name": "최도영", "dob": "980514", "room": 24, "seat": 19, "exam": "MC045"},
    {"name": "최무경", "dob": "980410", "room": 24, "seat": 20, "exam": "MC046"},
    {"name": "최찬기", "dob": "980922", "room": 24, "seat": 21, "exam": "MC047"},
    {"name": "하태규", "dob": "980124", "room": 24, "seat": 22, "exam": "MC048"},
    {"name": "한지훈", "dob": "960331", "room": 24, "seat": 23, "exam": "MC049"},
    {"name": "홍준재", "dob": "950111", "room": 24, "seat": 24, "exam": "MC050"}
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
