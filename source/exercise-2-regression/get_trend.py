import ee
from ee_plugin import Map

divisor = 1000*60*60*24*365


def add_time_band(image):
    return image.addBands(image.metadata("system:time_start").divide(divisor))


def add_ndvi(image):
    ndvi = image.normalizedDifference(["SR_B5", "SR_B4"]).rename("NDVI")
    return image.addBands(ndvi)


roi_layer = QgsProject.instance().mapLayersByName("sao_felix_do_xingu")[0]
roi_geometry = next(roi_layer.getFeatures()).geometry()
points = roi_geometry.asPolygon()[0]
list_vertices = [[i.x(), i.y()] for i in points]
polygon_ee = ee.Geometry.Polygon(list_vertices)

landsat8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2") \
    .filterDate("2017-01-01", "2021-01-01") \
    .filterBounds(polygon_ee) \
    .map(add_ndvi) \
    .map(add_time_band)

trend = landsat8.select(["system:time_start", "NDVI"]) \
    .reduce(ee.Reducer.linearFit())

Map.addLayer(landsat8, {}, "Landsat 8")
Map.addLayer(trend.clip(polygon_ee).select(["scale"]),
             {"min": -0.02782, "max": 0.02782,
              "palette": ["#ff0000", "#ffffbf", "#21ff8e"]},
              "NDVI variation"
             )
