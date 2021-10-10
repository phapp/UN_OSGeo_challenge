# General Configuration

## Working Directory

Let's define a working directory, for instance: `Documents/1_Change_Detection`. Now, create a new QGIS project in our working directory. Our project’s name will be **exercise1**. Then, create the following folders to save all the necessary files for this tutorial: **Clip**, **Images**, **Preprocess**, **Reports**, **Results** and **Stacks**.

So, the initial structure of our working directory is the following: 

```
+--- 1_Change_Detection
|   +--- Clip
|   +--- exercise1.qgz
|   +--- Images
|   +--- Preprocess
|   +--- Reports
|   +--- Results
|   +--- Stacks
```

## Select area of study

Our study area is located in the Huaraz region, where its capital, Huaraz city, is located in Peru's northern Callejón de Huaylas valley. The city sits more than 3,000 meters above sea level, with the snow-capped peaks of the Cordillera Blanca range forming its dramatic eastern skyline. Encompassing much of the Cordillera Blanca is Huarascán National Park, home to Andean condors and jaguars as well as Peru's tallest mountain, Huascarán.

Huascarán mountain is the focus of this tutorial, where with the help of Quantum GIS and some plugins for supervised classification, we will monitor the evolution of its snow-capped peak during the last 5 years.

```{eval-rst}
.. figure:: ../_static/img_ex1/1_huascaran.jpg
  :name: huascaran_mountain
  :width: 600px

  Huascarán mountain, the highest point in Peru (elevation: 6768 meters).
```

## Create account for Earth Explorer

We are going to work with [Landsat 8](https://www.usgs.gov/core-science-systems/nli/landsat/landsat-8?qt-science_support_page_related_con=0#) images, so it is necessary to have an account to download Landsat products.

In case you do not have an account, go to [this link](https://ers.cr.usgs.gov/register) to create it.

Just enter a _username_ and _password_, validate the captcha, and then click on **Continue**.

```{eval-rst}
.. figure:: ../_static/img_ex1/2_create_user.png
  :name: create-user
  :width: 400px
```

Complete the form and enter your contact information to create an account.

:::{note}
Remember to save the **_username_** and **_password_** as we will need them later.
:::

## Setting Up SCP to download images

In order to download Landsat 8 products, we will use the **Semi-Automatic Classification Plugin - SCP** for QGIS. A detailed explanation about how to install SCP can be found in [this link](https://fromgistors.blogspot.com/2016/11/install-scp-from-repository.html).

Once SCP is installed in QGIS, go to **SCP->Download products**

```{eval-rst}
.. figure:: ../_static/img_ex1/3_scp_download_products.png
  :width: 250px
  :name: scp-download-products
```

Then, click on tab **Login data** to add the credentials for the products to be downloaded

```{eval-rst}
.. figure:: ../_static/img_ex1/4_scp_login_data.png
  :width: 800px
  :name: scp-login
```
