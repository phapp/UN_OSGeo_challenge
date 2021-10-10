# Supervised Change Detection

## Semantic Segmentation

Semantic Segmentation can be defined as the process to assign a class with semantic meaning to each pixel of an image. There are many machine learning algorithms to perform this task, which are trained upon datasets that contain features (pixel intensity values, texture, shape, etc.) and its corresponding labels (classes with semantic meaning).

### Random Forest (RF)
The Random Forest classifier has become popular within the remote sensing community due to the accuracy of its classifications. RF classifier is an ensemble classifier that produces multiple decision trees, using a randomly selected subset of training samples and features. RF classifier can be employed for semantic segmentation by performing pixel-wise classification.

### Support Vector Machine (SVM)
Support Vector Machine is a linear model for classification and regression problems. It can solve linear and non-linear problems and work well for many practical problems. The idea of SVM is simple: The algorithm creates a line or a hyperplane which separates the data into classes.

### Gaussian Mixture Model (GMM)
A Gaussian Mixture Model is a distribution assembled from weighted multivariate Gaussian distributions (normal distributionS). Weighting factors assign each distribution different levels of importance. The resulting model is a super-position (i.e. an overlapping) of bell-shaped curves.

### k-Nearest Neighbors (KNN)
The KNN algorithm assumes that similar things exist in close proximity. In other words, similar things are near to each other. KNN captures the idea of similarity (sometimes called distance, proximity, or closeness) based on the distance between points on a graph.

## Change Detection

Change Detection in Remote Sensing refers to the process of identifying changes between scenes of the same location acquired at different times. There are many applications of change detection such as detection of affected areas after a natural disaster (floods, hurricanes, tornadoes, earthquakes, tsunamis), discovering and quantification of illegal activities (rivers/ocean pollution, deforestation) or global warming consequences (deglaciation, biodiversity reduction).

Change Detection can be performed by direct comparison of classification maps of different dates. This comparison can be the subtraction of one image to the other one, to spotlight the changes that occurred for each class (diminish or increase).

This educational material employs the following methodology for monitoring snow areas in the Huascaran, Peru. First, a set of Landsat 8 images from the last five years are acquired. Second, these images are clipped, pre-processed and stacked. Then, samples are collected to train a Random Forest classifier. This classifier is applied to all images to generate classification maps for each date. Finally, the classification maps are compared and change detection maps are produced to illustrate the changes among the last five years.

```{eval-rst}
.. figure:: ../_static/img_ex1/0_methodology.png
  :name: methodology
  :width: 600px

  Methodology followed in this tutorial for monitoring snow areas in the Huascaran mountain, Peru.
```

More information about these topics can be found in the following links:
* Machine Learning [[1]](https://www.digitalocean.com/community/tutorials/an-introduction-to-machine-learning),[[2]](https://towardsdatascience.com/introduction-to-machine-learning-for-beginners-eed6024fdb08)
* [Random Forest](https://towardsdatascience.com/understanding-random-forest-58381e0602d2)
* [Support Vector Machines](https://towardsdatascience.com/support-vector-machine-introduction-to-machine-learning-algorithms-934a444fca47)
* [Gaussian Mixture Models](https://towardsdatascience.com/gaussian-mixture-models-explained-6986aaf5a95)
* [k-Nearest Neighbors](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)
* Semantic Segmentation [[1]](https://www.v7labs.com/blog/image-segmentation-guide#traditional-segmentation),[[2]](http://bit.kuas.edu.tw/~jihmsp/2019/vol1/JIH-MSP-2019-01-22.pdf)
* Change Detection [[1]](https://www.mdpi.com/2072-4292/12/11/1781/htm),[[2]](https://www.mdpi.com/2072-4292/12/15/2460)