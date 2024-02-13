#!/usr/bin/bash

models_dest_path="../../../locosim/ros_impedance_controller/worlds/models"
models_source_path="../mega_blocks_detector_project/Models"

model_names=("X1-Y1-Z2" "X1-Y2-Z1" "X1-Y2-Z2" "X1-Y2-Z2-CHAMFER"
"X1-Y2-Z2-TWINFILLET" "X1-Y3-Z2" "X1-Y3-Z2-FILLET" "X1-Y4-Z1"
"X1-Y4-Z2" "X2-Y2-Z2" "X2-Y2-Z2-FILLET")

for model in ${model_names[@]}
do
	if [ -d $models_dest_path/$model ]
	then
		echo info: $model already present in destination path
	else
		if [ -d $models_source_path/$model ]
		then
			cp -r $models_source_path/$model $models_dest_path/$model &&
			echo info: $model copied in destination path ||
			echo error: something went wrong during the copy of $model
		else
			echo error: $model not found in source path, it will be ignored
		fi
	fi
done



world_name="ur5_lego.world"
default_world="tavolo.world"

if [ -e $models_dest_path/../$world_name ]
then
	echo info: $world_name already present in destination path
else
	if [ -e $models_dest_path/../$default_world ]
	then
		cp $models_dest_path/../$default_world $models_dest_path/../$world_name &&
		echo info: $world_name generated successfuly ||
		echo error: something went wrong during the copy of $default_world
	else
		echo error: $default_world not found in source path, unable to generate $world_name
	fi
fi

#python3 load_blocks.py
