#!/usr/bin/bash

git submodule update --init
ln -s src/mega_blocks_detector_project/code/custom_model_ros.py src/ur5_lego_modules/bosco_code.py
ln -s src/pointcloud/pose_and_orientation.py src/ur5_lego_modules/posky_code.py

cd src/scripts/
bash create_world.sh
cd ../../
