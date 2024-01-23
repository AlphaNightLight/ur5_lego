world_path="../../../locosim/ros_impedance_controller/worlds"
world_name="ur5_lego.world"

if ! [ -e $world_path/$world_name ]
then
	bash create_world.sh
fi

nano $world_path/$world_name
