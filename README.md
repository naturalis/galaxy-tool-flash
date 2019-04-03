# galaxy-tool-flash
wrapper for FLASH, this repo can be used for the new (03-04-2019) galaxy 19.01 Naturalis server. The old galaxy 16.04 server is not supported anymore with this tool.
## Getting Started
### Installing
Installing the tool for use in Galaxy
```
cd /home/galaxy/Tools
```
```
sudo git clone https://github.com/naturalis/galaxy-tool-flash
```
```
sudo chmod 777 galaxy-tool-flash/flash_wrapper.py
```
```
sudo ln -s /home/galaxy/Tools/galaxy-tool-flash/flash_wrapper.py /usr/local/bin/flash_wrapper.py
```
```
sudo cp galaxy-tool-flash/flash.sh /home/galaxy/galaxy/tools/identify/flash.sh
sudo cp galaxy-tool-flash/flash.xml /home/galaxy/galaxy/tools/identify/flash.xml
```
Add the following line to /home/galaxy/galaxy/config/tool_conf.xml
```
<tool file="identify/flash.xml" />
```
Restart Galaxy to see the tool in the menu

## Source
FLASH: Fast length adjustment of short reads to improve genome assemblies. T. Magoc and S. Salzberg. Bioinformatics 27:21 (2011), 2957-63 https://ccb.jhu.edu/software/FLASH/
