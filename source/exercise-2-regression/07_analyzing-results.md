# Analysing the Results

We can compare our calculated trend with historical trends in tree cover loss and gain from [Global Forest Watch](https://www.globalforestwatch.org/map). As we can see, trends have similarities.

```{eval-rst}
.. figure:: ../_static/img_ex2/trend_comparison_rect.png
  :width: 600px
```

The colors used for slope values in linear fit:

- The red color indicates NDVI negative variation: loss.
- The green color indicates NDVI positive variation: gain,
- The creme color indicates approximately that there is no NDVI variation.

Even with this simple model, it is possible to see similar trends.
Better results can be expected when working with more robust models.

The estimated deforested area, computed by our simple model, is 25,976 {math}`Km^2`, more than double of [Sydney city area](https://www.britannica.com/place/Sydney-New-South-Wales).

```{code-block} python
>>> print(f"Deforested area: {area_km2:,.0f} (km^2)")
'Deforested area: 25,976 (km^2)'
```
