# Concluding Remarks

In this tutorial, we have learnt how to perform a linear regression to obtain a deforestation trend based on NDVI historical data in a region of interest.

It was applied to monitor the deforestation trends in the municipality São Félix do Xingu (Brazil). The images were from the satellite Landsat 8, acquired from 2017 to 2020 using the Google Earth Engine plugin for QGIS.

The main topics explained in the tutorial are the following:

- Acquisition of Landsat 8 images using Google Earth Engine plugin.
- Bands manipulation of Landsat 8 to add derivate bands like NDVI or time.
- PyQGIS to interface between QGIS layer (for Region of Interest) and Google Earth Engine plugin.
- Training a linear fit regression to get the trend based on images collection.
- Analysis of the parameters of linear regression model for deforestation.

The results obtained in this tutorial are preliminary results with a simplified model based on historical NDVI.
