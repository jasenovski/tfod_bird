# USAGE
# python generate_labels.py --dataset --labels dataset/labels.pickle

# import the necessary packages
from pyimagesearch import config
import argparse
import pickle

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--labels", required=True,
    help="path to output labels file")
args = vars(ap.parse_args())

# reverse the label encoding dictionary
labels = {v: k for (k, v) in config.LABEL_ENCODINGS.items()}

# save the class labels to disk
f = open(args["labels"], "wb")
f.write(pickle.dumps(labels))
f.close()