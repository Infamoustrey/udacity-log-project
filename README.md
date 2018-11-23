# Log Analysis Program
> A small reporter for the news db

## About
This program attempts to connect to the news database and query
the following statistics:

- Most Popular Articles
- Most Popular Authors
- Days where errors exceeded 1% of requests

It prints the results to the console via the standard output. 

## Usage 
To run simply run the following: 

```bash 
python3 log_report.py
```

To save to a text file simply run it this way: 

```bash 
python3 log_report.py > report_output.txt
```

