# Appendix B: Working with Sentinel-2 images

## Download Sentinel-2 images

To download **Sentinel-2** images, go to **SCP->Download** products. Then, enter the **UL** and **LR** cooridnates of the selected area, in **Products** select **Sentinel-2**, and set **Date from/to** to **2021-07-01** and **2021-07-31**, to find images in the same month that the **Landsat 8** images. Click on **Find**.

```{eval-rst}
.. figure:: ../_static/img_ex1/59_apxB_download_sentinel2.png
  :width: 800px
  :name: download-sentinel-2
```

SCP searches for **Sentinel-2** _Level 1C_ and _Level 2A_ images. _Level 1C_ images require atmospherical correction, while _Level 2A_ images do not. However, it is still necessary to convert pixel values to a decimal value of reflectance for _Level 2A_ images.

Unfortunately, it seems that there is a little bug in SCP that does not allow to preview **Sentinel-2** images. So, we need to download the images and see if they completely cover the area of interest. In this case, only the following images will be necessary:

|              ProductID             |
|:----------------------------------:|
| L1C_T17LRL_A022645_20210707T152640 |
| L1C_T18LTQ_A022645_20210707T152640 |
| L1C_T18LTR_A022645_20210707T152640 |

Then, select the other images from the list and delete them. Disable the options **Only if preview in Layers** and **Preprocess images**, and click on Run.

```{eval-rst}
.. figure:: ../_static/img_ex1/60_apxB_download_sentinel2_reduced.png
  :width: 800px
  :name: download-sentinel-2-reduced
```

Finally, the images are added to the project.

```{eval-rst}
.. figure:: ../_static/img_ex1/61_apxB_sentinel2_images.png
  :width: 800px
  :name: sentinel2-images
```
## Pre-processing

As **Sentinel-2** _Level 1C_ images were downloaded, it is necessary to perform the atmospheric correction. Then, go to **SCP->Preprocessing->Sentinel-2**.

Select the directory containing **Sentinel-2** bands and the _metadata file_. Let's begin with the following image: **L1C_T17LRL_A022645_20210707T152640**. Enable the option _Apply DOS1 atmospheric correction_ and disable all other options. 

Finally, click on **Run**. You will be asked to select a folder to save the preprocessed bands. For instance, create a folder with the following name: **Preprocess/Sentinel-2/L1C_T17LRL**.

```{eval-rst}
.. figure:: ../_static/img_ex1/62_apxB_preprocessing_configuration.PNG
  :width: 800px
  :name: sentinel2-images-preprocessing
```

After some minutes, the pre-processed bands are added to the project with the prefix **“RT\_”**.

:::{important}
It is recommended to perform the _DOS1 atmospheric correction_ for the entire image (before clipping the image) in order to improve the calculation of parameters based on the image.
:::

Repeat the same procedure for all **Sentinel-2** images downloaded.