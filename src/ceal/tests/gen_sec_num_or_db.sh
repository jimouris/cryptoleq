#!/bin/bash

if [ $# -ne 4 ]; then
    echo Usage: "$0" n Nbits beta num_to_encypt
    echo or
    echo Usage: "$0" f Nbits beta file_to_encrypt
    exit -1
fi

mode="$1"
Nbits="$2"
beta="$3"
numOrFile="$4"
PQ=0

if [[ $Nbits -eq "16" ]]; then
    PQ=239.251
elif [[ $Nbits -eq "32" ]]; then
    PQ=63199.64567
elif [[ $Nbits -eq "64" ]]; then
    PQ=4281167959.4271299633
elif [[ $Nbits -eq "128" ]]; then
    PQ=18299379327617480707.18345258783657292909
elif [[ $Nbits -eq "256" ]]; then
    PQ=338871469111127928412308213206819656391.338531414912581056934822037249894061881
elif [[ $Nbits -eq "512" ]]; then
    PQ=115689526107095890311249333520175779978137070980169508677335528535095435701957.115509443392406915656501893779637949187966713758992043305916442498716409678501
elif [[ $Nbits -eq "1024" ]]; then
    PQ=13392849694255970315601419090152597688339809774933571293865724091737666496951381207429127235940384883608845778583380210687006370486238723021460371010217257.13403952390292880134486926689236901739298695038033079040680862117777593853851234125818128702776151240584166261477766002390185782669746209391687589482784501
else
    echo "Wrong Nbits given. Try 16, 32, ..., 1024."
    exit -1
fi

if [ $mode == f ]; then
    echo "../_bin_unx/ceal -p \"k=5 r=17 beta=$beta PQ=$PQ\" -c xenc $numOrFile"
    res="$(../_bin_unx/ceal -p "k=5 r=17 beta=$beta PQ=$PQ" -c xenc $numOrFile)"
    echo $res
    echo $res > "./input"$numOrFile"_N"$Nbits"_b"$beta".db.sec"
elif [ $mode == n ]; then
    echo "../_bin_unx/ceal -p \"k=5 r=17 beta=$beta PQ=$PQ\" -c xenc @$numOrFile"
    res="$(../_bin_unx/ceal -p "k=5 r=17 beta=$beta PQ=$PQ" -c xenc @$numOrFile)"
    echo $res
    echo $res > "./input"$numOrFile"_N"$Nbits"_b"$beta".sec"
else
    echo "Wrong mode given. Try f for file or n for number"
    exit -1
fi
