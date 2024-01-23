#!/usr/bin/env python

from actual_poses_params import actual_poses
from actual_poses_params import x_offset
from actual_poses_params import y_offset
from actual_poses_params import z_offset

text_begin = """\
<?xml version="1.0" ?>
<sdf version="1.4">
  <world name="ur5_lego">
    <physics type='ode'>
      <gravity>0 0 -9.81</gravity>
      <!-- max step size has to be a multiple of the desired task rate-->
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
    </physics>
    <!-- A global light source -->
    <include>
      <uri>model://sun</uri>
    </include>
    <!-- A ground plane -->
    <include>
      <uri>model://ground_plane</uri>
    </include>
    <include>
      <name>tavolo</name>
      <uri>model://tavolo</uri>
      <pose>0.0 0.0 0.0 0 0 0</pose>
    </include>
"""

text_end = """
    <gui>
    <camera name="gzclient_camera">
      <pose>1. 3.2 2.2 0. 0.4 -1.75</pose>
    </camera>
    </gui>

  </world>
</sdf>
"""

if __name__ == "__main__":
  file = open("../../../locosim/ros_impedance_controller/worlds/ur5_lego.world", "wt")
  file.write(text_begin)

  for block in actual_poses:
    text_block = "\n    <include>\n      <name> "
    text_block += block.label
    text_block += " </name>\n      <uri> model://"
    text_block += block.label
    text_block += " </uri>\n      <pose> "
    text_block += str(block.x + x_offset)
    text_block += " "
    text_block += str(block.y + y_offset)
    text_block += " "
    text_block += str(z_offset)
    text_block += " "
    text_block += "0"
    text_block += " "
    text_block += "0"
    text_block += " "
    text_block += str(block.theta)
    text_block += " </pose>\n    </include>\n"
    file.write(text_block)

  file.write(text_end)
  file.close()
