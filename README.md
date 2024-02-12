# ur5 lego

Master Repository for Introduction to robotics. It contains 4 submodules: 

- *task planner*: for communications
- *mega blocks detector*: Machine learning with YOLOv8
- *pointcloud*: converts 2D bounding boxes to 3d poses
- *motion planner*: the kinematics functions

## How to run the code
Once cloned this repository, run `bash init_ur5_lego.sh` to link the submodules and create the world.
After that, you just have to type `bash ur5_lego_run.sh`, it will launch *ur5_generic.py* as well as all the other custom nodes.

## Manteiners
*Alex Pegoraro*

*Alberto Dal Bosco*

*Jacopo Veronese*

*Federica Lorenzini*
