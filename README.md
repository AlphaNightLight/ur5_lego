# ur5 lego

Master Repository for Introduction to robotics. It contains 4 submodules: 

- *task planner*: for communications
- *mega blocks detector*: Machine learning with YOLOv8
- *pointcloud*: converts 2D bounding boxes to 3D poses
- *motion planner*: the kinematics functions

## How to run the code

Once cloned this repository, run `bash init_ur5_lego.sh` to link the submodules and create the world.
After that, you just have to type `bash ur5_lego_run.sh`, it will launch *ur5_generic.py* as well as all the other custom nodes.

You can update the world modifying *src/scripts/actual_poses_params.py* and then running `bash create_world.sh` in that folder.
Desired parameters are on the other hand located in in *src/ur5_lego_modules/desired_poses_params.py*.

## Video Simulation

You can find a video of this project at work clicking on the following link:

[https://drive.google.com/file/d/1DNL8iuRZcL6LyBjQTsNmU_ZFPuaRO0vQ/view?usp=sharing](https://drive.google.com/file/d/1DNL8iuRZcL6LyBjQTsNmU_ZFPuaRO0vQ/view?usp=sharing)

## Manteiners
*Alex Pegoraro*

*Alberto Dal Bosco*

*Federica Lorenzini*

*Jacopo Veronese*
