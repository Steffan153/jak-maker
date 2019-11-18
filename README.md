## Installation

Make sure you have [Jade Application Kit](https://github.com/codesardine/Jade-Application-Kit) installed.

Clone repo:
```bash
git clone https://github.com/Steffan153/jak-maker.git
```

## Usage

```bash
cd jak-maker
sudo python create.py
```

Example input:
```
Name: Manjaro Wiki
Description: Manjaro Wiki
Command to execute program: manjaro-wiki
Icon path (PNG), no need to keep it, it will be copied to another location: /path/to/manjaro-icon.png
Category: Accessories
Website URL: https://wiki.manjaro.org
```

## Notes

* Make sure to use sudo, or it may not work properly.
* The PNG icon's name you give must not exist in `/usr/share/pixmaps/`.
* "Command to execute program" must not exist in `/usr/bin/`, or `/usr/share/applications/{name}.desktop`.
