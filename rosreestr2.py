from rosreestr2coord import Area
import json
import csv

area = Area("05:06:000033:625")
# аргументы
#   code='' - кадастровый номер участка
#   area_type=1 - тип площади
#   epsilon=5 - точность аппроксимации
#   media_path='' - путь для временных файлов
#   with_log=True - логирование
#   coord_out='EPSG:4326' - или EPSG:3857 (будет удалена в последующих версиях)
#   center_only=False - экспорт координат центров участка
#   with_proxy=False - запросы через прокси
#   use_cache=True - использовать кэширование запросов

x = area.to_geojson()
print(x)
x = json.loads(x)
print(x)
with open('ground.csv', 'w', newline='', encoding="utf8") as csvfile:
    first_line = ["Latitude", "Longitude", "Description", "Label", "Placemark number"]
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(first_line)
    for coord in range(len(x['features'])):
        coord_lon, coord_lat = x['features'][coord]['geometry']['coordinates']
        writer.writerow([coord_lat, coord_lon])


