#%%
import csv

import overpy
api = overpy.Overpass()
result = api.query("""
    way(44.181073,44.784200,44.468061,45.734029);
    (._;>;);
    out body;
    """)
#
# for way in result.ways:
#     print(way.tags)
with open('coords_canal.csv', 'a+', newline='', encoding="utf8") as csvfile:
    first_line = ["Latitude", "Longitude", "Description", "Label", "Placemark number"]
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(first_line)

    for way in result.ways:
        if way.tags.get('waterway'):
            if way.tags.get('name') == 'канал Караногайская ветвь':
                print("Название канала: %s" % way.tags.get("name", "n/a"))
                print(way.tags)
                print("  Nodes:")
                for node in way.nodes:
                    #writer.writerow([i, i ** 2, "Квадрат числа %d равен %d" % (i, i ** 2)])
                    writer.writerow([node.lat, node.lon])
                # break
            # break



    # if way.tags.get("name", "n/a") == 'канал Караногайская ветвь':
    #     print("Name: %s" % way.tags.get("name", "n/a"))
    #     print("  Highway: %s" % way.tags.get("highway", "n/a"))
    #     print("  Nodes:")
    #
    #     for node in way.nodes:
    #         print("    Lat: %f, Lon: %f" % (node.lat, node.lon))



# with open('coords_canal.csv', 'w', newline='', encoding="utf8") as csvfile:
#     first_line = ["Latitude", "Longitude", "Description", "Label", "Placemark number"]
#     writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writerow(first_line)
#     writer = csv.writer(csvfile,
#                         delimiter=',',
#                         quotechar='"',
#                         quoting=csv.QUOTE_NONNUMERIC)
#     for i in range(10):
#         writer.writerow([i, i ** 2, "Квадрат числа %d равен %d" % (i, i ** 2)])