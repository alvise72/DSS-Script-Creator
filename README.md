# THIS FILE IS WORK IN PROGRESS

# DSS-Script-Creator
This python tool prepare a script to be fed to DeepSkyStacker to ease the use of the command line

Project is still beta. It aims to automatically prepare a script text file to be passed to DeepSkyStackerCL.exe command line to automatize the stacking process of deep sky images.
I uses a template file containing the settings I've saved for a certain astrophoto session. Then it merges this template with a list of light/dark/bias/flat files contained in the directories specified in the options.

```
usage: prepare-dss-script.py [-h] [-b BIAS] [-d DARK] [-l LIGHT] [-o OUTPUT]
                             [-f FLAT] [-R] [-T Template file for settings]
                             DeepSpace Object Name

Tool to produce DSS script file

positional arguments:
  DeepSpace Object Name
                        Specify the mandatory name of the deep sky object name

optional arguments:
  -h, --help            show this help message and exit
  -b BIAS, --bias BIAS  Specify the folder containing the bias/offset frames
  -d DARK, --dark DARK  Specify the folder containing the dark frames
  -l LIGHT, --light LIGHT
                        Specify the folder containing the light frames
  -o OUTPUT, --output OUTPUT
                        Specify the filename of the siril script to create
  -f FLAT, --flat FLAT  Specify the folder containing the flat/vignetting
                        files
  -R, --raw             Specify if source files are RAW
  -T Template file for settings, --templatefile Template file for settings
                        Specify the file containing the basic settings to be
                        modified and merged with file list
```
