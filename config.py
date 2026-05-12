# config.py
# setting up all the paths and basic config for the project
# will keep adding stuff here as project grows

import os

# base directory - where the project lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# data folders
DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")

# model and report output folders
MODELS_DIR = os.path.join(BASE_DIR, "models")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# flask stuff
FLASK_PORT = 5000
DEBUG = True

# for ml models
RANDOM_STATE = 42
TEST_SIZE = 0.2

if __name__ == "__main__":
    print("config loaded, paths are set")
    print("BASE_DIR:", BASE_DIR)
