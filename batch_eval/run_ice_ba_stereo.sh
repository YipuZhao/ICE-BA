#!/bin/bash

# Set your own EuRoC_PATH path to run ice-ba. Use './bin/ice_ba --help' to get the explanation for all of the flags. Flags [imgs_folder] and [iba_param_path] are necessary.
# Add flag '--save_feature' to save feature message and calibration file for back-end only mode

EuRoC_PATH=/mnt/DATA/Datasets/EuRoC_dataset
Sequence=V2_03_difficult

mkdir $EuRoC_PATH/result

cmd="../bin/ice_ba --imgs_folder $EuRoC_PATH/$Sequence --start_idx 0 --end_idx -1 --iba_param_path ../config/config_of_stereo_v2.txt --stereo" # --gba_camera_save_path $EuRoC_PATH/result/$Sequence.txt --save_feature
echo $cmd
eval $cmd
