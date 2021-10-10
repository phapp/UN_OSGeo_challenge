# Change Detection

## Quantifying the changes

To quantify the **Snow Cover** areas in each date, we need to count the number of pixels belonging to this class. Fortunately, **SCP** has a function to perform it. Go to **SCP->Postprocessing->Classification report**. 

```{eval-rst}
.. figure:: ../_static/img_ex1/46_scp_classification_report.png
  :width: 300px
  :name: scp-classification-report
```

We only need to select the raster layer with the classification output. Click on the **Refresh** button, then, click on **Run**.

```{eval-rst}
.. figure:: ../_static/img_ex1/47_scp_classification_report_parameters.png
  :width: 800px
  :name: scp-classification-report-parameters
```
You will be asked to enter the name of the report file. Let’s create a folder in the working directory: **Reports**, and name the file as **2016.csv**. 

:::{note}
Remember: A _Comma Separated Value_ or _CSV_ file is a delimited text file that uses a comma to separate values. Each line of the file is a data record, and each record consists of one or more fields, separated by commas.
:::

This file can be opened with any text editor, for instance: _Notepad_. 

There are the following columns:
- **_Class_**: class index as were defined. In this case: 1: **Background*, and 2: **Snow Cover**.
- **_PixelSum_**: Number of pixels of a class.
- **_Percentage %_**: Percentage of pixels that a class represents.
- **_Area [metre^2]_**: Area of each class in the project’s units, in this case: square meters. 

```{eval-rst}
.. figure:: ../_static/img_ex1/48_scp_classification_report_result.png
  :width: 800px
  :name: scp-classification-report-result
```

:::{important}
To change project`s units, go to **Project->Properties…->General**, and in the **Measurements** section, select the units for _distance_ and _area measurements_. 
:::

After repeating these steps for all images, we get the following table for the class **Snow Cover**, where the area was converted to square kilometers for an easier comparison.

|    Date    | Area (km2) | Pixels | Percentage % |
|:----------:|:----------:|:------:|:------------:|
| 2021-07-15 |   316.73   | 351921 |     8.27     |
| 2020-07-28 |   303.57   | 337295 |     7.93     |
| 2019-07-10 |   320.84   | 356492 |     8.38     |
| 2018-07-07 |   331.43   | 368261 |     8.66     |
| 2016-11-22 |   272.80   | 303106 |     7.13     |

A clear pattern can be seen from **2018** to **2020**, where the percentage of **Snow Cover** gradually diminishes. However, the same does not happen from **2016** to **2018**, and from **2020** to **2021**. In order to understand what happened in those years, we will compare the produced masks.

## Comparison of masks

For a better understanding of the changes between each date, let’s create maps with the **_added_** or **_removed_** areas between different years using the **Raster Calculator**. 

Go to **Raster->Raster Calculator**. First, compute the difference between masks from **2016** and **2018**. In **Raster Bands**, double click on the layer **result_2016-11-22@1**, click on operator **“-”**, and double click on layer **result_2018-07-07@1**. In the **Output layer**, write the name of the output file: **Results/2016-2018**, **Output format**: **GeoTIFF**. And click on **OK**.

```{eval-rst}
.. figure:: ../_static/img_ex1/49_raster_calculator_difference.png
  :width: 800px
  :name: raster-calculator
```

A new layer is added to the project with values: **0**, **1** and **-1**. For a better visualization, change the colormap. **Right click** on the layer, and go to **Properties->Symbology**:
- In _Render Type_ select _Singleband pseudocolor_.
- _Mode_: _Equal Interval_
- _Classes_: 3. 

Finally, edit the colors in the following way: 
**-1**: <span style="color: green;"><b>Green</b></span>, 
**0**: Transparent, and 
**1**: <span style="color: red;"><b>Red</b></span>. Click on **Apply** and **OK**.

```{eval-rst}
.. figure:: ../_static/img_ex1/50_difference_2016-2018.png
  :width: 400px
  :name: difference_2016-2018
```

According to the selected colormap, as the difference between **2016** and **2018** was computed, the **Transparent** color represents the areas that have not changed. The color <span style="color: red;"><b>Red</b></span> describes the areas that had **Snow Cover** in **2016**, but do not in **2018**. Finally, the <span style="color: green;"><b>Green</b></span> color shows the areas that did not have **Snow Cover** in **2016**, but now do in **2018**. 

```{eval-rst}
.. figure:: ../_static/img_ex1/51_explanation_masks_difference.png
  :width: 300px
  :name: difference_explanation
```

Repeat the same procedure for the masks from the years **2020** and **2021**.

```{eval-rst}
.. figure:: ../_static/img_ex1/52_years_difference.png
  :width: 800px
  :name: difference_2016-2021
```

## Analysing the results

Now that we have generated the difference between masks, let’s analyze them. 

For instance, the difference between **2016** and **2018**. The following snip shows big <span style="color: green;"><b>green</b></span> areas, which could lead us to think that the quantity of **Snow Cover** has increased between these years. However, comparing the images from **2016** and **2018**, it can be seen that these green areas were covered by clouds in **2016**, and did not in **2018**. For that reason, the **Snow Cover** areas increased according to **2018’s** mask. This would be the main reason for the **Snow Cover** percentage growth from **2016** to **2018**.

```{eval-rst}
.. figure:: ../_static/img_ex1/53_2016-2018_cut1.png
  :width: 900px
  :name: 2016-2018_cut1
```

:::{important}
Notice that the classifier correctly discriminated between **Clouds** and **Snow Cover**, producing accurate masks.
:::

Taking a look at another snip, we can see how the **Snow Cover** diminishes (<span style="color: red;"><b>red</b></span> areas) on the top of the mountains, maybe due to snow melting. Moreover, the **Snow Cover** area expands its coverage in the mountains boundaries (<span style="color: green;"><b>green</b></span> areas), perhaps because of some snow slides.

```{eval-rst}
.. figure:: ../_static/img_ex1/54_2016-2018_cut2.png
  :width: 900px
  :name: 2016-2018_cut2
```

A similar behaviour can be seen between **2020** and **2021**, where the percentage of **Snow Cover** increased from **7.93%** to **8.27%**, approximately. However, due to the presence of clouds, we can not say that this is very accurate.

```{eval-rst}
.. figure:: ../_static/img_ex1/55_2020-2021_cut.png
  :width: 900px
  :name: 2020-2021_cut
```
