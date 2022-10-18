#!/bin/bash

outlocation=$(mktemp -d /data/files/XXXXXX)

# sanity check
printf "Conda env: $CONDA_DEFAULT_ENV\n"
printf "Python version: $(python --version)\n"
printf "Biopython version: $(conda list | egrep biopython | awk '{print $2}')\n"
printf "Bash version: ${BASH_VERSION}\n"
printf "Outlocation: $outlocation\n\n"

SCRIPTDIR=$(dirname "$(readlink -f "$0")")

python $SCRIPTDIR"/flash_wrapper.py" -i $1 -of $outlocation -t $4 -d $5 -f $6 -m $7 -x $8 -M $9
mv $outlocation"/log.log" $3
mv $outlocation"/merged.zip" $2
rm -rf $outlocation
