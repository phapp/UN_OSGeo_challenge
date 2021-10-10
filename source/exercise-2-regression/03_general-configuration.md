# General Configuration

## Working directory

Let's define a working directory, for instance: `Documents/2_Trends_Regression`. Now, create a new QGIS project in our working directory. Our project’s name will be **exercise2**.

So, the initial structure of our working directory is the following:

```
+--- 2_Trends_Regression
| +--- exercise2.qgz
| +--- points.gpkg
| +--- sao_felix_do_xingu.geojson
```

The files used in this tutorial `points.gpkg` and `sao_felix_do_xingu.geojson` can be downloaded from [here](https://zenodo.org/record/5511994).

## Select area of study

Our study area is a municipality called São Félix do Xingu, in the state of Pará, in the Northern part of Brazil. This municipality contains part of:

- Tapirapé Biological Reserve, created in 1989
- Tapirapé-Aquiri National Forest, created in 1989
- Terra do Meio Ecological Station, created in 2005
- Serra do Pardo National Park, created in 2005

```{eval-rst}
.. figure:: ../_static/img_ex2/working_directory.png
  :name: ex2_initial
  :width: 600px

  Layers from the 2 initial files.
```

São Félix do Xingu is the focus of this tutorial, thus you can load the files `points.gpkg` and `sao_felix_do_xingu.geojson` to the project. We will monitor the deforestation trend of this area from 2017 to 2020.

In order to see the point labels (P1, P2 and P3), we need to choose the `Single Labels` option and `Name` as **attribute value** in Labels menu from Layer Properties of our Layer `points`.

```{eval-rst}
.. figure:: ../_static/img_ex2/name_single_label.png
  :width: 700px
```

The file `sao_felix_do_xingu.geojson` was generated from [Pará Municipalities](https://github.com/tbrugz/geodata-br/blob/master/geojson/geojs-15-mun.json)

The file `points.gpkg` contains 3 sampled points that are inside São Félix do Xingu.

The points were generated from `Vector ► Research Tools ► Random Points in Polygons` menu. You can check [this link](https://www.youtube.com/watch?v=A-nloh5jYvY) for more details.

If you want to work with your own region of interest, you can create your customized polygon layer.
With respect to the points, you can create random sample points or draw specific points according to your needs.

## Create account for Google Earth Explorer

We are going to work with Landsat 8 images. For using GEE to process algorithms in the cloud, you will need an account in Google Earth Engine.

In case you do not have an account:
1. Go to [this link](https://signup.earthengine.google.com).
2. Complete the form and submit the requested information to create an account.

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_signup.png
  :width: 600px
```

When you are accepted, you will receive an email like this:

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_account_confirmation.png
  :width: 600px
```

:::{important}
Remember to save the **username** and **password** as we will need them later.
:::

## Setting the plugins

Go to `Plugins ► Manage and Install Plugins` menu. You will need to install 2 plugins:
1. Google Earth Engine 
2. GEE Timeseries Explorer (requirement: Google Earth Engine plugin)

### Google Earth Engine Plugin

Our first plugin to install is [Google Earth Engine](https://gee-community.github.io/qgis-earthengine-plugin/) (it lets us handle GEE resources with Python). Do not forget to check this plugin after the installation is concluded. You can follow this [external tutorial](https://www.geodose.com/2019/12/google-earth-engine-qgis-plugin-tutorial.html).

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_plugin.png
  :width: 600px
```

> The plugin checks if the user is authenticated to use the GEE. If this is not the case, the user will be asked to authenticate later.

This authentication is done using the email registered on Google Earth Engine account.

To check if the plugin is working, we need to open the Python Console in QGIS (`Plugins ► Python Console`) and type: **import ee**

:::{important}
[The QGIS Python Console](https://docs.qgis.org/3.16/en/docs/user_manual/plugins/python_console.html) is installed by default.
:::

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ok.png
  :width: 600px
```

If no error appears, the installation process was successful.

### GEE Timeseries Explorer

Requirement: Google Earth Engine Plugin installation

Search and install in QGIS/Plugins: GEE Timeseries Explorer

```{eval-rst}
.. figure:: ../_static/img_ex2/gee_ts.png
  :width: 600px
```

