# Google Earth Engine Elements

In order to familiarize ourselves with the elements used in Google Earth Engine, we will use the **GEE Timeseries Explorer** plugin.

Go to **`View / Panels / GEE Timseries Explorer (v1.1)`**, we will analyze the 3 sampled points from Layer `points`: P1, P2 and P3.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_overview.png
  :width: 700px
```

Now, we will inspect some elements from GEE Timeseries Explorer:

- Collection
- Bands
- Point Browser
- Collection Editor

## Collection

Let us select some collections of [GEE datasets](https://developers.google.com/earth-engine/datasets).

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_l8_collection.png
  :width: 600px
```

## Bands

After selecting and loading a collection, its available bands are shown:

```{eval-rst}
.. figure:: ../_static/img_ex2/l8_bands.png
  :width: 400px
```

## Point Browser

It let us explore the historical data (selected bands) of a single point.

In our case we have 3 sample points from `points` layer. We will start with `P1`:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_point_browser.png
  :width: 600px
```

## Data

After a point (in the point browser) and some bands are selected...

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_p1_b5.png
  :width: 600px
```

We can see the plot of historical data:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_p1_b5_plot.png
  :width: 600px
```

With the data button:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_data_button.png
  :width: 500px
```

We can see the raw data used in the plot:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_raw_data.png
  :width: 500px
```

At this moment, we are exploring default bands from GEE datasets. If we want to explore a derivated band like NDVI or understand a bit more how this plugin is interacting with GEE plugin, we need to use the **Collection Editor**.

## Collection Editor

It helps us to understand how a dataset from GEE is called and how to customize our default collections.

### Exploration

To invocate the **Collection Editor** we need to click in:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_click_collection_editor.png
  :width: 500px
```

This opens the **Collection Editor** which contains:

1. **Open Earth Engine Data Catalog** button: clicking opens the [Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets/catalog).
2. A code python editor with the code used to call the collection **USGS Landsat 8 Surface reflectance Tier 1** from Google Earth Engine datasets.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_collection_editor.png
  :width: 500px
```

In the first line, **ee** (the Python API package of GEE) is imported.

```python
import ee
```

The following line extracts the Landsat 8 collection

```python
imageCollection = ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")
```
:::{important}
In this tutorial, we are focusing on Landsat 8 images. However, you can select any data collection available, like Sentinel 1 and Sentinel 2 images.
:::

The Earth Engine snippet **ee.ImageCollection("LANDSAT/LC08/C01/T1_SR")** is extracted from the Earth Engine Catalog:

```{eval-rst}
.. figure:: ../_static/img_ex2/ee_data_warning.png
  :width: 500px
```

:::{important}
If you access our initial collection ([LANDSAT/LC08/C01/T1_SR](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C01_T1_SR)), it shows a warning message:

**"This dataset (USGS Landsat 8 Surface Reflectance Tier 1) has been superseded by [LANDSAT/LC08/C02/T1_L2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2)"**

This is a situation that sometimes ocurrs with collections in GEE. That's why it is important to check the information about our collection in the GEE Catalog.
:::

Taking this in consideration, we can exchange our initial collection to [LANDSAT/LC08/C02/T1_L2](https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2):

```{eval-rst}
.. figure:: ../_static/img_ex2/ee_data_suggested.png
  :width: 500px
```

:::{caution}
Take in consideration the **Scale** parameter, used by Google to save space in the dataset.
In the previus plot, the values of B5 were out of scale from their actual values.
:::

```python
imageCollection = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
```

Then, the suggested new snippet replace the old (from our initial collection) in the **Collection Editor**. Next, we need to click in **Load Connection** in order to refresh and select the bands of the new collection (the suggested by the GEE catalog).

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_load_new_collection.png
  :width: 700px
```

As we can see, the band names in this collection are different: `SR_B4` and `SR_B5`

To update the plot, we need:

1. Click in `Re-read point profile` button
2. Right click in the black background plot and click in `View All`

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_update_view.png
  :width: 700px
```

Now, we can see the trends of the selected bands values, remember to take in consideration the **Scale** and **Offset** parameter for the actual value.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_p1.png
  :width: 700px
```

Then, we can explore the profile of the other points:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_p2.png
  :width: 700px
```

(Add_bands)=

### Add customized bands

Sometimes we need a derivated band like NDVI.
For example, in Landsat 8, the NDVI is calculated based on B5 and B4 bands (in the current dataset, the bands names are `SR_B5` and `SR_B4`):

  ```{math}
   \begin{eqnarray}
      ndvi & = & \frac{SR\_B5 - SR\_B4}{SR\_B5 + SR\_B4}
   \end{eqnarray}
  ```
  
We can build an **add_ndvi** function to achieve this.
First, the **add_ndvi** function can be applied to an image and has 2 parts:

1. Calculate the ndvi band and name it **NDVI**.
2. Add the calculated band to the image.

```python
def add_ndvi(image):
    ndvi = image.normalizedDifference(["SR_B5", "SR_B4"]).rename("NDVI")
    return image.addBands(ndvi)
```

Then, our image collection applies the **add_ndvi** function to each of its images through the python [map](https://docs.python.org/3/library/functions.html#map) function.

```python
imageCollection = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2").map(add_ndvi)
```

The following gee methods are used:

- [normalizedDifference](https://developers.google.com/earth-engine/apidocs/ee-image-normalizeddifference) function to calculate the `ndvi`. (The **Scale** related to `SR_B5` and `SR_B4` does not impact the NDVI calculation).
- [rename](https://developers.google.com/earth-engine/apidocs/ee-image-rename) function
- [addBands](https://developers.google.com/earth-engine/apidocs/ee-image-addbands) function

After writting the code, click on **Load Collection**. The NDVI band is shown in the list of bands.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_add_ndvi_band.png
  :width: 500px
```

Finally, we can update (remember the 2 steps: `Re-read point profile` and right click and `View all`) our plot to see the historical ndvi data.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts_ndvi_p2.png
  :width: 700px
```

As we can see, the `ndvi` values are within the expected range (between -1 and 1).
