from . import dataset
from . import helpers
import os
import json
import pandas as pd

class Chung2019(dataset.Dataset):
    
    name = "chung2019"
    url = "https://github.com/marcoguerini/CONAN/raw/master/CONAN.json"
    hash = "511c062b5563affbc78bb2c9d9edafd88fe6419add73b5190865bb42863eacc4"
    files = [
        {
            "name": "chung2019en.csv",
            "language": "en",
            "type": "training",
            "platform": "artifical"
        }
    ]
    license = """This resource can be used for research purposes. Please cite the publication above if you use it."""

    @classmethod
    def process(cls, tmp_file_path, dataset_folder, temp_folder):
        with open(tmp_file_path, "r") as f:
            a = json.load(f)
        b = pd.DataFrame(a['conan'])
        tmp_file_path = tmp_file_path + ".csv"
        b.to_csv(tmp_file_path)
        helpers.copy_file(tmp_file_path, os.path.join(dataset_folder, "chung2019en.csv"))