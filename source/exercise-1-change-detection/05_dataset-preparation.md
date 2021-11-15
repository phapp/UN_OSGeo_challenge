# Dataset Preparation

## Clipping images

The next step is to **Clip** the images to the region of interest. To do this, go to **SCP->Band set** to define a band set with all bands.

In the **Single band list** section, click on **Refresh list** to list all bands layers in our project.

```{eval-rst}
.. figure:: ../_static/img_ex1/18_bandset_2021.png
  :name: scp-refresh-list
  :width: 800px
```

:::{attention}
The band BQA is not necessary at this point. So, this layer should be removed from the project.
:::

Click on the **Select all** button , and then click on the **Add band to Band set**.

Now the **Band set 1** contains bands from 2 to 7. Next, select the **Wavelength quick settings** for **Landsat 8 OLI (bands 2, 3, 4, 5, 6, 7)**. You will notice how the wavelengths are assigned to each band.

```{eval-rst}
.. figure:: ../_static/img_ex1/19_bandset_2021_2.png
  :name: scp-add-bandset
  :width: 800px
```

:::{caution}
The _**Center wavelength**_ values could be different in case that SCP's **Wavelength quick settings** includes band 1, which occurs sometimes.

However, this would not be a problem for our case, as we will not generate the spectral signatures of each band.
:::

Now that the band set is defined. Go to the **Clip multiple rasters** menu to clip the bands based on a set of given coordinates. It is also possible to use a vector file to clip rasters.

```{eval-rst}
.. figure:: ../_static/img_ex1/20_clipping_menu.png
  :name: scp-clip-menu
  :width: 200px
```

:::{tip}
It is not necessary to click on the **Run** button, as we are only defining a band set.
:::

Similarly to the **Download products** section, we will select the **UL** and **LR** coordinates from the map.

```{eval-rst}
.. figure:: ../_static/img_ex1/20_clipping_window.png
  :name: scp-clip-bandset
  :width: 800px
```

But first, change the CRS of the project to the CRS of the bands.

```{eval-rst}
.. figure:: ../_static/img_ex1/21_clipping_CRS.png
  :name: change-bands-crs
  :width: 400px
```

Again, it is possible to define the coordinates by clicking on the **Set area in the map** button. Then, we just need to do a **left click**, to select the **UL**, and **right click**, to select the **LR**. 

For this tutorial, let’s use the following coordinates to have the same results:

|     | UL              | LR              |
| :-- | --------------: | --------------: |
| X   |          190907 |          244798 |
| Y   |         -973415 |        -1044425 |

:::{important}
Remember that we are currently working with the **WGS 84 / UTM zone 18N (EPSG:32618)** as Coordinate Reference System (CRS) for the project.
:::

```{eval-rst}
.. figure:: ../_static/img_ex1/22_clipping_ROI.png
  :name: scp-clip-img
  :width: 600px
```

Now, click on the **Run** button, where you will be asked to select a folder to save the results. Let’s create a folder called **Clip**, in the project directory, and a subfolder with the acquisition date, in this case: **2021-07-15**. 

After clipping the images, we have the clipped raster layers in the project with the prefix **“clip\_”**. Each clipped image has a size of 1796 x 2367.

```{eval-rst}
.. figure:: ../_static/img_ex1/23_clipping_result.png
  :name: scp-clips-layers
  :width: 800px
```

:::{warning}
If you receive an error message while clipping the images, go to **SCP->Settings->Debug** and click on **Test dependencies**. This will check if **SCP** has all necessary dependencies installed to work properly.

If a dependency is missing, as it happened to us in mac OS, you can use QGIS to clip your images.

More information about how to do it can be found in the following [link](http://www.qgistutorials.com/en/docs/raster_mosaicing_and_clipping.html).
:::

## Pre-processing Landsat images

Now, we are ready to pre-process the clipped images. Go to **SCP->Preprocessing->Landsat**.

There are two input parameters:

- _Directory containing Landsat bands_: it is the directory of the clipped images: **Clip/2021-07-15**.
- _Select MTL file_: path to the MTL file downloaded with all original bands: **Images/LC08_L1TP_008066_20210715_20210716_01_RT_2021-07-15/LC08_L1TP_008066_20210715_20210716_01_RT_MTL.txt**

Just enable _Add bands in a new Band set_ and _Use value as NoData_, and disable all other options as they are not necessary in this case.

```{eval-rst}
.. figure:: ../_static/img_ex1/24_scp_preprocessing.png
  :name: scp-pre-processing
  :width: 800px
```

:::{important}
The pre-processing could be performed during the download of the products. However, we are doing it manually to have more control about the applied transformations.
:::

Then, click on **Run**. You will be asked to enter an output directory. Let’s create another folder with the acquisition date: **Preprocess/2021-07-15**. After preprocessing the images, we have new raster layers in the project with the prefix **“RT\_”**.

```{eval-rst}
.. figure:: ../_static/img_ex1/25_scp_preprocess_result.png
  :name: scp-rts-layers
  :width: 800px
```

At this point, the structure of the working directory should be the following:

```{literalinclude} ../_static/ex1_pwd.txt
---
language: default
---
```

As we are interested in monitoring the evolution of the study area in the last 5 years, we will download more images. The acquisition dates of all images are the following:

|    Date    | Cloud cover (%) | Zone | Row |
|:----------:|:---------------:|:----:|:---:|
| 2021-07-15 |        5        |   8  |  66 |
| 2020-07-28 |        6        |   8  |  66 |
| 2019-07-10 |        9        |   8  |  66 |
| 2018-07-07 |        6        |   8  |  66 |
| 2016-11-22 |        23       |   8  |  66 |

:::{important}
It is possible to select other dates; however, these specific dates have the less cloud coverage in the study area. 

Moreover, images from the same month and different years were selected to analyze the snow cover almost in the same day of the year. 

The image from 2016 is an exception as it was the only date without clouds in the study area. There are not images from 2017 as it was not possible to find images without clouds in the study area.

Notice that all images have the same **Zone** and **Row**, because they cover exactly the same area.
:::

Then, we need to repeat the last steps to download, clip and pre-process all Landsat 8 products:

* To download more images, go to **SCP->Download Products**. It is only necessary to change some parameters like **Date from/to**, and in some cases, the **Max cloud cover (%)**. The other parameters are the same: **UL** and **LR** coordinates, and **Products**. Finally, click on **Run**.

:::{important}
Remember to clear the list with the results of the search by clicking on the button **Reset** before downloading an image from another date.

```{eval-rst}
.. figure:: ../_static/img_ex1/25_scp_reset_list.PNG
  :name: scp-reset-list
  :width: 50px
```
:::

* Before **Clipping**, remember to define a _**Band Set**_ with the downloaded bands. Go to **SCP->Band set**. Then, click on **Refresh** the list and **Add** the corresponding bands to create a new band set.

* For **Clipping** all bands, go to **SCP->Preprocessing->Clip multiple rasters**. Select the _**Band set**_ created in the previous step, and the coordinates. Remember to change the **CRS** of the project to the **CRS** of the bands. Finally, click on **Run**.

* To perform the **Pre-processing** of all clipped bands, go to **SCP->Preprocessing->Landsat**. Then, select the folder with _all clipped bands_ and its corresponding _MTL file_. Finally, click on **Run**.

After executing these steps, the working directory will have the following structure:

```{literalinclude} ../_static/ex1_clip_preprocess.txt
---
language: default
---
```

:::{tip}
After downloading, clipping and pre-processing all images, the project will have too many layers loaded. This is not necessary as we will work only with all pre-processed images, so, just keep layers with the prefix **“RT\_”**
:::