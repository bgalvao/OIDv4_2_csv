from os.path import dirname
from os import makedirs
import argparse
import pandas as pd

from src.utils import get_relpaths, get_imgs_dims

parser = argparse.ArgumentParser(
    description='Make VOC-csv annotation from images downloaded' + \
        ' using OIDv4_Toolkit. This tool was created to create a suitable ' + \
        'format for the https://github.com/Tony607/object_detection_demo' + \
        ' boilerplate from the OIDv4 dataset downloaded using ' + \
        'https://github.com/EscVM/OIDv4_ToolKit'
)

parser.add_argument(
    '--imgs_source', '-i', default='../Dataset/validation',
    help='Source folder where images are. Will walk recursively.'
)

parser.add_argument(
    '--output_csv_filename', '-o',
    default='../Dataset/csv_folder/train_voc.csv',
    help='Where to write the output csv file to.'
)

parser.add_argument(
    '--annotations_file_path', '-a',
    default='../csv_folder/validation-annotations-bbox.csv',
    help='Path to csv annotations file provided by OID. Do recommend ' + \
        'to make your own smaller annotations file of classes of interest.'
)

parser.add_argument(
    '--labels_file_path', '-l',
    default='../csv_folder/class-descriptions-boxable.csv',
    help='Path to csv annotations file provided by OID. Do recommend ' + \
        'to make your own smaller annotations file of classes of interest.'
)

args = parser.parse_args()

_SOURCE = args.imgs_source
_DESTINATION = args.output_csv_filename
_ANNOTATIONS_PATH = args.annotations_file_path
_LABELS_PATH = args.labels_file_path

if __name__ == '__main__':

    img_paths = get_relpaths(_SOURCE)
    df = get_imgs_dims(img_paths)

    annotations = pd.read_csv(_ANNOTATIONS_PATH)
    labels = pd.read_csv(_LABELS_PATH, header=None)
    labels.columns = ['LabelName', 'class']
    ann = annotations.set_index('LabelName').join(labels.set_index('LabelName'))         
    df = df.join(ann.set_index('ImageID')).drop(
        ['Source', 'Confidence'],
        axis=1
    )
    del annotations, ann, labels

    df['xmin'] = (df.XMin * df.width).round(0).astype(int)
    df['xmax'] = (df.XMax * df.width).round(0).astype(int)
    df['ymin'] = (df.YMin * df.height).round(0).astype(int)
    df['ymax'] = (df.YMax * df.height).round(0).astype(int)

    df = df.reset_index().rename({'ImageID':'filename'}, axis=1)[[
        'filename', 'width', 'height', 'class',
        'xmin', 'ymin', 'xmax', 'ymax'
    ]]

    # hard coded part...
    df.filename = df.filename.map(lambda fn: fn + '.jpg')
    df = df.set_index('filename')

    # save it
    makedirs(dirname(_DESTINATION), exist_ok=True)
    df.to_csv(_DESTINATION)
