#!/bin/sh

if [ $# -ne 3 ]; then
    echo Usage: "$0" PQ beta num_to_encypt
    exit
fi

PQ="$1"
beta="$2"
num="$3"

echo "../../_bin_unx/ceal -p \"k=5 r=17 beta=$beta PQ=$PQ\" -c xenc @$num"
../../_bin_unx/ceal -p "k=5 r=17 beta=$beta PQ=$PQ" -c xenc @$num
