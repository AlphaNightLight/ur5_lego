#!/usr/bin/bash

git submodule update --init
ln -s src/mega_blocks_detector_project/code/custom_model_ros.py src/ur5_lego_modules/bosco_code.py
ln -s src/pointcloud/pose_and_orientation.py src/ur5_lego_modules/posky_code.py
bash src/scripts/create_world.sh
python3 src/scripts/load_blocks.py
