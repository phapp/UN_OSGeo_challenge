# Semantic Segmentation

## Training the algorithm for semantic segmentation

The samples to train the algorithm for semantic segmentation are ready in the **training.shp** file. As the samples were collected using the image from **2016-11-22** as reference, this image is our train set. Then, the other images will be our test set.

| Data       |   Set |
| :--------- | ----: |
| 2021-07-15 |  Test |
| 2020-07-28 |  Test |
| 2019-07-10 |  Test |
| 2018-07-07 |  Test |
| 2016-11-22 | Train |
| 2015-09-01 |  Test |

We are going to use the rasters with the stack of all bands. In this case, to train the Random Forest algorithm the file **Stack_2016-11-22.tif** is used.

Create a folder to save the segmentation results: **Results**, in the project directory. Now, let’s open the **dzetsaka plugin** to perform the segmentation. It is necessary to define the following parameters:

- _The image to classify_: select the raster layer **Stack_2016-11-22**.
- _Your ROI_: select the vector layer **training.shp** with the training samples.
- _Column name where class number is stored_: it is the id column from the **training.shp** file.
- _Result filename_: **Results/result_2016-11-22.tif**.
- Enable the _Save Model_ option and enter a name for the model: **Results/model_RF**.
- Click on the **Settings** button (⚙️), and select any classification algorithm. For instance, **Random Forest**.
- Finally, click on **Perform the classification**.

```{eval-rst}
.. list-table::

    * - .. figure:: ../_static/img_ex1/39_dzetsaka_parameters.png
           :width: 600px           

      - .. figure:: ../_static/img_ex1/40_dzetsaka_parameters_2.png
           :width: 300px           
```

:::{warning}
It might be necessary to install some libraries in order to execute different Machine Learning algorithms.

The plugin will inform you if any library is missing and it will indicate the instructions to install it.

