
## Download Dataset

* Download the *cities5000.zip* from [http://download.geonames.org/export/dump/](Geonames portal)
* Extract the file on the *data* folder and run the following:

```
python load_data.py
```

## Get a GOOGLE API KEY

* You need an GOOGLE MAPS API KEY to use the examples. Remember to set it on the .py files

## Running the Examples

```
bokeh serve --show step1.py
bokeh serve --show step2.py
bokeh serve --show step3.py
```