# TorDetector
This script accept a text file and collect any IP address (based on its format x.x.x.x) and check if it is one of Tor exit nodes, such as validating IP addresses from FW, IIS, access logs, etc.

## Usage
Provide the log file to the script as argument, the script will fetch the Tor exit node IP addresses from "https://check.torproject.org/torbulkexitlist" and store it in "tor_exit_nodes.list" file, you can provide a folder path and it will check all log files inside it

```                  
python TorDetector.py (<logs-folder>|<log-file>)
```

and it will get the list from the file "tor_exit_nodes.list" if exists.

## Output

![Results](https://github.com/salehmuhaysin/TorDetector/blob/master/Selection_010.png?raw=true)


## Requirements
```
pip install validators
```
