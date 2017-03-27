
## Download Dataset

* [http://quantquote.com/files/quantquote_daily_sp500_83986.zip](Quantquote sp500 stock dataset)
* Extract its contents on the *data* folder

## Install Instructions

```
$ virtualenv --system-site-packages --python=python3 .venv/
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

## Execute examples

```
$ bokeh serve --show step1.py
```