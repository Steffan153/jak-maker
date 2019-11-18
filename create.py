from os import path, chmod
from shutil import copyfile

name = input("Name: ")
desc = input("Description: ")
bin_name = input("Command to execute program: ")
old_icon = input("Icon path (PNG), no need to keep it, it will be copied to another location: ")
category = input("Category: ")
url = input("Website URL: ")

icon = "/usr/share/pixmaps/" + path.basename(old_icon)

copyfile(old_icon, icon)

python_script = f"""#!/usr/bin/env python

from JAK.Application import JWebApp

url = "https://www.udemy.com"
JWebApp(title="{name}", web_contents="{url}", online=True).run()
"""

desktop_file = f"""#!/usr/bin/env xdg-open
 
[Desktop Entry]
Name={name}
Comment={desc}
Exec={bin_name}
Icon={icon}
Terminal=false
Type=Application
Categories={category};
"""

with open("/usr/bin/" + bin_name, 'x') as py: print(python_script, file = py)
with open(f"/usr/share/applications/{bin_name}.desktop", 'x') as d: print(desktop_file, file = d)

chmod("/usr/bin/" + bin_name, 0o755)
