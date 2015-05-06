#!/bin/bash

cat RNA.txt | sed -e "s/SEQUENCE//g" | sed -e 's/>//g' -e 's/:/\t/g' |  sed -e ':a;N;$!ba;s/\n[A-Z]//g' | sed -e 's/|/\t/g' > RNA-oneline.txt
cat RNA+lig.txt | sed -e "s/SEQUENCE//g" | sed -e 's/>//g' -e 's/:/\t/g' |  sed -e ':a;N;$!ba;s/\n[A-Z]//g' | sed -e 's/|/\t/g' > RNA+lig-oneline.txt
cat RNA-bezlig.txt | sed -e "s/SEQUENCE//g" | sed -e 's/>//g' -e 's/:/\t/g' |  sed -e ':a;N;$!ba;s/\n[A-Z]//g' | sed -e 's/|/\t/g' > RNA-bezlig-oneline.txt
