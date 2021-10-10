(Data_pyqgis_gee)=

# Data transfer between Layer to GEE plugin

[PyQGIS](https://docs.qgis.org/3.16/en/docs/pyqgis_developer_cookbook/index.html) is the Python environment inside QGIS. In this tutorial, it helps us to transfer the polygon data from our layer `sao_felix_do_xingu` (region of interest) to GEE.
To achieve this, we need to transform the polygon data into a [polygon object accepted by Google Earth Engine](https://developers.google.com/earth-engine/apidocs/ee-geometry-polygon?hl=en).

```{eval-rst}
.. figure:: ../_static/img_ex2/qgis_gee.png
  :width: 600px
```

:::{warning}
The GEE Timeseries Explorer plugin helped us to understand about GEE in a more interactive way.
However, from this section onwards, it will not be used. 
Only GEE plugin (scripting) will be used.
:::

PyQGIS works for scripting. It can be opened in QGIS from the `Plugins ► Python Console` menu.

```{eval-rst}
.. figure:: ../_static/img_ex2/pyqgis_python_console.png
  :width: 600px
```

Mainly, the Python Console has 3 buttons:

- Clear Console
- Run Command
- Show Editor

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_main_buttons.png
  :width: 200px
```

Clicking the **Show Editor**:

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_click_show_editor.png
  :width: 700px
```

It opens the Editor where we will paste the following lines of code:

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-20
lineno-start: 1
---
```

:::{tip}
In this tutorial, to copy lines of codes from code blocks:

**Move your cursor to the upper right corner and a copy button will appear.**

```{eval-rst}
.. figure:: ../_static/img_ex2/copy_button.png
  :width: 450px
```

:::

With the lines of code copied, paste with the shortcut of your operative system or right click in the Editor and select the `paste` option:

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_editor_paste_action.png
  :width: 300px
```

After pasting the lines, the overview of Python Console will be:

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_pasted_data_transfer.png
  :width: 700px
```

Then, save the script in the current project as **linear_fit.py** filename (in the following chapter this file will be updated)

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_save_script.png
  :width: 400px
```

Doing this, our current directory will be:

```
+--- 2_Trends_Regression
| +--- exercise2.qgz
| +--- points.gpkg
| +--- sao_felix_do_xingu.geojson
| +--- linear_fit.py
```

Recapitulating, the lines of code that we are going to deal with in this section.

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-20
lineno-start: 1
emphasize-lines: 3-6

---
```

The highlighted lines correspond to the **data transfer** stage (our goal in this section) of the total process of this tutorial:

```{eval-rst}
.. figure:: ../_static/img_ex2/qgis_gee_data_transfer.png
  :width: 600px
```

With this, our polygon layer can be transfered to a polygon object accepted by GEE like.

The code described at the beginning will be explained below.

:::{hint}
Our sources on PyQGIS are:

- [QGIS API Documentation](https://qgis.org/api/)
- [QGIS Python API documentation](https://qgis.org/pyqgis/master/)
  :::

:::{tip}
To follow the provided snippet you can click in run button and then explore the variables in the python console:

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_run_script.png
  :width: 600px
```

Or you can run selected lines:

```{eval-rst}
.. figure:: ../_static/img_ex2/python_console_run_selected.png
  :width: 600px
```

:::

## Importing the python ee package

In the first line, `ee` (the Python API package of GEE) is imported.

```{literalinclude} get_trend.py
---
language: python
lines: 1
lineno-start: 1
---
```

## Select our desired polygon layer

This is shown in line 3. In this case, the name of the layer is **sao_felix_do_xingu**

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-16
lineno-start: 1
emphasize-lines: 3
---
```

If you work with temporal layers or layers with similar names, an alternative way to select our desired polygon layer is working with the current active layer in QGIS:

```{code-block} python
roi_layer = iface.activeLayer()
```

To apply this, our current select layer in qgis should be **`sao_felix_do_xingu`** and not other layer.

The variable `roi_layer` is of the type: [`QgsVectorLayer`](https://qgis.org/pyqgis/master/core/QgsVectorLayer.html), it give us hints about which methods we can follow to achieve our goal.

```{code-block} bash
>>> type(roi_layer)
qgis._core.QgsVectorLayer
```

:::{tip}
In this tutorial, when a code starts with `>>>`, as the one above, it means we are debugging the code to check the output of the command line.

You can click to copy the command and then paste it directly to the Python Terminal.
:::

## Extract polygon geometry

With `roi_layer` we need to extract the geometry (polygon's vertices) of our desired polygon.
In this case, **`roi_layer.getFeatures()`** return us an [iterator](https://anandology.com/python-practice-book/iterators.html#the-iteration-protocol). For this reason, the **next** method is used.

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-17
lineno-start: 1
emphasize-lines: 4
---
```

An anternative way to do this, is to convert the iterator into a list and then get its first element (because in this case, there is only 1 polygon):

```{code-block} python
roi_geometry = list(roi_layer.getFeatures())[0].geometry()
```

The variable polygon_geometry is of the type: [`QgsGeometry`](https://qgis.org/pyqgis/master/core/QgsGeometry.html), it brings us closer to our goal.

```{code-block} bash
>>> roi_geometry
<QgsGeometry: Polygon ((-50.91863399759999709 -5.15029175370000036,
                        -50.90714271939999946 -5.1636283516999999,
                        -50.89869634709999957 -5.1568509627000001...>
```

## Obtaining points from geometry

In PyQGIS, the way to get the points from a geometry (`QgsGeometry`) is through the **asPolygon** method.

```{code-block} bash
>>> roi_geometry.asPolygon()
[[<QgsPointXY: POINT(-50.91863399759999709 -5.15029175370000036)>,
 <QgsPointXY: POINT(-50.90714271939999946 -5.1636283516999999)>,
 <QgsPointXY: POINT(-50.89869634709999957 -5.1568509627000001)>,
 ...
 <QgsPointXY: POINT(-50.91863399759999709 -5.15029175370000036)>]]
```

In our case, our region of interest is 1 polygon. This is the reason why the points are the first element (index zero) of the returned list by **asPolygon** method:

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-18
lineno-start: 1
emphasize-lines: 5
---
```

The variable `points` is of the type **list**:

```{code-block} bash
>>> type(points)
<class 'list'>
```

```{code-block} bash
>>> points
[<QgsPointXY: POINT(-50.91863399759999709 -5.15029175370000036)>,
 <QgsPointXY: POINT(-50.90714271939999946 -5.1636283516999999)>,
 <QgsPointXY: POINT(-50.89869634709999957 -5.1568509627000001)>,
 ...,
 <QgsPointXY: POINT(-50.91863399759999709 -5.15029175370000036)>]
```

## Create list of vertices

The variable `points` contains the polygon vertices, we need to format them to be accepted by **ee.Geometry.Polygon** method.

```{code-block} python
ee.Geometry.Polygon([
  [-50.9186339976, -5.1502917537],
  [-50.9071427194, -5.1636283517,
  [[-50.8986963471, -5.1568509627,
  ...
  [-50.9186339976, -5.1502917537]
])
```

To achieve this, we need to analyze an element of `points` which is a [**QgsPointXY**](https://qgis.org/api/classQgsPointXY.html) type:

```{code-block} bash
>>> points[0]
<QgsPointXY: POINT(-50.91863399759999709 -5.15029175370000036)>
```

To extract the coordinates we can use the **x** and **y** methods:

```{code-block} bash
>>> points[0].x()
-50.91863399759999709
>>> points[0].y()
-5.15029175370000036
```

Using a [List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp) with the methods **x** and **y** of `QgsPointXY`, we can get the desired list of vertices:

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-19
lineno-start: 1
emphasize-lines: 6
---
```

```bash
>>> list_vertices
[[-50.9186339976, -5.1502917537],
 [-50.9071427194, -5.1636283517],
 [-50.8986963471, -5.1568509627],
 ...
 [-50.9186339976, -5.1502917537]]
```

## Build an Earth Engine polygon

With `ee.Geometry.Polygon` we can have the input for our linear model:

```{literalinclude} get_trend.py
---
language: python
lines: 1, 15-20
lineno-start: 1
emphasize-lines: 7
---
```

```{code-block} bash
>>> type(polygon_ee)
<class 'ee.geometry.Geometry'>
```
