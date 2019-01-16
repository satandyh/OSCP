#!/bin/sh

targets="/opt/scans/targets.txt"
options="-v -sV --script vulners"
date=$(date +%Y%m%d-%H%M%S)
dir="/opt/scans"

cd $dir || exit 2
nmap $options -iL "$targets" -oA "scan_$date" > /dev/null

if [ -e scan_prev.xml ] && [ -e "$targets" ]; then
    ndiff scan_prev.xml "scan_$date.xml" > "diff_$date.xml"
#    cat "diff_$date.xml"
fi

#cat "scan_$date.nmap"
ln -sf "scan_$date.xml" scan-prev.xml
exit 0
