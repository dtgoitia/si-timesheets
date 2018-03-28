#!/bin/sh

git checkout master
git checkout dev ./timesheet.exe
git add timesheet.exe
git commit -m "Deploy"
git push origin master
git checkout dev