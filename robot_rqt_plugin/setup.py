from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['robot_rqt_plugin'],
    package_dir={'': 'src'},
)

setup(**d)
