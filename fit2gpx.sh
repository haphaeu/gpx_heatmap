#!/bin/bash
#
# Converts FIT files to GPX files.
#
# After downloading Strava activities, remeber to unzip GZ files first:
#
#     gunzip *.gz
#

# Input arguments

# Source directory
src=/home/raf/Documents/Archive/gpx/strava

# Path to gpsbabel 
gpsbabel=~/gpsbabel-1.7.0/gpsbabel

# Existing fit files:
fit_files=$(find $src -type f -name "*.fit")
for f in $fit_files; do
    echo "    $f"
    $gpsbabel -i garmin_fit -f $f -o gpx -F $f.gpx
done
    

