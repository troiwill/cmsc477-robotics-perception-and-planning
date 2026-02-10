# RoboMaster SDK

- Documentation: https://robomaster-dev.readthedocs.io/en/latest/

- GitHub repository: https://github.com/dji-sdk/RoboMaster-SDK

## FAQs

Here are some tips that will help you guys in the future lab sessions:


1. Set up a conda or venv with python version 3.8.10, this is required to install robomaster.

2. Under the project0 instructions, there is a QR code for the wifi connection. DO NOT USE THAT. You need to generate a new one from your laptop once you're connected to the Lab wifi, not eduroam.

3. Before you run any example scripts, add the robomaster ip config at the beginning of the script, the instructions for this are given in the pdf. Otherwise you will connect to other robots in the lab.

Known Issues:

1. M series Macs unable to pip install robomaster. Solution: Setup a VM with Ubuntu and setup the env and repo there.
2. Some Windows Laptops unable to run scripts with pupil-apriltags library. Solution pending

3. Robot doesn't connect to the qr code. Solution : Restart the robot or try with another laptop, this can be a little finicky

Coming Soon.
