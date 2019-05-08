# easyiotest
Trivial test scripts to debug EasyIO MQTT


## Requirements

Tested on python 2.7.
Requires paho.

```
pip install paho-mqtt
```

## Instructions

Use two terminals.  In terminal 1, start recv.py

```
python recv.py
```

It will sit there forever (until you ctrl+c out of it).

In terminal 2, run send.py

```
python send.py
```

You will see the test message appear in terminal 1.  Great, we are connected.

The recv script is subscribed to all topics starting with `ecc1/iot`.  Anything that the EasyIO is sending should also appear.