# Collect samples for training/testing

## Create bands stacks
Now, we will create a training set for the classification algorithm. The training set is a vector layer with polygons delineating areas belonging to each class, in this case: **Snow Cover** and **Background**.

But first, let’s create an **_stack with all preprocessed Landsat 8 bands_** for each date. These stacks will help us to train the classification algorithm.

:::{tip}
In order to simplify the following steps, it is recommended to remove all layers from the project.
:::

Go to the menu **Raster->Miscellaneous->Merge**:

```{eval-rst}
.. figure:: ../_static/img_ex1/26_merge_rasters.png
  :name: raster-m-merge
  :width: 500px
```

In the **Merge** window, we need to set up the following parameter: **Input layers**

```{eval-rst}
.. figure:: ../_static/img_ex1/27_merge_rasters_window.png
  :name: merge-parameters
  :width: 800px
```

Click on the three dots, then, click on **Add File(s)**, and select bands **2,3,4,5,6 and 7** for each date. In this case, **2021-07-15**.

```{eval-rst}
.. figure:: ../_static/img_ex1/28_merge_rasters_all_bands.png
  :name: merge-parameters-bands
  :width: 800px
```

:::{important}
The order of the bands is not important to build the stack. However, you must remember this order and use the same for all dates.

Thus, to simplify this step, let's use the following order: _2, 3, 4, 5, 6 and 7_. You can change the order of each band by clicking and dragging each element in the list.
:::


Click on **OK**. Enable the option: **Place each input file into a separate band**. Then, in **Merged**, select the **Save to File…** option, and enter the name of the raster: **Stacks/Stack_2021-07-15.tif**. Finally, click on **Run**.

The output raster is loaded in the project. We can distinguish two main classes: **mountains** (dark blue) and **snow cover** (white).

```{eval-rst}
.. figure:: ../_static/img_ex1/29_merge_rasters_result_Stack.png
  :name: rgb_2021-07-15
  :width: 800px
```

The mountains appear in a dark blue color due to the RGB composition of this raster. We can change it for a better visualization, **right click** on the layer, and go to **Properties**.

In the **Symbology** menu, change the bands in the **Band Rendering** section. Initially, the **RGB** order is **Band 1**, **Band 2**, and **Band 3**, which would be a _false color composition_. In order to create a _true color RGB composition_, change the order to **Band 3**, **Band 2**, and **Band 1**. 

```{eval-rst}
.. figure:: ../_static/img_ex1/30_stack_rgb_composition.png
  :name: stack-color-composition
  :width: 800px
```

Click on **Apply**, and **OK**. Then, the layer visualization changes. Now mountains appear in a dark brown color.

```{eval-rst}
.. figure:: ../_static/img_ex1/30_stack_rgb_composition_layer.png
  :name: stack-color-composition-layer
  :width: 800px
```

:::{important}
Remember that in Landsat 8, the **RGB** bands are the **4**, **3**, and **2**.

Also, due to the order employed to stack all bands, bands **4**, **3**, and **2** are the bands **3**, **2**, and **1**, respectively, in the stack file.
:::

Repeat this step for each date to create all stacks.

:::{important}
Do not forget to use the same order to create all stacks: _2, 3, 4, 5, 6 and 7_.

Also, enable the **Place each input file into a separate band** option.
:::

Now, the following files have been added to the project directory:

```{literalinclude} ../_static/ex1_rgb-compositions_stacks.txt
---
language: default
---
```

## Collecting samples

We are ready to create the polygons for training. Go to the menu **Layer->Create Layer->New Shapefile Layer…**:

```{eval-rst}
.. figure:: ../_static/img_ex1/31_create_vector_layer.png
  :name: new-shapefile-layer
  :width: 500px
```

In the **New Shapefile Layer** window, select the following parameters:

- _File name_: path to the file to save the vector layer, training.shp in our project directory.
- _Geometry type_: select **Polygon**.
- _Coordinate Reference System_: select the same CRS as the images. In this case: **EPSG:32618 WGS 84 / UTM zone 18N**.
- In the **New Field** section, add the **Class** field to store the classes names. Then, click on **Add to Fields List**.
- Finally, click on **OK**.

So, an empty vector layer has been added to our project.

