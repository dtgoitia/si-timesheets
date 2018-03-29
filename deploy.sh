#!/bin/sh

git checkout master
git checkout dev ./timesheet.exe
git checkout dev ./timesheet.spec
git checkout dev ./README.md
git add .
git commit -m "Deploy"
git push origin master
git checkout dev