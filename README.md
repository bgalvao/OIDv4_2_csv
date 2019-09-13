# OIDv4_2_csv
Tiny utility to convert annotation data from [OIDv4_Toolkit](https://github.com/EscVM/OIDv4_ToolKit)
to the csv format necessary to convert to TFRecords. Made with 
[Tony607/object_detection_demo](https://github.com/Tony607/object_detection_demo)
in mind.


```
(base) bgalvao@rocket:~/repos/tools/OID2csv_voc$ python main.py --help
usage: main.py [-h] [--imgs_source IMGS_SOURCE]
               [--output_csv_filename OUTPUT_CSV_FILENAME]
               [--annotations_file_path ANNOTATIONS_FILE_PATH]
               [--labels_file_path LABELS_FILE_PATH]

Make VOC-csv annotation from images downloaded using OIDv4_Toolkit. This tool
was created to create a suitable format for the
https://github.com/Tony607/object_detection_demo boilerplate from the OIDv4
dataset downloaded using https://github.com/EscVM/OIDv4_ToolKit

optional arguments:
  -h, --help            show this help message and exit
  --imgs_source IMGS_SOURCE, -i IMGS_SOURCE
                        Source folder where images are. Will walk recursively.
  --output_csv_filename OUTPUT_CSV_FILENAME, -o OUTPUT_CSV_FILENAME
                        Where to write the output csv file to.
  --annotations_file_path ANNOTATIONS_FILE_PATH, -a ANNOTATIONS_FILE_PATH
                        Path to csv annotations file provided by OID. Do
                        recommend to make your own smaller annotations file of
                        classes of interest.
  --labels_file_path LABELS_FILE_PATH, -l LABELS_FILE_PATH
                        Path to csv annotations file provided by OID. Do
                        recommend to make your own smaller annotations file of
                        classes of interest.

```
