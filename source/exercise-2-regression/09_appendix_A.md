(Image_visualization_gee)=

# Appendix A: Image Visualization in GEE

In this appendix, the visualization parameters for an GEE image are addressed.

The [Image Visualization guide in GEE](https://developers.google.com/earth-engine/guides/image_visualization) shows us examples for bands where range values are known.

In this tutorial, **our scale (slope) band image** presents unknown values after the linear fit model is trained.

Thus, we need to compute the minimum and maximum values of an image's band.

```python
reduce_values = trend.select(["scale"])\
              .reduceRegion(reducer = ee.Reducer.percentile([5,95])\
                                        .setOutputs(['min','max']),\
                            geometry = polygon_ee,\
                            scale = 10,\
                            bestEffort = True)
>>> reduce_values.getInfo()
{'scale_max': 0.027822210968628233, 'scale_min': -0.017080171456639426}
```

Min and Max are calculated based on percentile 5 and 95 using a reducer inside a [reduceRegion](https://developers.google.com/earth-engine/apidocs/ee-image-reduceregion).

The computation of **reduce_values** may be intensive. In case you do not receive an answer from GEE, you can increase the value of scale (nominal scale in meters) parameter or set **bestEffort** to False.

Take in consideration that values from our reducer (min and max) are obtained calling the [getInfo method](https://developers.google.com/earth-engine/guides/python_install#printing-objects).