For instance, the plugin will provide a link as [this](https://github.com/nkarasiak/dzetsaka#installation-of-scikit-learn).

After installing the required library, it may be necessary to restart QGIS.
:::

A new layer with the result is added to the project. It is a binary image with values of 1 and 2 for the classes **Background** and **Snow Cover**, respectively.

```{eval-rst}
.. figure:: ../_static/img_ex1/41_classification_map_2016.png
  :name: binary-image
  :width: 600px
```

:::{note}
Random Forest training involves process where random selections are performed. Thus, the obtained result would be slightly different every time the training step is executed.
:::

Let’s change the colors for a visualization. **Right click** on the layer and select **Properties**. Go to **Symbology**, and in **Render Type**, select **Singleband pseudocolor**. In **Mode**, select **Equal Interval**, and set **Classes** to **2**. Change the color for each class by double clicking their square color.

As we are only interested in the **Snow Cover** class, the class **Background** will be assigned a transparent color.

```{eval-rst}
.. figure:: ../_static/img_ex1/42_classification_map_2016_layout.png
  :width: 800px
  :name: apply-singleband
```

:::{note}
For more information about how to change vector layer's style, visit the following links: [[1]](https://www.qgistutorials.com/en/docs/basic_vector_styling.html),[[2]](https://www.youtube.com/watch?v=CmK73b_e36g&ab_channel=RobinLovelace)
:::

Finally, click on **Apply**.

```{eval-rst}
.. figure:: ../_static/img_ex1/43_classification_map_2016_colors.png
  :width: 600px
  :name: snow-cover-class
```

As we can see, the **Random Forest** managed to distinguish between **Snow** and **Clouds**. If it is necessary, we can change the training polygons to add more samples, just edit the vector layer **training.shp**, and design more polygons where the **Random Forest** made some mistakes. This can happen if there are not enough samples for training, or the variability of them is low. So, increase more polygons and perform the classification many times until you see a good result.

:::{attention}
Remember that this image is our training set, so we can add more training samples. 

We **can not take samples from other images** as they are the test set, a set that the classifier **only sees** after training.
:::

Other classification algorithms can be selected in this step. The **dzetsaka plugin** provides the following algorithms: Random Forest (RF), Support Vector Machines (SVM), Gasussian Mixture Models (GMM), and k-Nearest Neighbors (KNN). There are slightly differences between the classification results obtained by each algorithm:

```{eval-rst}
.. figure:: ../_static/img_ex1/43_1_classification_comparison.png
  :width: 900px
  :name: comparison-classification-algorithms
```

:::{note}
We will continue this tutorial using Random Forest due to its simplicity and processing speed to perform many different test.
:::

## Generation of masks for each date

Now that the classification algorithm has been trained, we can perform inference over the test set. Remember that during training, the model was saved in the file **Results/model_RF**.

For inference, we need to configure the following parameters:

- _The image to classify_: select the raster layer **Stack_2021-07-15**.
- Enable the **Load model** option and select the trained model: **Results/model_RF**.
- _Result filename_: **Results/result_2021-07-15.tif**.
- Finally, click on **Perform the classification**.
- Disable the _Save Model_ option (it is optional as this parameter is not considered for inference).

```{eval-rst}
.. figure:: ../_static/img_ex1/44_prediction_2021.png
  :width: 600px
  :name: rf-stack-2021-07-15
```

A new layer with the result is added to the project. Again, it is a binary image with values of **1** and **2** for the classes **Background** and **Snow Cover**, respectively. 

Let’s change the colormap for a better visualization. As we already defined a colormap for the result of the training, we can copy it for this image. Just **right click** on the layer **result_2016-11-22**, go to **Styles->Copy Style**; then, right click on the layer **result_2021-07-15**, go to **Styles->Paste Style**.

```{eval-rst}
.. figure:: ../_static/img_ex1/45_classification_maps_2016_2021.png
  :width: 800px
  :name: results_2016_and_2021
```
Repeat the same procedure for all images in the test set: **2020-07-08**, **2019-07-10**, and **2018-07-07**.

## Accuracy Assessment

In this application, there is not a reference (ground truth) with the correct labels for each date.

However, if you have a reference file (raster or vector), you can employ SCP to perform an accuracy assessment.

Go to **SCP->Postprocessing->Accuracy**. We need to provide the following parameters (click on the **Refresh** button to see the layers in the project):
* _Select the classification to assess_: this is the classification output obtained by the classification algorithm.
* _Select the reference vector or raster_: this is the reference (ground truth). If it is a vector, select the _Vector field_ with the corresponding labels.

Just for testing purposes, let's use the same layer in both cases: **result_2021-07-15**.

```{eval-rst}
.. figure:: ../_static/img_ex1/45_scp_accuracy_assessment.PNG
  :width: 800px
  :name: scp-accuracy-assessment
```

:::{important}
Remember, in a real scenario, use the layers with the classification output and its corresponding reference (groud truth).
:::

Click on **Run**. You will be asked to enter a filename to save the results. For instance: **Reports/accuracy**.

Two files are created in the **Reports** folder: **accuracy.csv** and **accuracy.tif**. Also, the output of the accuracy assessment is presented.

```{eval-rst}
.. figure:: ../_static/img_ex1/45_scp_accuracy_assessment_output.PNG
  :width: 800px
  :name: scp-accuracy-assessment-output
```

In the output, you can find the **ErrMatrixCode**, where each number represents a combination between pixel values of the **Reference** and the **Classification output**. 

In this case, as they are the same, there are only two values: **1** and **4**, for the combinations _1:1_ and _2:2_, respectively. These values are also represented in the file **accuracy.tif**, where each pixel takes one of those values.

In a real scenario, there would be more combinations: _1:1_, _1:2_, _2:1_, and _2:2_, as the **Classification output** usually missclassify some pixels.

:::{note}
Remember, there are only two classes in this case: 1 (Background), and 2(Snow Cover).
:::

There are many different metrics in the output such as the **Overall accuracy** and **Kappa hat classification**. This report is also available in the file **accuracy.csv**.