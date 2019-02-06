# INSTALLING THE FULL STACK 
### Krogoth Setup For Docker

#### Contents
    1. Getting Started 
    2. Installation Components

If you want to deploy a full krogoth stack immediately with all included features,
just run the command below and wait for the images to finish downloading. 

## Getting Started
Run the installer with python3:
#### macOS
```bash
my-host-os$ python3 install_krogoth.py
```
#### Ubuntu
* root permissions may be required on most Linux distributions.*
```bash
my-host-os$ sudo python3 install_krogoth.py
```

## Installatioh Components

The installation of Krogoth goes through the phases listed below:

    1. Create docker container with Django/NGINX
    2. Create a Redis docker container
    3. 