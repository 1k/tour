import re

def update_style(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_style = '''    <style>
    
        :root {
            --primary-color: #34495E;  /* 深蓝灰色 */
            --secondary-color: #4A6D7C; /* 柔和的蓝灰色 */
            --background-color: #F5F7F9; /* 浅灰白 */
            --text-color: #2C3E50; /* 深灰蓝 */
            --card-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
        }

        * {
            box-sizing: border-box;
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
            box-shadow: 0 2px 5px rgba(0,0,0,0.08);
            height: 60px;
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
        }

        .city-section {
            background-color: white;
            margin-bottom: 20px;
            padding: 20px;
            border-radius: 8px;
            box-shadow: var(--card-shadow);
        }

        .attractions-container {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 15px;
        }

        .attraction-card {
            margin-bottom: 15px;
            border: none;
            box-shadow: var(--card-shadow);
            transition: transform 0.3s ease;
        }

        .attraction-card:hover {
            transform: scale(1.03);
        }

        .attraction-card .card-img-top {
            height: 200px;
            object-fit: cover;
        }

        .attraction-card .card-body {
            padding: 15px;
        }

        .attraction-card .card-title {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .attraction-card .card-text {
            font-size: 0.9rem;
            color: var(--secondary-color);
        }
    </style>'''
    
    # 替换原有的 <style> 块
    content = re.sub(r'<style>.*?</style>', new_style, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    html_files = [
        'd:/tour/children-travel-site/index.html',
        'd:/tour/children-travel-site/templates/index.html',
        'd:/tour/children-travel-site/templates/attraction.html',
        'd:/tour/children-travel-site/templates/city.html',
        'd:/tour/children-travel-site/templates/500.html',
        'd:/tour/children-travel-site/templates/404.html'
    ]
    
    for file_path in html_files:
        update_style(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
