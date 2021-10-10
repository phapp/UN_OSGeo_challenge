# Regression

## NDVI

The Normalized Difference Vegetation Index (NDVI) [can be used as an indicator of vegetation degradation of ecosystem vegetation](https://www.researchgate.net/publication/292666603_NDVI_as_indicator_of_degradation). Factors like clouds, shadows of clouds, climate anomalies (like **La Niña/El Niño**) should be taken in consideration for more robust models which are out the scope of the present tutorial.
Despite this limitation, the NDVI variation can help us to understand the context of deforestation and can be used as an indicator.

## Linear Regression

In this tutorial, the NDVI variation will be modeled as a linear fit.

The data should be set up as a two-band input image, where the first band is the independent variable and the second band is the dependent variable.

In our case, the dependent variable is the NDVI and the independent variable is the time, and the slope of this model will be our indicator for deforestation. The process is shown in {numref}`methodology-ex2`.

```{eval-rst}
.. figure:: ../_static/img_ex2/methodology_ex2.png
  :name: methodology-ex2
  :width: 600px

  Methodology followed in this tutorial for monitoring deforestation in São Félix do Xingu, Brazil.
```

More information about these topics can be found in the following links:

- Machine Learning [[1]](https://www.digitalocean.com/community/tutorials/an-introduction-to-machine-learning),[[2]](https://towardsdatascience.com/introduction-to-machine-learning-for-beginners-eed6024fdb08)
- Linear Regression [[1]](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86),[[2]](https://machinelearningmastery.com/linear-regression-for-machine-learning)
