import re

def reset_attractions_layout(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 移除所有多余的 attractions-container
    content = re.sub(r'<div class="attractions-container">\s*', '', content)
    content = re.sub(r'\s*</div>\s*</div>', '</div>', content)
    
    # 在每个城市板块后直接添加 attractions-container
    def add_attractions_container(match):
        city_section = match.group(0)
        attractions = re.findall(r'<div class="card attraction-card">.*?</div>', city_section, re.DOTALL)
        
        if attractions:
            attractions_html = ''.join(attractions)
            return city_section + f'\n<div class="attractions-container">{attractions_html}</div>'
        return city_section
    
    content = re.sub(r'<div class="city-section"[^>]*>.*?</div>\s*</div>', add_attractions_container, content, flags=re.DOTALL)
    
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
        reset_attractions_layout(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
