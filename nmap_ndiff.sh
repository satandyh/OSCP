#!/bin/sh

targets="/opt/scans/targets.txt"
options="-v -sV --script vulners,vulscan/vulscan.nse --script-args vulscandb=vulscan/exploitdb.csv"
date=$(date +%Y%m%d-%H%M%S)
dir="/opt/scans"

slack(){
curl -F "file=@diff_$date" \
    -F 'initial_comment="Internal Port Change Detected"' \
    -F "channels=#alerts" \
    -F "token=xxxx-xxxx-xxxx" https://slack.com/api/files.upload
}

cd $dir || exit 2
nmap $options -iL "$targets" -oA "scan_$date" > /dev/null

if [ -e scan_prev.xml ]; then
    ndiff scan_prev.xml "scan_$date.xml" > "diff_$date"
    [ "$?" -eq "1" ] && sed -i -e 1,3d diff_$date && slack
fi

ln -sf "scan_$date.xml" scan_prev.xml
exit 0
