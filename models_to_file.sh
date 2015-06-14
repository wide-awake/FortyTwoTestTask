#!/bin/bash
FILENAME=$(date +"%Y-%m-%d")

chmod go+w .
echo "Generating file with list of all the models in it"
python manage.py models 2>> $FILENAME.dat
chmod 700 .

txtgrn=$(tput setaf 2)
echo "${txtgrn}=============================== Done!${txtgrn}"