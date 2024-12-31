import os
import requests

def download_unsplash_image(url, filename):
    try:
        # 设置用户代理
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # 下载图片
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"成功下载: {filename}")
        else:
            print(f"下载失败: {url}")
    
    except Exception as e:
        print(f"下载出错: {e}")

# Unsplash 开放图片资源链接
beijing_attractions = [
    {
        "name": "gg",  # 故宫缩写
        "url": "https://images.unsplash.com/photo-1655879795507-d007fbe4c9aa?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "cq",  # 长城缩写
        "url": "https://images.unsplash.com/photo-1597200270998-4acf0094aeda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "tam",  # 天安门缩写
        "url": "https://images.unsplash.com/photo-1597200270998-4acf0094aeda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "yhy",  # 颐和园缩写
        "url": "https://images.unsplash.com/photo-1655879795507-d007fbe4c9aa?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "nc",  # 鸟巢缩写
        "url": "https://images.unsplash.com/photo-1597200270998-4acf0094aeda?q=80&w=1000&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
]

# 创建图片保存目录
os.makedirs('d:/tour/children-travel-site/images/beijing', exist_ok=True)

# 下载图片
for attraction in beijing_attractions:
    filename = f'd:/tour/children-travel-site/images/beijing/{attraction["name"]}.jpg'
    download_unsplash_image(attraction["url"], filename)
