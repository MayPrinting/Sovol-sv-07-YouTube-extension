# Sovol sv 07 YouTube extension

A KlipperScreen extension that seamlessly integrates YouTube into the Sovol SV07 touchscreen!


## Features

- 🎬 Watch YouTube directly on your printer's touchscreen
- ⌨️ Built-in on-screen keyboard
- 🖥️ Optimized for the Sovol SV07 display
- 🔄 Easily launch and close YouTube from KlipperScreen
- 🛠️ Lightweight and easy to install

## Installation

Build a connection to your Klipper Screen via ssh. The default password for the user `mks` is `makerbase`.
```bash
ssh mks@mkspi
```
If `mkspi` doesn`t work, use the IP address of your printer instead.


Since the operating system is very old, you will need to change the Debian-sources first. Open the `sources.list` in your terminal and replace the whole contents with the following url:
```bash
sudo nano /etc/apt/sources.list
```
```bash
deb http://archive.debian.org/debian buster main contrib non-free
```

Then, disable the validity check of the package manager:
```bash
sudo nano /etc/apt/apt.conf.d/99no-check-valid-until
```
Paste this into the file:
```bash
Acquire::Check-Valid-Until "false";
```


