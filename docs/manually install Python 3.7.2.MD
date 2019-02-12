## Manually Install Python 3.7.2
#### Ubuntu 18.04

Download Python 3.7.2 source code:
```sh
apt-get install wget
wget 'https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tar.xz'
```

Create path and extract the source there:
```sh
mkdir pysrc_37
tar -xf '/usr/src/tmp/Python-3.7.2.tar.xz'  -C /usr/src/tmp/pysrc_37

Navigate to the extracted contents and run these commands to compile and install:
```sh
cd /usr/src/tmp/pysrc_37
./configure
make
make install
```


This may take awhile to finish, be patient.