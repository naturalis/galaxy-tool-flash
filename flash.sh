#!/bin/bash
#location for production server
#outlocation=$(mktemp -d /media/GalaxyData/database/files/XXXXXX)
#location for the testserver
outlocation=$(mktemp -d /media/GalaxyData/files/XXXXXX)
flash_wrapper.py -i $1 -of $outlocation -t $4 -f $5 -m $6 -x $7 -M $8
mv $outlocation"/log.log" $3
mv $outlocation"/merged.zip" $2
rm -rf $outlocation 
