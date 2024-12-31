import re

def optimize_color_scheme(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 定义新的配色方案
    color_scheme = {
        # 深蓝灰色调，给人专业、可靠的感觉
        'primary_color': '#2C3E50',       # 深蓝灰色，用于主要文字和重要元素
        'background_color': '#F5F7FA',    # 浅灰白，柔和的背景
        'navbar_bg': '#34495E',           # 深蓝灰，导航栏背景
        'navbar_text': '#ECF0F1',         # 浅灰白，导航栏文字
        'card_bg': '#FFFFFF',             # 纯白，卡片背景
        'card_border': '#BDC3C7',         # 浅灰色边框
        'accent_color': '#3498DB',        # 明亮的蓝色，用于强调和交互元素
        'footer_bg': '#2C3E50',           # 深蓝灰，页脚背景
        'footer_text': '#ECF0F1'          # 浅灰白，页脚文字
    }
    
    # 新的CSS样式
    new_style = f'''
    <style>
    body {{
        background-color: {color_scheme['background_color']};
        color: {color_scheme['primary_color']};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}

    .navbar {{
        background-color: {color_scheme['navbar_bg']} !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}

    .navbar-brand, .nav-link {{
        color: {color_scheme['navbar_text']} !important;
        transition: color 0.3s ease;
    }}

    .nav-link:hover {{
        color: {color_scheme['accent_color']} !important;
    }}

    .city-header h2 {{
        color: {color_scheme['primary_color']};
        border-bottom: 2px solid {color_scheme['accent_color']};
        padding-bottom: 10px;
    }}

    .city-description {{
        color: {color_scheme['primary_color']};
        opacity: 0.8;
    }}

    .card.attraction-card {{
        background-color: {color_scheme['card_bg']};
        border: 1px solid {color_scheme['card_border']};
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }}

    .card.attraction-card:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }}

    .card-title {{
        color: {color_scheme['primary_color']};
        font-weight: 600;
    }}

    .card-text {{
        color: {color_scheme['primary_color']};
        opacity: 0.8;
    }}

    .site-footer {{
        background-color: {color_scheme['footer_bg']};
        color: {color_scheme['footer_text']};
    }}

    .footer-section h5 {{
        color: {color_scheme['footer_text']};
        border-bottom: 2px solid {color_scheme['accent_color']};
        padding-bottom: 10px;
    }}

    .footer-section a {{
        color: {color_scheme['footer_text']};
        opacity: 0.7;
        transition: opacity 0.3s ease;
    }}

    .footer-section a:hover {{
        opacity: 1;
        color: {color_scheme['accent_color']};
    }}

    #back-to-top {{
        background-color: {color_scheme['accent_color']};
        color: white;
    }}
    </style>
    '''
    
    # 替换或添加样式
    style_pattern = r'<style>.*?</style>'
    if re.search(style_pattern, content, re.DOTALL):
        modified_content = re.sub(style_pattern, new_style, content, flags=re.DOTALL)
    else:
        # 如果没有style标签，就在head中添加
        modified_content = content.replace('</head>', new_style + '</head>')
    
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
        optimize_color_scheme(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
