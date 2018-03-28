#!/bin/sh

cp ./dist/timesheet.exe ./timesheet.exe
git checkout master
git checkout dev ./timesheet.exe
git checkout add ./timesheet.exe
git commit -m "Deploy"
git push origin master
git checkout dev