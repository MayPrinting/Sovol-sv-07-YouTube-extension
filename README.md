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

Then, disable the validity check of the package manager, because the operating system will mark the packages metadata expired.:
```bash
sudo nano /etc/apt/apt.conf.d/99no-check-valid-until
```
Paste this into the file:
```bash
Acquire::Check-Valid-Until "false";
```

For saving time, open
```bash
sudo nano /etc/apt/apt.conf.d/99no-contents
```
and paste
```bash
Acquire::IndexTargets {
    deb::Contents-deb {
        DefaultEnabled "false";
    };
};
```
That prevents that `apt` loads all the unnecessary Content-files.

Update the local database without the Content-files:
```bash
sudo apt update
```

Now let's continue with installing a lightweight browser. The best choice is `chromium`
```bash
sudo apt install chromium
```
(optional) Validate installation - you should get something like `/usr/bin/chromium Chromium 89.0.4389.114`
```bash
which chromium
chromium --version
```

If you don't have it already installed, use the following command to install the `gcode_shell_command.py` for your printer. That lets us run our own shell files.










