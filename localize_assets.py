import os
import re

def replace_cdn_links(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Bootstrap CSS
    content = re.sub(
        r'https://cdn\.jsdelivr\.net/npm/bootstrap@5\.1\.3/dist/css/bootstrap\.min\.css', 
        'static/css/bootstrap.min.css', 
        content
    )
    
    # Replace Font Awesome CSS
    content = re.sub(
        r'https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/5\.15\.3/css/all\.min\.css', 
        'static/css/all.min.css', 
        content
    )
    
    # Replace Bootstrap JS
    content = re.sub(
        r'https://cdn\.jsdelivr\.net/npm/bootstrap@5\.1\.3/dist/js/bootstrap\.bundle\.min\.js', 
        'static/js/bootstrap.bundle.min.js', 
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
            replace_cdn_links(file_path)
            print(f"Processed {file_path}")

if __name__ == '__main__':
    main()
