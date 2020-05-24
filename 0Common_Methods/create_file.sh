#!/bin/bash
#===============================================================================
#
#          FILE:  create_file.sh
# 
#         USAGE:  ./create_file.sh fileName  
# 
#   DESCRIPTION:  Bash script to create, for now, a personalized .py file
# 
#       OPTIONS:  ---
#  REQUIREMENTS:  Python 3.7
#          BUGS:  ---
#         NOTES:  ---
#        AUTHOR:   (Lev Cesar Guzman Aparicio), 
#       COMPANY:  
#       VERSION:  1.0
#       CREATED:  2020-05-23 12:45:37 PM EDT
#      REVISION:  ---
#===============================================================================

touch $1.py #retrieves the name of the file from the command line and creates a .py file


#since this script is designed for my bioinformatics problems, it will only import common_methods.py 

#we will use a here document to write on the file

cat <<EOF >$1.py
import common_methods.py as cm

#*******************************************************
#* Author: Lev Cesar Guzman Aparicio		       *
#* Email: lguzm038@uottawa.ca or lguzm77@gmail.com     *
#* Problem #-- : ---------------------------------     *
#*      				               *
#*******************************************************

#---------------------METHODS----------------------


#---------------------MAIN-------------------------

def main():
    pass

main()
 
EOF

