#!/bin/sh

echo Removing build folder...
rm -rf ./build
echo Removing dist folder...
rm -rf ./dist
echo Removing __pycache__ folder...
rm -rf ./__pycache__

pyinstaller ./timesheet.spec --onefile --distpath ./

cp ./src/.config ./.config