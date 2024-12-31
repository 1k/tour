import os
import re

def update_fontawesome_path(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 更新Font Awesome的CSS路径
    content = re.sub(
        r'href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/5\.15\.3/css/all\.min\.css"', 
        'href="static/css/all.min.css"', 
        content
    )
    
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
        if os.path.exists(file_path):
            update_fontawesome_path(file_path)
            print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
