import re

def update_color_palette(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义更稳重的配色方案
    color_scheme = {
        'primary_color': '#1A5F7A',       # 深蓝绿色，更加专业和沉稳
        'secondary_color': '#2C7DA0',     # 稍亮的蓝色，作为辅助色
        'background_color': '#F0F4F8',    # 更柔和的浅灰蓝色背景
        'text_color': '#2C3E50',          # 深灰蓝色，保持原有的文字颜色
        'card_border': '#A9B7C0',         # 更柔和的边框颜色
        'navbar_bg': '#2C7DA0',           # 深蓝色导航栏
        'navbar_text': '#FFFFFF',         # 白色文字
        'footer_bg': '#1A5F7A'            # 与主色调一致的页脚背景
    }
    
    # 更新CSS样式
    color_update = f'''
    body {{
        background-color: {color_scheme['background_color']};
    }}

    .navbar {{
        background-color: {color_scheme['navbar_bg']} !important;
    }}

    .navbar-brand, .nav-link {{
        color: {color_scheme['navbar_text']} !important;
    }}

    .nav-link:hover {{
        color: rgba(255,255,255,0.8) !important;
    }}

    .city-header h2 {{
        color: {color_scheme['primary_color']};
        border-bottom: 2px solid {color_scheme['secondary_color']};
    }}

    .card.attraction-card {{
        border: 1px solid {color_scheme['card_border']};
    }}

    .card-title {{
        color: {color_scheme['primary_color']};
    }}

    .site-footer {{
        background-color: {color_scheme['footer_bg']};
        color: white;
    }}

    .footer-section h5 {{
        color: white;
        border-bottom: 2px solid {color_scheme['secondary_color']};
    }}

    .footer-section a {{
        color: rgba(255,255,255,0.8);
    }}

    .footer-section a:hover {{
        color: white;
    }}

    #back-to-top {{
        background-color: {color_scheme['secondary_color']};
    }}
    '''
    
    # 替换现有的颜色定义
    style_pattern = r'(body\s*{[^}]*background-color:)[^;]*;'
    modified_content = re.sub(style_pattern, r'\1 ' + color_scheme['background_color'] + ';', content)
    
    style_pattern = r'(\.navbar\s*{[^}]*background-color:)[^!]*!important;'
    modified_content = re.sub(style_pattern, r'\1 ' + color_scheme['navbar_bg'] + ' !important;', modified_content)
    
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
        update_color_palette(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
