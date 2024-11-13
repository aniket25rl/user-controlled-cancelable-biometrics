

import os
import shutil
from pathlib import Path




BASE_DIR = Path().resolve()
print(BASE_DIR)

NEW_DATASET_PATH = r"dataset/NEW_DB"

def organize_user_files(src : str) :
    """
    Used to create new dataset from the existing dataset with organized user files.

    Parameters : 
        src (str) - Path of existing dataset

    
    """

    os.chdir(src)

    try : 
        # Create folder NEW_DB
        os.mkdir(os.path.join(BASE_DIR , NEW_DATASET_PATH))

    except FileExistsError :
        pass


    for filename in os.listdir() : 

        user , template = filename.split("_")
        user_dir_path = os.path.join(BASE_DIR , NEW_DATASET_PATH , user)

        try :     
            # Create user folder 
            os.mkdir(user_dir_path)

        except FileExistsError :
            pass

        finally :
            # Move the file to user folder
            shutil.move(filename ,  user_dir_path)

if __name__ == "__main__" :
    DATASET1 = r"dataset/DB1_A"
    organize_user_files(DATASET1)
