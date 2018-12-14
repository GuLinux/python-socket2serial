# Python Socket2Serial

Creates a virtual serial port over a TCP or UDP connection.

# Installation
First make sure you have python3 installed on your system.
Download this repository and extract it in a directory of your choice.

Then just run:
```
sudo make install
```

# Usage

```python-socket2serial.py [-u|--udp] <host> <port>```
The program will print on screen the virtual serial port path.

## Options
`-u` or `--udp`: use UDP instead of TCP

### Qidi X-Pro with Octoprint

Although this could be a general utility, I created it specifically to connect my Qidi X-Pro to Octoprint.
In order to do this, just run the following command when the Octoprint server starts:
```
python3 /usr/bin/python-socket2serial.py -u <printer_ip_address> 3000
```

In Octoprint settings you then need to add the following ports to the `Additional serial ports` field:
```
/dev/pts/2
/dev/pts/3
/dev/pts/4
/dev/pts/5
```
Usually it's `/dev/pts/2`, but it may vary depending on which port is already in use.
