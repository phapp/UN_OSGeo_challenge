# Appendix A: Working with Sentinel-1 images

## Download Sentinel-1 images

To download **Sentinel-1** images, go to **SCP->Download** products. Then, enter the **UL** and **LR** cooridnates of the selected area, in **Products** select **Sentinel-1**, and set **Date from/to** to **2021-07-01** and **2021-07-31**, to find images in the same month that the **Landsat 8** images. Click on **Find**.

```{eval-rst}
.. figure:: ../_static/img_ex1/56_apxA_download_sentinel1.png
  :width: 800px
  :name: download-sentinel-1
```

:::{important}
SCP only includes the search and download of **Sentinel-1 GRD** images.
:::

Select any of the images in the list and click on the button **Display preview of highlighted images in map**.

```{eval-rst}
.. figure:: ../_static/img_ex1/57_apxA_preview_download_sentinel1.png
  :width: 600px
  :name: preview-download-sentinel-1
```
Finally, click on the button **Run** to download the previewed images. You will be asked to select a directory to download the products. Let's use the folder **Images**.

:::{important}
Sentinel-1 bands are bigger than Landsat 8, so this step would take several minutes, depending on your internet connection.
:::

## Pre-processing

SCP will pre-processes Sentinel-1 GRD images performing the following methodology:

- Orbit file application;
- Removal of GRD border noise (for low intensity and invalid data);
- Removal of thermal noise (to reduce discontinuities between sub-swaths);
- Radiometric calibration for backscatter intensity calculation;
- Orthorectification (terrain correction) using the SRTM 30 meter DEM (Digital Elevation Model);
- Conversion of backscatter coefficient to dB.

:::{note}
More information about Sentinel-1 pre-processing can be found in this [paper](https://www.mdpi.com/2504-3900/18/1/11).
:::

Go to **SCP->Preprocessing->Sentinel-1**. Select the Sentinel-1 image previously downloaded. Then, click on **Run**.


```{eval-rst}
.. figure:: ../_static/img_ex1/58_apxA_preprocessing_sentinel1.png
  :width: 700px
  :name: preprocessing-sentinel-1
```

These processes are performed through the **SNAP Graph Processing Tool (GPT)** with a graph file **.xml**. 
Therefore, the installation of [ESA SNAP](https://step.esa.int/main/toolboxes/snap/) is required for the pre-processing of Sentinel-1 images.

After the pre-processing, these images can be clipped to the region of interest following the instructions in section [Dataset Preparation](05_dataset-preparation.html#dataset-preparation).