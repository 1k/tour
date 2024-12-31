# 梓航日照游迹・RZUC 博客 🌍

## 项目介绍
这是一个专为记录梓航日照旅行经历而设计的博客网站，展示中国各个城市的精彩景点。网站提供了丰富的景点信息和生动的描述，记录旅行的点点滴滴。

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

### 运行项目
```bash
python app.py
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
