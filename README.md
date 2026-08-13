# Sovol sv 07 YouTube extension
<img src="/images/>

A KlipperScreen extension that seamlessly integrates YouTube into the Sovol SV07 touchscreen!


## Features

- 🎬 Watch YouTube directly on your printer's touchscreen
- ⌨️ Built-in on-screen keyboard
- 🖥️ Optimized for the Sovol SV07 display
- 🔄 Easily launch and close YouTube from KlipperScreen
- 🛠️ Lightweight and easy to install

## Installation

<i>All the installation steps need the repository to be cloned into the user folder of your computer, using the command `git clone https://github.com/MayPrinting/Sovol-sv-07-YouTube-extension.git`</i>


Build a connection to your Klipper Screen via ssh. The default password for the user `mks` is `makerbase`:
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

Then, disable the validity check of the package manager, because the operating system will mark the packages metadata expired:
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

Now let's continue with installing a lightweight browser. The best choice is `chromium`:
```bash
sudo apt install chromium
```
(optional) Validate installation - you should get something like `/usr/bin/chromium Chromium 89.0.4389.114`
```bash
which chromium
chromium --version
```
Chromium itself does not include on-screen keyboard logic. We will have to install `onboard`:
```bash
sudo apt install onboard
```
Set the keyboard up:
```bash
gsettings list-keys org.onboard.window.portrait
gsettings set org.onboard.window docking-enabled false
gsettings set org.onboard.window force-to-top true
gsettings set org.onboard.window.portrait width 480
gsettings set org.onboard.window.portrait height 300
gsettings set org.onboard.window.portrait x 0
gsettings set org.onboard.window.portrait y 450
```

Install a window manager so that the keyboard can be used as interface
```bash
sudo apt install matchbox-window-manager
```

If you don't have it already installed, use the following command to install the `gcode_shell_command.py` for your printer. That lets us run our own shell files:
```bash
cd ~/klipper/klippy/extras/
wget https://raw.githubusercontent.com/MayPrinting/Sovol-sv-07-YouTube-extension/refs/heads/main/gcode_shell_command.py
```
Restart the system
```bash
sudo systemctl restart klipper
```

Check if your mkspi already has a folder for your own scripts, otherwise create one:
```bash
ls
```
```bash
mkdir scripts
```

Open another terminal window and use `secure copy` to move the Shell and Python files into the scripts folder:
```bash
scp ~/Sovol-sv-07-YouTube-extension/Shell/start_youtube.sh mks@mkspi:/home/mks/scripts/
scp ~/Sovol-sv-07-YouTube-extension/Shell/stop_youtube.sh mks@mkspi:/home/mks/scripts/
scp ~/Sovol-sv-07-YouTube-extension/Python/overlay_bar.py mks@mkspi:/home/mks/scripts/
```
Then, switch terminal windows again and make both the Shell files executable:
```bash
cd ~/scripts
sudo chmod +x start_youtube.sh
sudo chmod +x stop_youtube.sh
```

Now we need a YouTube icon for our YouTube button. We will also use `secure copy`, so change your terminal window again to move it to your MKS Pi. We will use one icon for all theming, you can change it later:
```bash
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/material-dark/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/material-darker/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/material-light/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/sovol-light/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/sovol-dark/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/sovol-light-test/
scp ~/Sovol-sv-07-YouTube-extension/icons/youtube.svg mks@mkspi:/home/mks/KlipperScreen/styles/z-bold/
```

Switch terminals again. We will continue with creating a button in the `actions` menu, so that you can access YouTube the easiest way.
We will need to edit the KlipperScreen.conf.
```bash
sudo nano ~/KlipperScreen/KlipperScreen.conf
```
Right before the `Do not edit` section, paste this:
```bash
[menu __main actions youtube]
name: YouTube
icon: youtube
method: printer.gcode.script
params: {"script":"START_YOUTUBE"}
```
The last step ist adding a gcode macro in the printer.cfg:
```bash
sudo nano ~/printer_data/config/printer.cfg
```
Just at the end of the section `gcode macros`, add the YouTube macro:
```bash
[gcode_shell_command start_youtube]
command: /home/mks/scripts/start_youtube.sh
timeout: 30.
verbose: True

[gcode_macro START_YOUTUBE]
gcode:
    RUN_SHELL_COMMAND CMD=start_youtube
```

## 🎉 Restart your KlipperScreen and YouTube is ready!
```bash
sudo systemctl restart KlipperScreen
```



# Usage

## Normal usage:
On your Klipper screen, navigate to `Home > Actions` and launch YouTube via the YouTube button

## Usage during printing
<i>Note: The print may stop for a second but usually continues when chrome started</i>

On your Klipper screen, got to `Macros` and choose START_YOUTUBE

## Embedded into your .gcode print file

In orca slicer, hover Sovol sv 07 and click the edit button appearing on the right, navigate to `Machine G-code` and add `START_YOUTUBE` in the `Machine start G-code` textbox.

You can also choose a layer and select `+` > `add Custom G-code`.

## About the keyboard
Hide the keyboard using `x` in the top right corner on the keyboard.
Show keyboard using the keyboard button in the top left corner of the screen.


# 🥳 Happy printing (and watching)!


















