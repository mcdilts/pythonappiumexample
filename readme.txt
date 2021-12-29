requires:
Appium - ideally through npm
Selenium - ideally through npm
pytest - through pip or npm

configure pytest as your python engine
you can use whatever interpreter you want

for local host interactions:
leave the url content commented out and point your port number to whatever port number adb tells you a device is on
(emulated or otherwise)

for genymotion interactions:

create ssh tunnel from localhost5555 to genymotion aws5555
ssh -i key.pem -NL 5555:localhost:5555 shell@35.172.146.129

start appium (current test is setup to instantiate the appium service on its own
change system port in test file to 5555 (to run against genymotion)
change system port in test file to adb server port (to run against connected device)

run pytest in pycharm
collects tests and performs actions