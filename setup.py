from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
#  scripts=['src/ur5_lego_modules/desired_poses_params.py', 'src/mega_blocks_detector_project/code/custom_model.py'],
  packages=['ur5_lego_modules'],
  package_dir={'': 'src'}
)

setup(**d)

