# Download Landsat images

Now let’s define the coordinates of our study area: the Huascaran mountain in the Cordillera Blanca range. 

Go to **SCP->Download products**, and in the **Search** menu, click on **_Add OpenStreetMap to the map_** to add an OpenStreetMap layer. This layer will be a visual reference to locate the study area.

```{eval-rst}
.. figure:: ../_static/img_ex1/5_scp_add_OSM.png
  :width: 600px
  :name: scp-add-osm
```

The study area is located in Peru, in the Ancash department:

```{eval-rst}
.. figure:: ../_static/img_ex1/6_peru_map.png
  :name: huascaran-location
  :width: 900px 
```

:::{tip}
It is not necessary to locate it with precision as we will introduce the exact coordinates in the following steps.
:::

Now, we need to define our region of interest to search for Landsat products containing it.

The region of interest is defined by the **UL** (_Upper Left_) and **LR** (_Lower Right_) values, which are the coordinates of a rectangle:

```{eval-rst}
.. figure:: ../_static/img_ex1/7_UL_LR.png
  :name: ul-lr
  :width: 250px
```

To define these coordinates in SCP, click on **_Set area in the map_**:

```{eval-rst}
.. figure:: ../_static/img_ex1/8_scp_show_area.png
  :name: set-area
  :width: 300px
```

Then, we just need to do a **left click**, to select the **UL**, and **right click**, to select the **LR**. 

After doing that, we will see a Red Rectangle delineating our region of interest.

```{eval-rst}
.. figure:: ../_static/img_ex1/9_map_area_download.png
  :name: huascaran-lulr
  :width: 500px
```

:::{note}
It is possible to move these coordinates by doing another left and right click.
:::

In order to work with the same area, let’s use the following coordinates for **UL** and **LR**:

|     | UL              | LR              |
| :-- | --------------: | --------------: |
| X   |           -77.8 |           -77.0 |
| Y   |            -8.7 |            -9.6 |

:::{important}
Remember that we are currently working with the **WGS 84 (EPSG:4326)** as Coordinate Reference System (CRS) for the project.
:::

Now, our region of interest is well defined. The next step is to select the **Products** and the **date interval** to search for them. In this case, let’s search for an image in this year, 2021, from Landsat 8.

So, in **Products** select **L8 OLI/TIRS**, in **Date from/to** write **2021-01-01** and **2021-08-10** (or the current day), and select a maximum percentage of **cloud cover** by changing the field **Max cloud cover (%)**. In this case, let’s try with **10%**. Finally, click on the **Find images** button

```{eval-rst}
.. figure:: ../_static/img_ex1/10_scp_download_dates.png
  :name: scp-find-images
  :width: 800px
```

Now, we can see the results of our search. In this case, there was only one image with a cloud cover of 5%, acquired on **2021-07-15**, path 8, row 66:

```{eval-rst}
.. figure:: ../_static/img_ex1/11_scp_download_image.png
  :name: scp-2021-07-15
  :width: 800px
```

:::{caution}
If this image is not available in SCP, you can download it from our data repository in Zenodo: [link](https://zenodo.org/record/5507081#.YVZKqtD0mUk) or you can work with a different available image (it may be necessary to increase *the max cloud cover* parameter).

Apparently, there were some changes in SCP during the development of this material, or there is a temporary bug, that may result in different search results. Even if this image exists in the [USGS Earth Explorer repository](https://earthexplorer.usgs.gov/), it may not appear in the SCP search results.
:::

It is possible to see a preview of the image over the region of interest. Just click on the button **Display preview of highlighted images in map**.

```{eval-rst}
.. figure:: ../_static/img_ex1/12_scp_download_preview.png
  :name: scp-2021-07-15-display
  :width: 400px
```

Then, a new layer is added to the project, a lower resolution version of the selected image. As we can see, it covers our region of interest, which is located at the bottom of the image. In this scene, the mountains are covered with snow, which appears in a light blue color in the image.

```{eval-rst}
.. figure:: ../_static/img_ex1/13_scp_download_preview2.png
  :name: scp-landsat-2021-07-15
  :width: 600px
```

Before downloading the products, it is necessary to define which bands to use. Based on [Landsat 8 bands definition](https://www.usgs.gov/faqs/what-are-band-designations-landsat-satellites?qt-news_science_products=0#qt-news_science_products), we are going to work just with bands 2, 3, 4, 5, 6, and 7.

```{eval-rst}
.. figure:: ../_static/img_ex1/14_landsat_bands.png
  :name: landsat-bands
  :width: 800px
```

Then, go to the **Download options** menu, and select those bands:

```{eval-rst}
.. figure:: ../_static/img_ex1/15_landsat_selected_bands.png
  :name: landsat-selected-bands
  :width: 900px
```

Now, let’s download the product. Come back to the **Search** menu, and verify the following configuration in the **Download** section:

```{eval-rst}
.. table::
   :widths: auto
   :name: lansat-imgs-parameters

   +---------------------------+------------+-------------------------------------------------+
   | Parameter                 | Status     | Description                                     |
   +===========================+============+=================================================+
   | Only if preview in Layers | Enable     | To download only images that its preview is in  |
   |                           |            | the layers’ project; otherwise, all images will |
   |                           |            | be downloaded                                   |
   +---------------------------+------------+-------------------------------------------------+
   | Preprocess images         | Disable    | We will preprocess all images later             |
   +---------------------------+------------+-------------------------------------------------+
   | Load bands in QGIS        | Enable     | Enable if you would like to see all bands layers|
   |                           |            | in your project                                 |
   +---------------------------+------------+-------------------------------------------------+
```

Finally, click on the **Run** button.

```{eval-rst}
.. figure:: ../_static/img_ex1/16_scp_download_run.png
  :name: scp-run
  :width: 800px
```

:::{caution}
These steps were tested on different computers with different OS and configurations.

In some cases, the preview button was not working properly.

If it is the case, uncheck the option _**Only if preview in layers**_ in order to be able to download all images in the list.
Note that all products that will not be used should be removed from the list first.
:::

You will be asked to select a directory to download the products. For instance, a folder called **Images** in the project directory. You can follow the progress of the products downloading with the progress bar. Depending on your internet connection, this step could take some minutes.

```{eval-rst}
.. figure:: ../_static/img_ex1/16_scp_downloading.png
  :name: scp-downloading
  :width: 800px
```
&nbsp;

Now we can see all bands as layers in the project

```{eval-rst}
.. figure:: ../_static/img_ex1/17_scp_download_2021.png
  :name: scp-all-bands
  :width: 800px
```
&nbsp;

Notice the following files in the folder selected to download the Landsat product: **Images/LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15**:

```{eval-rst}
.. table::
   :widths: 73 27
   :name: landsat-files   

   ===========================================================  =====================================================
   Filename                                                     Description
   ===========================================================  =====================================================
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B2.TIF   Raster image with band 2
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B3.TIF   Raster image with band 3
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B4.TIF   Raster image with band 4
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B5.TIF   Raster image with band 5
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B6.TIF   Raster image with band 6
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_B7.TIF   Raster image with band 7
   LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15_BQA.TIF  Raster image with the Quality Assessment band
   LC08_L1TP_008066_20210715_20210716_01_RT_MTL.txt             MTL file with metadata about acquisition of all bands
   ===========================================================  =====================================================
```
