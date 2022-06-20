This project serves as an example for writing Automation(Selenium, Rest Api and Web-socket) using Gauge
Installation Help Documentation - https://docs.gauge.org/getting_started/installing-gauge.html?os=windows&language=python&ide=vscode

**Pre-requisites (Install the following softwares)** -
  pip install getgauge==0.3.17 –user
  pip3 install --upgrade protobuf==3.20.0
  pip install selenium
  pip3 install websocket-client
  python -m pip install requests
  pip install webdriver-manager
  
**To generate reports** - 
  gauge install html-report
  gauge install json-report
  gauge install xml-report
  gauge install spectacle
  gauge install flash

**To generate spectacle report** - gauge docs spectacle

**Run specific features with environment files** –  gauge run --env="default" specs
**Run specific feature file** – gauge run .\specs\login_csv.spec


**Suppose that you have a specification file, called let say Login.spec, and you want to list all the scenarios or tags. Below command can be used :**

gauge list --tags specs/login.spec // tag names
gauge list --scenarios specs/login.spec // scenario names
