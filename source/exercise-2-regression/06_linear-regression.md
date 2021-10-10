# Linear Regression

After understanding a bit more about the GEE plugin, we can start writting our final code.

The NDVI variation will be modeled as a linear fit.

The data should be set up as a two-band input image, where the independent variable band is _time_ and the dependent variable band is _NDVI_.

## Adding bands

In our collection **"LANDSAT/LC08/C02/T1_L2"**, the band names for B5 and B4 are `SR_B5` and `SR_B4`.

Using [the explained procedure to add bands in our collections](Add_bands), we define the functions `add_time_band` and `add_ndvi` to generate the inputs for our regression.

```{literalinclude} get_trend.py
---
language: python
lines: 4-13
---
```

[Google Earth Engine suggests us to scale milliseconds by a large constant](https://developers.google.com/earth-engine/guides/reducers_regression) to avoid very small slopes in the linear regression output. In this case, **divisor** is a constant conversion between milliseconds and 1 year.

## Generating GEE Polygon from ROI

Convert our region of interest into google earth engine polygon (explained in [Data transfer between Layer to GEE plugin](Data_pyqgis_gee)).

```{literalinclude} get_trend.py
---
language: python
lines: 16-20
---
```

## Generating Landsat 8 collection of ROI

- The analyzed data is from 2017 to 2021. The [filterDate](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-filterdate) function filters a collection by a date range.
- [filterBounds](https://developers.google.com/earth-engine/apidocs/ee-imagecollection-filterbounds?hl=en) function filters a collection by intersection with geometry (our region of interest). It is part of [coding best practices that are intended to maximize the chance of success for complex or expensive Earth Engine computations](https://developers.google.com/earth-engine/guides/best_practices).
- Our collection adds the bands `system:time_start` and `NDVI` through the functions: **add_time_band** and **add_ndvi**.

```{literalinclude} get_trend.py
---
language: python
lines: 22-26
---
```

## Applying Linear Fit Regression

In our case, the inputs bands are:

1. "system:time_start" (independent variable)
2. "NDVI" (dependent variable)

```{literalinclude} get_trend.py
---
language: python
lines: 28-29
---
```

The linear fit is applied through the reducer [ee.Reducer.linearFit()](https://developers.google.com/earth-engine/apidocs/ee-reducer-linearfit?hl=en) and saved in the variable **trend**.
This model calculates the slope (scale in the GEE terminology) and offset.

Other reducers are also available in GEE:

- ee.Reducer.linearRegression()
- ee.Reducer.robustLinearRegression()
- ee.Reducer.ridgeRegression()

For more information, check [this link](https://developers.google.com/earth-engine/guides/reducers_regression?hl=en).

## Visualization

[Map.addLayer](https://developers.google.com/earth-engine/apidocs/map-addlayer) let us add a given EE object to the map as a layer.
To use it, we need to import **Map** from **ee_plugin**:

```python
from ee_plugin import Map
```

For example, the **Landsat8** variable contains the image collection that covers our region of interest from 2017 to 2020.

```{literalinclude} get_trend.py
---
language: python
lines: 31
---
```

```{eval-rst}
.. figure:: ../_static/img_ex2/landsat8_roi_bounds.png
  :width: 600px
```

Now it is time to plot the slope (**scale** in Google Earth Engine terminology) of the linear regression:

- The linear fit model is clipped by our region of interest
- The parameters of image visualization (min, max) are detailed in [Appendix A](Image_visualization_gee).

```{literalinclude} get_trend.py
---
language: python
lines: 32-36
---
```

```{eval-rst}
.. figure:: ../_static/img_ex2/lr_roi.png
  :width: 600px
```

In summary, the final code used is:

```{literalinclude} get_trend.py
---
language: python
lineno-start: 1
---
```
