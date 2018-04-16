# galaxy-tool-flash
wrapper for FLASH
## Getting Started
### Prerequisites
Installing FLASH on the Naturalis galaxy server. Most of the tools are installed in the Tools folder, below are instructions to install FLASH.
```
mkdir /home/galaxy/Tools/flash
```
```
cd /home/galaxy/Tools/flash
```
```
sudo wget http://ccb.jhu.edu/software/FLASH/FLASH-1.2.11-Linux-x86_64.tar.gz
```
```
sudo tar xzf FLASH-1.2.11-Linux-x86_64.tar.gz
```
```
sudo ln -s /home/galaxy/Tools/flash/FLASH-1.2.11-Linux-x86_64/flash /usr/local/bin/flash
```
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
