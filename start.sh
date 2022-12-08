#!/bin/bash

###################################################################################################
#                                                                                                 #
# SCRIPT FILE: start.sh                                                                           #
# CREATION DATE: 17/11/2022                                                                       #
# HOUR: 11:48                                                                                     #
# DISTRIBUTION USED: UBUNTU                                                                       #
# OPERATIONAL SYSTEM: DEBIAN                                                                      #
#                                                                             DEVELOPED BY: BATES #
###################################################################################################
#                                                                                                 #
# SUMMARY: DATA ON THE CIRCULATION OF NATIONAL CURRENCIES                                         #
#                                                                                                 #
###################################################################################################

# variables


if  [ $? -eq 0 ]; then > /dev/null
    clear
    python3 random_cup/main.py > random_cup/relatorio_copa.txt
fi
