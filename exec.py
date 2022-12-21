#%%
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

for way in result.ways:

    if way.tags.get('waterway'):
        if way.tags.get('name') == 'канал Караногайская ветвь':
            print("Название канала: %s" % way.tags.get("name", "n/a"))
            print(way.tags)
            print("  Nodes:")

            for node in way.nodes:
                print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
            break



    # if way.tags.get("name", "n/a") == 'канал Караногайская ветвь':
    #     print("Name: %s" % way.tags.get("name", "n/a"))
    #     print("  Highway: %s" % way.tags.get("highway", "n/a"))
    #     print("  Nodes:")
    #
    #     for node in way.nodes:
    #         print("    Lat: %f, Lon: %f" % (node.lat, node.lon))
