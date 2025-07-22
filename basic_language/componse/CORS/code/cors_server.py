from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)
# 允许携带 cookies 的 CORS 配置
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])  # 可根据实际前端端口调整

@app.route('/api/data', methods=['GET'])
def get_data():
    resp = make_response(jsonify({"message": "跨域请求成功，已设置cookie！"}))
    resp.set_cookie('token', '123456', httponly=False, samesite='Lax')
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True) 