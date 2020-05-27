# TorDetector
This script accept a text file and collect any IP address (based on its format x.x.x.x) and check if it is one of Tor exit nodes, such as validating IP addresses from FW, IIS, access logs, etc.

## Usage
Provide the log file to the script as argument, the script will fetch the Tor exit node IP addresses from "https://www.dan.me.uk/torlist/" and store it in "tor_exit_nodes.list" file, you can provide a folder path and it will check all log files inside it

```                  
python TorDetector.py <log-file>
```
Note: the webside "https://www.dan.me.uk/torlist/" only allow to fetch the database every 30mins, if you try to run the script again it will print the message
```
[-] Message: Umm... You can only fetch the data every 30 minutes - sorry.  It's pointless any faster as I only update every 30 minutes anyway.
If you keep trying to download this list too often, you may get blocked from accessing it completely.
(this is due to some people trying to download this list every minute!)
```
and it will get the list from the file "tor_exit_nodes.list" if exists.


## Requirements
```
pip install validators
```
