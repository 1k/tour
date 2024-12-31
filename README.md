# 儿童旅行指南 🌍

## 项目介绍
这是一个专为儿童设计的静态旅行网站，展示中国各个城市的精彩景点。网站提供了丰富的景点信息和生动的描述，帮助孩子们了解不同城市的文化和特色。

## 技术栈
- Flask (Python Web框架)
- Frozen-Flask (静态站点生成)
- Bootstrap 5 (响应式前端框架)

## 功能特点
- 展示多个城市的旅游景点
- 每个景点都有详细的描述和图片
- 响应式设计，适配手机和电脑
- 静态站点，加载速度快

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 生成静态站点
```bash
python freeze.py
```

生成的静态文件将位于 `docs` 目录，可以直接部署到 GitHub Pages 或其他静态站点托管服务。

### 本地预览
```bash
# 使用 Python 的内置服务器
python -m http.server 8000 --directory docs
```

## 目录结构
```
children-travel-site/
│
├── app.py               # Flask 应用主文件
├── freeze.py            # 静态站点生成脚本
├── data/
│   └── cities.json      # 城市和景点数据
├── templates/           # HTML 模板
│   ├── index.html
│   ├── city.html
│   └── attraction.html
└── docs/                # 生成的静态站点
```

## 部署
1. 生成静态站点：`python freeze.py`
2. 将 `docs` 目录部署到 GitHub Pages 或其他静态站点托管服务

## 贡献
欢迎提交 issues 和 pull requests！

## 许可证
MIT License
