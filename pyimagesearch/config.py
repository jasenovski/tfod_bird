# import the necessary packages
import os

# base path of the Caltech UCSD Birds dataset
DATA_PATH = os.path.sep.join(["dataset", "CUB_200_2011"])

# path to the files that contain the image filenames, bounding box
# annotations, and information about dataset splits
IMAGE_PATH = os.path.sep.join([DATA_PATH, "images.txt"])
BOUNDING_BOXES = os.path.sep.join([DATA_PATH, "bounding_boxes.txt"])
TRAIN_TEST_SPLIT = os.path.sep.join([DATA_PATH, 
	"train_test_split.txt"])

# path to the CSV files for training and evaluations sets
TRAIN_LABELS = os.path.sep.join(["dataset", "train_labels.csv"])
TEST_LABELS = os.path.sep.join(["dataset", "test_labels.csv"])

# path to the file that contains the IDs of the different
# classes of birds
LABEL_MAP = os.path.sep.join(["dataset", "label_map.pbtxt"])

# a dictionary containing that maps the different classes of birds
# to integers 
LABEL_ENCODINGS = {"Bobolink": 1, 
	"Gray_Catbird": 2, 
	"Yellow_billed_Cuckoo": 3, 
	"Acadian_Flycatcher": 4, 
	"Great_Crested_Flycatcher": 5, 
	"Northern_Fulmar": 6, 
	"Pigeon_Guillemot": 7, 
	"Green_Kingfisher": 8, 
	"White_breasted_Kingfisher": 17, 
	"White_crowned_Sparrow": 10, 
	"Bank_Swallow": 11, 
	"Barn_Swallow": 12, 
	"Forsters_Tern": 13, 
	"White_eyed_Vireo": 14, 
	"Black_and_white_Warbler": 15, 
	"Cerulean_Warbler": 16, 
	"Northern_Waterthrush": 18, 
	"Cactus_Wren": 19, 
	"Marsh_Wren": 20
}