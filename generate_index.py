import json
import os
import base64

def generate_placeholder_image(width=300, height=200):
    """生成base64编码的占位图"""
    # 直接返回一个简单的base64编码的灰色图片
    return "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="

def generate_static_index():
    # 城市数据
    cities_data = json.load(open('data/cities.json', 'r', encoding='utf-8'))
    
    # 城市简介（可以根据实际情况调整）
    city_descriptions = {
        # 重新定义北京、上海、成都的描述
        "北京": "古都风采，长城故宫，千年文明，现代活力。",
        "上海": "魔都风情，外滩浦东，中西合璧，国际大都市。",
        "成都": "熊猫故乡，美食天堂，慢生活，巴蜀文化。",
        
        # 其他城市描述保持不变
        "苏州": "园林之城，水乡风情，园林精致，古韵悠长。",
        "无锡": "太湖之滨，灵山大佛，江南水乡的诗意栖居。",
        "常州": "恐龙主题公园，历史文化名城，充满童趣。",
        "南京": "古都风采，秦淮河畔，中山陵，历史文化底蕴深厚。",
        "杭州": "西湖美景，运河文化，诗画江南，休闲胜地。",
        "武汉": "长江之滨，黄鹤楼，三镇风情，历史与现代交融。",
        "广州": "南国商都，沙面风情，美食天堂，岭南文化中心。",
        "深圳": "改革开放前沿，科技创新之城，现代都市魅力。",
        "重庆": "山城魅力，长江三峡，巴渝文化，立体城市。",
        "西安": "古都风采，兵马俑，丝绸之路起点，历史文明之城。",
        
        # 之前的新增城市描述
        "青岛": "海滨城市，啤酒之都，海鲜美食，欧陆风情。",
        "济南": "泉城风光，大明湖畔，泉水之城，历史文化名城。",
        "大连": "海港城市，俄式风情，海洋公园，滨海风光。",
        
        # 其他城市描述
        "南通": "长江之滨，近代工业发源地，江海交汇处。",
        "武汉": "长江中游城市，黄鹤楼，三镇风情，历史与现代交融。",
        "郑州": "黄河文化发源地，中原腹地，现代化新兴城市。",
        "石家庄": "华北平原中心，近代工业重镇，现代化省会城市。",
        "太原": "晋商文化发源地，煤炭工业中心，山西省省会。",
        "呼和浩特": "草原风情，民族文化，内蒙古自治区首府。",
        "沈阳": "东北老工业基地，历史文化名城，现代化大都市。",
        "长春": "汽车工业之都，电影之都，东北重要城市。",
        "哈尔滨": "冰雪之城，俄式建筑，中国北方风情。",
        "合肥": "安徽省省会，科技创新中心，现代化城市。",
        "福州": "闽江之滨，海峡西岸经济区中心，历史文化名城。",
        "厦门": "海上花园城市，经济特区，现代化国际港口城市。",
        "南昌": "八一起义发源地，江西省省会，红色文化中心。",
        "长沙": "湖南省省会，毛泽东故乡，历史文化名城。",
        "海口": "海南省省会，热带滨海度假城市，国际旅游目的地。",
        "贵阳": "山水之城，生态文明示范区，黔中高原明珠。",
        "昆明": "春城，滇池之滨，多民族文化交汇处。",
        "兰州": "丝绸之路黄金段起点，甘肃省省会，西部重要城市。",
        
        # 之前添加的新城市描述
        "徐州": "汉楚文化交汇地，云龙湖畔，历史文化名城。",
        "潍坊": "风筝之乡，民俗文化，现代化工业城市。",
        "淮安": "水城风情，淮扬文化，运河古城，诗意栖居。",
        "枣庄": "矿业文化发源地，山东运河文化中心。",
        "连云港": "海滨城市，丝绸之路海上起点，现代港口。",
        "淄博": "陶瓷文化之都，齐文化发源地，工业重镇。",
        "扬州": "园林之城，瘦西湖，盐商文化，江南韵味。"
    }

    # 生成占位图
    placeholder_image = generate_placeholder_image()

    # 按照城市名称的字母顺序排序城市
    sorted_cities = sorted(cities_data.keys())
    
    # 生成城市导航栏
    city_nav_items = f'''
    <div class="container-fluid px-3">
        <a class="navbar-brand" href="#">🌈 儿童旅行指南</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#cityNavbar">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="cityNavbar">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                {"".join([f'<li class="nav-item"><a class="nav-link" href="#{city}">{city}</a></li>' for city in sorted_cities])}
            </ul>
        </div>
    </div>
    '''

    # 生成每个城市的景点卡片
    city_content = ''
    for city, city_info in cities_data.items():
        attractions_cards = []
        for attraction in city_info['attractions']:
            card = f'''
            <div class="card attraction-card">
                <img src="{attraction.get('image', placeholder_image)}" class="card-img-top" alt="{attraction['name']}">
                <div class="card-body">
                    <h5 class="card-title">{attraction['name']}</h5>
                    <p class="card-text">{attraction['description']}</p>
                </div>
            </div>
            '''
            attractions_cards.append(card)

        # 城市内容区域
        city_content += f'''
            <div class="city-section" id="{city}">
                <div class="city-header">
                    <h2>{city}</h2>
                    <div class="city-description">{city_descriptions.get(city, "精彩城市，等待探索！")}</div>
                </div>
                <div class="attractions-container">
                    {''.join(attractions_cards)}
                </div>
            </div>'''

    # HTML 模板
    base_css = '''
        :root {
            --primary-color: #4CAF50;
            --secondary-color: #2196F3;
            --background-color: #F0F4F8;
            --text-color: #333;
            --card-shadow: 0 4px 8px rgba(0, 0, 0, 0.06);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Noto Sans SC', sans-serif;
            background-color: var(--background-color);
            color: var(--text-color);
            line-height: 1.4;
            padding-top: 60px;
        }

        .navbar {
            background-color: white;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            padding: 5px 0;
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
        }

        .navbar-brand {
            font-weight: 700;
            color: var(--primary-color) !important;
            font-size: 1.2rem;
        }

        .nav-link {
            color: var(--text-color);
            font-weight: 500;
            font-size: 0.9rem;
            padding: 5px 10px !important;
        }

        .city-section {
            background-color: white;
            margin-bottom: 10px;
            box-shadow: var(--card-shadow);
            padding: 15px;
        }

        .city-header {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .city-header h2 {
            margin: 0;
            margin-right: 15px;
            color: var(--primary-color);
            font-size: 1.5rem;
        }

        .city-description {
            color: #6c757d;
            font-size: 0.9rem;
        }

        .attractions-container {
            display: flex;
            overflow-x: auto;
            gap: 10px;
            padding-bottom: 10px;
        }

        .attractions-container::-webkit-scrollbar {
            height: 6px;
        }

        .attractions-container::-webkit-scrollbar-thumb {
            background-color: rgba(0,0,0,0.2);
            border-radius: 3px;
        }

        .attraction-card {
            flex: 0 0 auto;
            width: 200px;
            border: none;
            transition: transform 0.2s ease;
        }

        .attraction-card:hover {
            transform: scale(1.05);
        }

        .attraction-card img {
            height: 150px;
            object-fit: cover;
            border-radius: 8px;
        }

        .attraction-card .card-body {
            padding: 10px;
            text-align: center;
        }

        .attraction-card .card-title {
            font-size: 0.9rem;
            margin-bottom: 5px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        .attraction-card .card-text {
            font-size: 0.8rem;
            color: #6c757d;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }
    '''
    custom_css = '''
        /* 渐变背景 */
        body {
            background: linear-gradient(135deg, #f6f8f9 0%, #e5ebee 100%);
            background-attachment: fixed;
        }

        /* 导航栏优化 */
        .navbar {
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .navbar-brand {
            color: white !important;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }
        .nav-link {
            color: rgba(255,255,255,0.8) !important;
            transition: all 0.3s ease;
            position: relative;
        }
        .nav-link:hover {
            color: white !important;
            transform: scale(1.05);
        }
        .nav-link::after {
            content: '';
            position: absolute;
            width: 0;
            height: 2px;
            bottom: -5px;
            left: 50%;
            background-color: white;
            transition: all 0.3s ease;
        }
        .nav-link:hover::after {
            width: 100%;
            left: 0;
        }

        /* 城市区块优化 */
        .city-section {
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            overflow: hidden;
            transition: all 0.3s ease;
            position: relative;
            padding: 20px;
        }
        .city-section::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: linear-gradient(to right, #4facfe 0%, #00f2fe 100%);
        }
        .city-section:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }

        /* 景点卡片优化 */
        .attractions-container {
            display: flex;
            gap: 10px;
            padding: 10px 0;
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: thin;
            scrollbar-color: #4facfe #e0e0e0;
        }
        .attractions-container::-webkit-scrollbar {
            height: 8px;
        }
        .attractions-container::-webkit-scrollbar-track {
            background: #f1f1f1;
        }
        .attractions-container::-webkit-scrollbar-thumb {
            background: #4facfe;
            border-radius: 4px;
        }
        .attraction-card {
            width: 220px;
            min-width: 220px;
            flex-shrink: 0;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            border: none;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            display: inline-block;
        }
        .attraction-card img {
            height: 180px;
            width: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }
        .attraction-card .card-body {
            padding: 10px;
            height: 200px;
            display: flex;
            flex-direction: column;
        }
        .attraction-card .card-title {
            font-weight: bold;
            font-size: 0.95rem;
            color: #4facfe;
            margin-bottom: 5px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .attraction-card .card-text {
            font-size: 0.85rem;
            color: #666;
            line-height: 1.5;
            overflow: hidden;
            text-overflow: ellipsis;
            display: -webkit-box;
            -webkit-line-clamp: 4;
            -webkit-box-orient: vertical;
        }
        .attraction-card:hover {
            transform: scale(1.05);
            box-shadow: 0 8px 15px rgba(0,0,0,0.15);
        }
        .attraction-card:hover img {
            transform: scale(1.1);
        }

        /* 响应式调整 */
        @media (max-width: 1200px) {
            .attraction-card {
                width: 200px;
                min-width: 200px;
            }
        }
        @media (max-width: 992px) {
            .attraction-card {
                width: 180px;
                min-width: 180px;
            }
        }
        @media (max-width: 768px) {
            .attraction-card {
                width: 160px;
                min-width: 160px;
            }
        }

        /* 页脚优化 */
        .site-footer {
            background: linear-gradient(135deg, #f6f8f9 0%, #e5ebee 100%);
            border-top: 3px solid #4facfe;
            padding: 40px 0;
            color: #333;
        }
        .site-footer .container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
        }
        .footer-section {
            text-align: left;
            padding: 0 15px;
        }
        .footer-section h5 {
            color: #4facfe;
            position: relative;
            padding-bottom: 10px;
            margin-bottom: 15px;
            font-weight: bold;
            border-bottom: 2px solid #4facfe;
        }
        .footer-section ul {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .footer-section ul li {
            margin-bottom: 8px;
        }
        .footer-section ul li a {
            color: #666;
            text-decoration: none;
            transition: color 0.3s, transform 0.2s;
            display: inline-block;
        }
        .footer-section ul li a:hover {
            color: #4facfe;
            transform: translateX(5px);
        }
        .footer-bottom {
            background-color: rgba(0,0,0,0.05);
            padding: 15px 0;
            text-align: center;
            color: #6c757d;
            border-top: 1px solid rgba(0,0,0,0.1);
            font-size: 0.9rem;
        }

        /* 响应式适配 */
        @media (max-width: 992px) {
            .site-footer .container {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 576px) {
            .site-footer .container {
                grid-template-columns: 1fr;
            }
            .footer-section {
                text-align: center;
            }
            .footer-section h5 {
                text-align: center;
                border-bottom: 2px solid #4facfe;
                display: inline-block;
                padding-bottom: 5px;
                margin: 0 auto 15px;
            }
            .footer-section ul {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
        }

        /* 返回顶部按钮优化 */
        #back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            display: none;
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
            color: white;
            border-radius: 50%;
            border: 2px solid rgba(255,255,255,0.3);
            outline: none;
            cursor: pointer;
            z-index: 1050;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0.8;
        }

        #back-to-top i {
            font-size: 24px;
            transition: transform 0.3s ease;
        }

        #back-to-top:hover {
            opacity: 1;
            transform: translateY(-10px);
            background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
            box-shadow: 0 12px 25px rgba(0,0,0,0.3);
        }

        #back-to-top:hover i {
            transform: scale(1.2) rotate(360deg);
        }

        /* 返回顶部按钮呼吸动画 */
        @keyframes breathe {
            0%, 100% { 
                transform: scale(1) translateY(0); 
                box-shadow: 0 8px 20px rgba(0,0,0,0.2);
            }
            50% { 
                transform: scale(1.05) translateY(-5px); 
                box-shadow: 0 12px 25px rgba(0,0,0,0.3);
            }
        }

        #back-to-top.show {
            display: flex;
            animation: breathe 2s infinite;
        }

        /* 响应式适配 */
        @media (max-width: 768px) {
            #back-to-top {
                width: 45px;
                height: 45px;
                bottom: 20px;
                right: 20px;
            }
            #back-to-top i {
                font-size: 20px;
            }
        }
    '''
    back_to_top_js = '''
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var backToTopButton = document.getElementById('back-to-top');
        
        // 显示/隐藏返回顶部按钮
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('show');
            } else {
                backToTopButton.classList.remove('show');
            }
        });
        
        // 点击返回顶部
        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    });
    </script>
    '''
    html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>中国儿童旅游网</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" rel="stylesheet">
    <style>
    {base_css}
    {custom_css}
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light fixed-top">
        {city_nav_items}
    </nav>
    
    <div class="container-fluid px-3 mt-3">
        {city_content}
    </div>
    
    <button id="back-to-top" title="返回顶部">
        <i class="fas fa-arrow-up"></i>
    </button>
    
    {back_to_top_js}
    
    <footer class="site-footer">
        <div class="container">
            <div class="footer-section">
                <h5>关于我们</h5>
                <ul>
                    <li><a href="#">网站简介</a></li>
                    <li><a href="#">团队介绍</a></li>
                    <li><a href="#">联系方式</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h5>旅游资源</h5>
                <ul>
                    <li><a href="#">城市导航</a></li>
                    <li><a href="#">景点推荐</a></li>
                    <li><a href="#">旅游攻略</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h5>用户服务</h5>
                <ul>
                    <li><a href="#">常见问题</a></li>
                    <li><a href="#">意见反馈</a></li>
                    <li><a href="#">隐私政策</a></li>
                </ul>
            </div>
            <div class="footer-section">
                <h5>关注我们</h5>
                <ul>
                    <li><a href="#">微信公众号</a></li>
                    <li><a href="#">微博</a></li>
                    <li><a href="#">抖音</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            &copy; 2024 儿童旅游网. 版权所有 | 京ICP备12345678号
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

    # 保存为静态 HTML
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_template)

    print("静态页面生成完成：index.html")

if __name__ == '__main__':
    generate_static_index()
