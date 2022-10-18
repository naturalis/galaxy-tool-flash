# galaxy-tool-flash
Wrapper for FLASH v.1.2.11. This repo uses Pyhton3 and has been tested with Galaxy v.22.01  
(using a Terraform/Ansible install on the new Naturalis OpenStack). Although FLASH is also  
available from the Toolshed, this wrapper fits better in our pipeline because it can handle zip files.

## Installation
### Manual
Clone this repo in your Galaxy ***Tools*** directory:  
`git clone https://github.com/naturalis/galaxy-tool-flash`  

Make the python script executable:  
`chmod 755 galaxy-tool-flash/flash_wrapper.py`  

Append the file ***tool_conf.xml***:    
`<tool file="/path/to/Tools/galaxy-tool-flash/flash.xml" />`  

### Ansible
Depending on your setup the [ansible.builtin.git](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html) module could be used.  
[Install the tool](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/git_module.html#examples) by including the following in your dedicated ***.yml** file:  

`  - repo: https://github.com/naturalis/galaxy-tool-flash`  
&ensp;&ensp;`file: flash.xml`  
&ensp;&ensp;`version: master`  


## Source
FLASH: Fast length adjustment of short reads to improve genome assemblies. T. Magoc and S. Salzberg. Bioinformatics 27:21 (2011), 2957-63 https://ccb.jhu.edu/software/FLASH/
