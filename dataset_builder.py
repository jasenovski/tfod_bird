# USAGE
# python dataset_builder.py

# import the necessary packages
from pyimagesearch import config
import pandas as pd
import numpy as np 
import random
import os

def extractClassName(string):
	# extract the class name accordingly from the given string
	# and then return it
	return string.split(".")[1].split("/")[0]

# load the text files in dataframes with descriptive column names
# as needed
print("[INFO] loading .txt files...")
imagePaths = pd.read_csv(config.IMAGE_PATH, header=None, 
    sep = " ", names=["image_id", "image_path"])
boundingBoxes = pd.read_csv(config.BOUNDING_BOXES, header=None,
	sep=" ", names=["image_id", "x", "y", "width", "height"])
trainTestSplit = pd.read_csv(config.TRAIN_TEST_SPLIT, header=None,
    sep = " ", names=["image_id", "is_training_image"])

# extract the class names from the image paths and add them in a
# new column inside the images dataframe
classNames = imagePaths["image_path"].map(extractClassName)
imagePaths["class"] = classNames

# calculate (x,y) coordinates, add them to the appropriate dataframe,
# and change the data type of the coordinates to integer
boundingBoxes["xmax"] = boundingBoxes["x"] + boundingBoxes["width"]
boundingBoxes["ymax"] = boundingBoxes["y"] + boundingBoxes["height"]
cols = ["x", "y", "width", "height", "xmax", "ymax"]
boundingBoxes[cols] = boundingBoxes[cols].astype("int")

# merge the image paths and bounding boxes data frames 
mergedDF = pd.merge(imagePaths, boundingBoxes, on="image_id")

# create a new data frame with the specified columns
interimDF = pd.DataFrame()
dataFrameCols = ["image_id", "filename", "width", "height",
	"class", "xmin", "ymin", "xmax", "ymax"]

# loop over each column in the newly created data frame
for col in dataFrameCols:
	# change the names of a few columns so that we don't run into 
	# errors while etrieving them from the merged data frame
	if col == "filename":
		col = "image_path"
	elif col == "xmin":
		col = "x"
	elif col == "ymin":
		col = "y"

	# copy over the rows from the merged data frame to the 
	# intermediate dataframe
	interimDF[col] = mergedDF[col]

# rename the columns in our intermediate data frame so that it is 
# compatible for generating TFRecords
interimDF.rename(columns={
    "image_path": "filename",
    "x": "xmin",
    "y": "ymin"
	}, inplace=True)

# merge the intermediate and train/test dataframes 
interimDF = pd.merge(intermDF, trainTestSplit, on="image_id")

# get the indexes of the test data points
testKeys = interimDF["is_training_image"] == 0
testSamples = interimDF.index[testKeys].tolist()

# drop the test data point indexes from the intermediate data frame,
# assign the rest of the data points as training data points, and
# extract the test data points 
trainDF = interimDF.drop(index=testSamples).reset_index(drop=True)
testDF = interimDF.iloc[testSamples].reset_index(drop=True)

# drop the two columns from train and test data frames 
# as they won't be required
trainDF.drop(["image_id", "is_training_image"], axis=1, inplace=True)
testDF.drop(["image_id", "is_training_image"], axis=1, inplace=True)

# initialize an empty list to store the predefined top-20 labels
labels = []

# loop over the keys of the encoding dictionary and add them to
# the list
for (key, _) in config.LABEL_ENCODINGS.items():
    labels.append(key)

# extract the data points from train and test data frames with
# respect to labels
trainDFSmall = trainDF[trainDF["class"].isin(labels)]
testDFSmall = testDF[testDF["class"].isin(labels)]

# serialize the CSV data to disk
print("[INFO] serializing the dataframes...")
trainDFSmall.to_csv(config.TRAIN_LABELS, index=False)
testDFSmall.to_csv(config.TEST_LABELS, index=False)