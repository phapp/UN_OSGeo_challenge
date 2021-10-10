# Concluding Remarks

In this tutorial, we have learnt how to perform supervised semantic segmentation based on pixel-wise classification using Random Forest. It was applied to monitor the snow areas in the Huascaran mountain. The images were from the satellite Landsat 8, acquired from 2016 to 2021 using the **Semi-Automatic Classification Plugin (SCP)** for QGIS.

The main topics explained in the tutorial are the following:
- Acquisition of Landsat 8 images using SCP plugin.
- Pre-processing of Landsat 8 images.
- Collecting samples to train a classifier.
- Training a classifier for supervised pixel-wise classification using the dzetsaka plugin.
- Generation of classification maps.
- Analysis of the classification maps and how to understand these results.

The results obtained in this tutorial are preliminary results. The statistics computed are not conclusive as the generated classification maps were affected by the presence of clouds.

Monitoring snow areas can be improved using **Synthetic Aperture Radar (SAR)** images, like those from Sentinel-1 satellite, as this kind of sensor is almost not affected by weather conditions (clouds, rain, day or night). Also, optical images with a higher spatial resolution, like those from Sentinel-2 satellite, would help to get more accurate classification maps. The SCP plugin can be employed to download and pre-process these images, similarly to what was explained for Landsat 8.

A more detailed explanaitio about the acquisition and pre-processing of Sentinel-1 and Sentinel-2 images can be found in Appendices [A](10_appendix_A.html#appendix-a-working-with-sentinel-1-images) and [B](11_appendix_B.html#appendix-b-working-with-sentinel-2-images).
