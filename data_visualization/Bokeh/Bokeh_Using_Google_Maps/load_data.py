#!/usr/bin/env python

import pandas as pd

df = pd.read_csv("data/cities5000.txt", sep="\t", header=None, usecols=[1, 4, 5, 14], names=["name", "lat", "long", "pop"])

df.to_csv("data/citypop.csv", sep="\t", index=False)