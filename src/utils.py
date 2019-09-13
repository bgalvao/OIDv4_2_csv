import os
from cv2 import imread
import pandas as pd
from tqdm import tqdm


def get_relpaths(root_dir, extensions=['.jpg', '.jpeg', '.png']):
    print('[INFO]: gathering filepaths.')
    def extension_match(filename, extensions):
        for ext in extensions:
            if ext in filename:
                return True
        return False

    file_set = set()
    
    for directory, _, files in os.walk(root_dir):
        # over engineering but ok
        target_filenames = [f for f in files if extension_match(f, extensions)]
        for file_name in target_filenames:
            rel_dir = os.path.relpath(directory, root_dir)
            rel_file = os.path.join(rel_dir, file_name)
            rel_file = os.path.join(root_dir, rel_file)
            file_set.add(rel_file)
    
    return file_set


def get_imgs_dims(img_paths):

    def get_info(path):
        if not os.path.exists(path) and not os.path.isfile(path):
            raise FileNotFoundError('{} not found.'.format(path))
        #print('path is', path)
        height, width, _ = imread(path).shape
        img_id = path.split('/')[-1].split('.')[0]
        return [img_id, width, height]

    print('[INFO]: gathering image ids and dimensions.')
    dickt = {
        img_id: [width, height]
        for img_id, width, height in tqdm(map(get_info, img_paths))
        #FileNotFoundError: width not found.
    }

    print('[INFO]: generating dataframe')
    df = pd.DataFrame.from_dict(
        dickt, orient='index', dtype=int, columns=['width', 'height']
    )
    df.index.name = 'ImageID'
    return df


if __name__ == '__main__':
    
    # for these paths to work, run this from root folder
    # of the repo, i.e. python src/utils.py
    # otherwise cv2.imread returns None
    paths = [
        '../Dataset/train/Dolphin/857c51854276a6aa.jpg',
        '../Dataset/train/Dolphin/acdd33932ceee6da.jpg'
    ]

    df = get_imgs_dims(paths)
    print(df)