```{eval-rst}
.. figure:: ../_static/img_ex1/32_create_vector_layer_parameters.png
  :name: shapefile-add-field
  :width: 600px
```

Now we need to create polygons over areas that belong to each class: **Snow Cover** and **Background**.

As a visual reference to locate areas of each class, let's use the true color RGB compositions. We will employ this composition as it is more intuitive and natural for interpretation. However, any RGB composition can be used at this point.

Select an stack file from any date as our training set. In this case, we will work with the image from **2016-11-22**, due to the presence of many clouds that we need to consider for training.

```{eval-rst}
.. figure:: ../_static/img_ex1/33_training_RGB_image.png
  :name: base_2016-11-22
  :width: 400px
```

Click on the vector layer **training.shp**, and click on **Toggle Editing**. Then, click on **Add Polygon**.

```{eval-rst}
.. figure:: ../_static/img_ex1/33_menu_vector.png
  :name: menu-vector
  :width: 200px
```

Zoom in to a mountain area, and define the vertices of a polygon by **left clicking** on the image.
To close the polygon, just do a **right click**. Now you have to enter the **id** and **Class** for this polygon. Let’s use **1** for **Background**, and **2** for **Snow Cover**.

```{eval-rst}
.. list-table::

    * - .. figure:: ../_static/img_ex1/34_training_sample_background.png
           :width: 400px           

      - .. figure:: ../_static/img_ex1/35_training_sample_snow.png
           :width: 400px           
```

As we only have 2 classes, we need to collect many different polygons for the class **Background**, as its variability is greater than **Snow Cover**. So, include _Clouds_, _Water Bodies_, _Mountains_, _Urban Area_ (if exists), or other classes different from **Snow Cover** to help our classifier to learn a proper discrimination between these classes.

Remember that the appearance of **Snow** and **Cloud** are similar in the true color RGB Compositions, but their spectral signature are different. Thus, we can discriminate them using bands that are not in the visible area of the electromagnetic spectrum. The following figure illustrates the spectral signatures for different classes:

```{eval-rst}
.. figure:: ../_static/img_ex1/36_spectral_signatures.png
  :name: cloud-detection
  :width: 800px

  Taken from Zhuge, X. Y., Zou, X., & Wang, Y. (2017). A fast cloud detection algorithm applicable to monitoring and nowcasting of daytime cloud systems. *IEEE Transactions on Geoscience and Remote Sensing*, 55(11), 6111-6119.
```

:::{important}
Remember. different RGB compositions could be employed as a visual reference, specially a composition that allow us to diferentiate between **Snow** and **Clouds**.

For instance, an RGB composition with bands **1**, **5**, and **6** looks much better to distinguish between **Snow** (Red) and **Clouds** (White).
```{eval-rst}
.. figure:: ../_static/img_ex1/36_another_rgb_composition.png
  :name: cloud-detection-2
  :width: 350px
```
Feel free to change the RGB composition while you are collecting samples to improve the visualization.
:::

After collecting many polygons, our vector layer for training looks like (you can download it [here](https://zenodo.org/record/5542555/files/training.rar?download=1)):

```{eval-rst}
.. figure:: ../_static/img_ex1/37_training_samples_collected.png
  :name: train-polygons
  :width: 800px
```

:::{important}
Before extracting the file with the training polygons, verify that this file is not locked. **Right click** on the file, go to **Properties**, then, check if the file is locked or not.

To visualize the polygons, you just need to add a vector layer with the downloaded file to the project.
:::

Where **Background** and **Snow Cover** are represented by the _brown_ and _blue_ polygons, respectively.

If you want to assign a color for each class, just **right click** on the **training** layer and go to **Properties**. In the **Symbology** menu, select **Categorized**, Column **id**, Color map **Random Colors**, and click on **Classify**.
Before applying the colormap, you can change each color by **double clicking** them. Finally, click on **Apply** and **OK**.

```{eval-rst}
.. figure:: ../_static/img_ex1/38_training_vector_layout.png
  :name: layer-training-symbology
  :width: 800px
```

:::{warning}
We collected just a few polygons in this exercise. The quality of the Machine Learning classifier is directly dependent on the quality of the training set.

Thus, for a real scenario, it may be important to collect a greater number of samples.
:::