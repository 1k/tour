from flask import Flask, render_template, jsonify, send_from_directory
import json
import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

app = Flask(__name__, static_folder='static')

# 从环境变量获取配置
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'

# 加载城市数据
def load_cities_data():
    with open(os.path.join(os.path.dirname(__file__), 'data', 'cities.json'), 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    cities_data = load_cities_data()
    cities = list(cities_data.keys())
    return render_template('index.html', cities=cities)

@app.route('/city/<city_name>')
def city_page(city_name):
    cities_data = load_cities_data()
    if city_name in cities_data:
        attractions = cities_data[city_name]['attractions']
        return render_template('city.html', city_name=city_name, attractions=attractions)
    return "城市未找到", 404

@app.route('/attraction/<city_name>/<attraction_name>')
def attraction_page(city_name, attraction_name):
    cities_data = load_cities_data()
    if city_name in cities_data:
        for attraction in cities_data[city_name]['attractions']:
            if attraction['name'] == attraction_name:
                return render_template('attraction.html', city_name=city_name, attraction=attraction)
    return "景点未找到", 404

# 静态文件服务
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# 错误处理
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
