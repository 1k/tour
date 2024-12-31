from flask_frozen import Freezer
from app import app
import os

# 配置输出目录
app.config['FREEZER_DESTINATION'] = 'docs'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_STATIC_FILES'] = False

freezer = Freezer(app)

@freezer.register_generator
def city_pages():
    cities_data = app.load_cities_data()
    for city_name in cities_data.keys():
        yield {'city_name': city_name}

@freezer.register_generator
def attraction_pages():
    cities_data = app.load_cities_data()
    for city_name, city_data in cities_data.items():
        for attraction in city_data['attractions']:
            yield {
                'city_name': city_name, 
                'attraction_name': attraction['name']
            }

if __name__ == '__main__':
    freezer.freeze()
