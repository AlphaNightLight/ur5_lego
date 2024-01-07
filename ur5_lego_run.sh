#!/usr/bin/bash

export ROSCONSOLE_FORMAT='[${severity}]: ${message}'
xterm -T 'ur5_generic' -fg 'white' -bg 'black' -fa 'Monospace' -fs 14 -hold -e 'bash' -c 'rosrun ur5_lego ur5_generic.py' &
sleep 5
xterm -T 'nodes' -fg 'white' -bg 'black' -fa 'Monospace' -fs 14 -hold -e 'bash' -c 'roslaunch ur5_lego ur5_lego.launch' &
