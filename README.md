# Log Analysis Program
> A small reporter for the news db

## About
This program attempts to connect to the news database and query
the following statistics:

- Most Popular Articles
- Most Popular Authors
- Days where errors exceeded 1% of requests

It prints the results to the console via the standard output. 

## Prerequisites

You will need vagrant, an editor, and a terminal for this project.

## Setup

This program analyses the news db for the following vagrant vm.
To setup clone the repository:

```bash 
git clone https://github.com/udacity/fullstack-nanodegree-vm.git
```

Then cd into the vagrant directory and launch the vm

```bash
cd fullstack-nanodegree-vm.git/vagrant
vagrant up 
```

Then download the `newsdata.sql` file from [this](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) link.

Copy the file into the `vagrant` directory on your local machine and run the following command to setup the db:

```bash 
psql -d news -f newsdata.sql
```

Now you'll need to clone this program repo into the `vagrant` dir on your local machine, to do so run the following command:

```bash
git clone https://github.com/Infamoustrey/udacity-log-project.git
```

Now you'll want to ssh into the vagrant machine and get into the `vagrant` dir to be able to run the report. From your localmachine run the following:

```bash
vagrant ssh
cd /vagrant/udacity-log-project
python3 log_report.py
```

## Usage 
To run simply run the following: 

```bash 
python3 log_report.py
```

To save to a text file simply run it this way: 

```bash 
python3 log_report.py > report_output.txt
```

