# Beeware Tutorial

Based on Beeware Tutorial by Russell Keith-Magee at PyCon US 2024

- slides: https://bit.ly/beeware-tutorial-pyconus-2024
- YT: https://youtu.be/New2JLvWxiE

## Tutorial Log

```
python3 -m venv beewarenv
source beewarenv/bin/activate
python -m pip install briefcase
briefcase --version
briefcase new
cd helloworld
briefcase dev -vv

## macOS app
briefcase create
briefcase build
briefcase run
briefcase package --adhoc-sign

## update or run and update
briefcase update
briefcase run -u
briefcase update --update-resources

## android
briefcase create android
briefcase build android
briefcase run android --update-resources
briefcase package android --adhoc-sign

## web
briefcase create web
briefcase build web
briefcase run web -u

## test
briefcase dev --test -r
briefcase run Android --test -r
```
