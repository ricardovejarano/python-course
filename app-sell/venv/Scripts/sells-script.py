#!"e:\desarrollo\python\curso platzi\code\app-sell\venv\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'sells','console_scripts','sells'
__requires__ = 'sells'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sells', 'console_scripts', 'sells')()
    )
