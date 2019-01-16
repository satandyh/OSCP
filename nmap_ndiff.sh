#!/bin/sh

targets="targets.txt"
options="-v -T4 -F -sV"
date=$(date +%F)
dir="/opt/scans"

cd $dir || exit 2
nmap $options -iL $dir/$targets -oA scan-$date > /dev/null

if [ -e scan-prev.xml ] && [ -e "$dir/$targets" ]; then

    ndiff scan-prev.xml scan-$date.xml > diff-$date.xml
#    echo "*** NDIFF RESULTS ***"
    cat diff-$date.xml
#    echo
fi

#echo "*** NMAP RESULTS ***"
#cat scan-$date.nmap
ln -sf scan-$date.xml scan-prev.xml

exit 0
