import re

def update_navbar_order(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取城市顺序
    city_order = re.findall(r'<div class="city-section" id="([^"]+)">', content)
    
    # 生成新的导航栏HTML
    navbar_items = [f'<li class="nav-item"><a class="nav-link" href="#{city}">{city}</a></li>' for city in city_order]
    
    # 替换导航栏
    navbar_pattern = r'(<div class="collapse navbar-collapse" id="cityNavbar">\s*<ul class="navbar-nav me-auto mb-2 mb-lg-0">).*?(</ul>\s*</div>)'
    new_navbar = r'\1' + '\n'.join(navbar_items) + r'\2'
    
    modified_content = re.sub(navbar_pattern, new_navbar, content, flags=re.DOTALL)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)

def main():
    html_files = [
        'd:/tour/children-travel-site/index.html',
        'd:/tour/children-travel-site/templates/index.html',
        'd:/tour/children-travel-site/templates/attraction.html',
        'd:/tour/children-travel-site/templates/city.html'
    ]
    
    for file_path in html_files:
        update_navbar_order(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
