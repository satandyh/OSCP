#!/bin/sh

TARGETS="<targets>"
OPTIONS="-v -T4 -F -sV"
DATE=$(date +%F)
DIR="/opt/scans"

cd $DIR || exit 2


nmap $OPTIONS $TARGETS -oA scan-$date > /dev/null

if [ -e scan-prev.xml ]; then
    ndiff scan-prev.xml scan-$date.xml > diff-$date
#    echo "*** NDIFF RESULTS ***"
#    cat diff-$date
#    echo
fi

echo "*** NMAP RESULTS ***"
cat scan-$date.nmap
ln -sf scan-$date.xml scan-prev.xml
