#!/bin/bash

# robi opisy

for d in `find . -type d | grep -v in | grep -v wyniki | sed 1d | sort`
do
d=`echo "$d" | tr -d './'`
echo "***************" $d
head -1 $d/$d.pdb
cat $d/$d.pdb | grep "TITLE"
cat $d/$d.pdb | grep "EXPDTA "
echo

cd $d

for f in `ls *.pdb | grep -v $d`
do
head -1 $f
cat $f | grep "TITLE"
cat $f | grep "EXPDTA "
done

echo
cd ..

done