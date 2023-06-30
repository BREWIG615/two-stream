# Two Stream

This module implements a simple version on the `two stream` application. The program is designed to import a simple excel database, perhaps postgesql in the future, allow the user to interact and even modify the data. This is meant to model a way to capture both the programing and rm data in a central location. Additionally the last piece will be to add a button that will convert the export to an encoded hexadecimal csv file. Additionally, while it wont be a part of the plotly application itself I will include another script that can also unscramble the hex to plain text so as to provide our higher headquarters with tangible results as they are not grasping the theoretical concept and this will hopefully provide them more fidelity.

## Dependencies
This is a `python3` package with the following python package dependencies.

* `Babel`
* `dash`
* `dash-bootstap-components`
* `pandas`
* `pandas-stubs`
* `plotly`
* `python-i18n[YAML]` note this package is only required if you wish to display the application in a different language otherwise you do nor require this package.

### Installation in a virtual environment

First, create a virtual environment.

```sh
python3 -m venv env
source env/bin/activate
```

```sh
pip install -r ./environment/requirements.txt
```
