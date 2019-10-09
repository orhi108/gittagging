# gittagging

Welcome to git repo tagging tool 
This is a git tool which will create tagging to your master or other current branches. 

It creates three different tags 
1. date and time based tag 
2. a tag name given as an argument 
3. a tag name as branch name different that master 


Syntax:
$ ./gittagging.py [tagname]     ; - optional tag name  

## Prerequisites

### Ubuntu/Debian
```bash
apt install python3 python3-pip git 
pip3 install GitPython
```

### RHEL/CentOS
```bash
yum install python3 python3-pip git
pip3 install GitPython
```

## Download 
```bash 
cd /tmp
git clone https://github.com/orhi108/gittagging.git
```

## Usage
```bash 
cd <your project git local repo>
cp /tmp/gittagging/gittaggin.py .
chmod +x gittaggin.py
./gittagging [<optional tag name>]
```

 


