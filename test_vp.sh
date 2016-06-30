#!/bin/bash
version=$1
#series=45
series=28
vp_folder="/production/maps/map_$series/official/$version/variant_pkg"

unzip -l ${vp_folder}/$2.zip | grep ".cdt" | awk 'BEGIN { FS="/" } { print $NF }' | cut -d"." -f1 > $2_qb.txt

