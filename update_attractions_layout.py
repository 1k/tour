import re

def update_attractions_layout(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找每个城市板块
    city_sections = re.findall(r'(<div class="city-section"[^>]*>.*?</div>)\s*</div>', content, re.DOTALL)
    
    for city_section in city_sections:
        # 在每个城市板块内找到所有景点卡片
        attractions = re.findall(r'(<div class="card attraction-card">.*?</div>)', city_section, re.DOTALL)
        
        if len(attractions) > 0:
            # 用attractions-container包裹景点卡片
            attractions_container = '<div class="attractions-container">' + ''.join(attractions) + '</div>'
            
            # 替换原有的景点卡片
            new_city_section = city_section.replace(''.join(attractions), attractions_container)
            
            # 更新内容
            content = content.replace(city_section, new_city_section)
    
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
        update_attractions_layout(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
