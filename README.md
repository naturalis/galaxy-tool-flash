# galaxy-tool-flash
Wrapper for FLASH, this repo can be used for the new (03-04-2019) galaxy 19.01 Naturalis server. The old galaxy 16.04 server is not supported anymore with this tool. Although FLASH is also available from the toolshed, this specific wrapper fits better in the pipeline because it can handle zip files.

## Getting Started
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
```
```
git clone https://github.com/naturalis/galaxy-tool-flash
```
```
chmod 777 galaxy-tool-flash/flash_wrapper.py
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="/home/galaxy/Tools/galaxy-tool-flash/flash.xml" />
```
Restart Galaxy to see the tool in the menu

## Source
FLASH: Fast length adjustment of short reads to improve genome assemblies. T. Magoc and S. Salzberg. Bioinformatics 27:21 (2011), 2957-63 https://ccb.jhu.edu/software/FLASH/
