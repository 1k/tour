import re

def add_city_navigation_script(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 在最后一个 script 标签之后添加新的 script
    script_pattern = r'(<script src="static/js/bootstrap.bundle.min.js"></script>)(\s*</body>)'
    new_script = r'\1\n    <script src="static/js/city_navigation.js"></script>\2'
    
    modified_content = re.sub(script_pattern, new_script, content)
    
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
        add_city_navigation_script(file_path)
        print(f"处理完成: {file_path}")

if __name__ == '__main__':
    main()
