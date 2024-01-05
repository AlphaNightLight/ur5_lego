#!/usr/bin/env python

class DesiredPose2D:
  def __init__(self, label, x, y, theta):
    self.label = label
    self.x = x
    self.y = y
    self.theta = theta

desired_poses = []
PI = 3.1415926535
z_offset = -0.5

# Set here your desired poses
desired_poses.append(DesiredPose2D( label = "aaa", x = 0.2, y = 0.0, theta = PI/3 ))
desired_poses.append(DesiredPose2D( label = "bbb", x = 0.4, y = 0.5, theta = 0 ))
desired_poses.append(DesiredPose2D( label = "ccc", x = 0.4, y = -0.3, theta = -PI/4 ))
desired_poses.append(DesiredPose2D( label = "ddd", x = 0.1, y = 0.22, theta = 3*PI/2 ))
