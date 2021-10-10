# Machine Learning with Earth Observation data: Case studies with Semantic Segmentation and Regression
Material for 2021 UN Open GIS Challenge 1 - Training on Satellite Data Analysis and Machine Learning with QGIS (Satellite_QGIS)

![Challenge](./source/_static/header_fig.png?raw=true "UN OSGeo Challenge")


Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


## Instructions

### Using Poetry Python

- [Install Poetry Python](https://python-poetry.org/docs/#installation)
- Run: `poetry shell`
- Inside the opened environment, run `make html`

```bash
$ poetry shell
.venv> make html
```

Sometimes it is necessary to clean the build folder:

```bash
$ poetry shell
.venv> make clean
```

### Using pip

- Activate your virtual environment
- Execute `pip install -r requirements.txt`
- Inside the opened environment, run `make html`
