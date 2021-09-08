# USAGE
# python label_map_builder.py

# import the necessary packages
from pyimagesearch import config
import pandas as pd

# open the classes output file
print("[INFO] preparing the pbtxt file...")
f = open(config.LABEL_MAP, "w")

# loop over the classes
for (k, v) in config.LABEL_ENCODINGS.items():
    # construct the class information and write to file
    item = ("item {\n"
            "\tid: " + str(v) + "\n"
            "\tname: '" + k + "'\n"
            "}\n")
    f.write(item)

# close the output classes file
f.close()