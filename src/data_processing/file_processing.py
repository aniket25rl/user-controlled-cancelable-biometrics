

import os
import shutil
from pathlib import Path




BASE_DIR = Path().resolve()
print(BASE_DIR)

DATASET1 = r"dataset/DB1_A"
DATASET2 = r"dataset/NEW_DB"
os.chdir(DATASET1)

try : 
    # Create folder NEW_DB
    os.mkdir(os.path.join(BASE_DIR , DATASET2))

except FileExistsError :
    pass


for filename in os.listdir() : 

    user , template = filename.split("_")
    user_dir_path = os.path.join(BASE_DIR , DATASET2 , user)

    try :     
        # Create user folder 
        os.mkdir(user_dir_path)

    except FileExistsError :
        pass

    finally :
        # Move the file to user folder
        shutil.move(filename ,  user_dir_path)
