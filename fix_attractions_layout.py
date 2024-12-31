import re

def fix_attractions_layout(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义城市板块的正则表达式模式
    city_section_pattern = r'(<div class="city-section"[^>]*>.*?<div class="city-header">.*?</div>)(.*?)(</div>\s*(?=<div class="city-section"|$))'
    
    def wrap_attractions(match):
        city_section_start = match.group(1)
        content_middle = match.group(2)
        city_section_end = match.group(3)
        
        # 检查是否已经有 attractions-container
        if 'attractions-container' not in content_middle:
            # 找出所有的 attraction-card
            attraction_cards = re.findall(r'<div class="card attraction-card">.*?</div>', content_middle, re.DOTALL)
            
            if attraction_cards:
                # 创建新的 attractions-container
                attractions_html = ''.join(attraction_cards)
                new_content_middle = f'\n<div class="attractions-container">{attractions_html}</div>'
                return city_section_start + new_content_middle + city_section_end
        
        return match.group(0)
    
    # 应用包装逻辑
    modified_content = re.sub(city_section_pattern, wrap_attractions, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

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
        fix_attractions_layout(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
