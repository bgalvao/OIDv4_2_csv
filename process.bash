# this loop thing passes raw bytes to python and it breaks. I have work to do
# so I don't care about fixing it

#subsets=("train" "test" "validation")
# for i in "${subsets[@]}"
# do
#     :
#     echo "processing $i subset"
#     python main.py \
#     --imgs_source ../OIDv4_Toolkit/OID/Dataset/\"${i}\" \
#     --annotations_file_path "../OIDv4_Toolkit/OID/csv_folder/\"${i}\"-annotations-bbox.csv" \
#     --labels_file_path ../OIDv4_Toolkit/OID/csv_folder/class-descriptions-boxable.csv \
#     --output_csv ../OIDv4_Toolkit/OID/\"${i}\".csv
# done

# train
echo "processing train subset"
python main.py \
--imgs_source ../OIDv4_ToolKit/OID/Dataset/train/ \
--output_csv_filename ./train.csv \
--annotations_file_path ../OIDv4_ToolKit/OID/csv_folder/train-annotations-bbox.csv \
--labels_file_path ../OIDv4_ToolKit/OID/csv_folder/class-descriptions-boxable.csv \
--target_classes Dolphin Whale

# test
echo "processing test subset"
python main.py \
--imgs_source ../OIDv4_ToolKit/OID/Dataset/test/ \
--output_csv_filename ./test.csv \
--annotations_file_path ../OIDv4_ToolKit/OID/csv_folder/test-annotations-bbox.csv \
--labels_file_path ../OIDv4_ToolKit/OID/csv_folder/class-descriptions-boxable.csv \
--target_classes Dolphin Whale

# validation
echo "processing validation subset"
python main.py \
--imgs_source ../OIDv4_ToolKit/OID/Dataset/validation/ \
--output_csv_filename ./validation.csv \
--annotations_file_path ../OIDv4_ToolKit/OID/csv_folder/validation-annotations-bbox.csv \
--labels_file_path ../OIDv4_ToolKit/OID/csv_folder/class-descriptions-boxable.csv \
--target_classes Dolphin Whale
