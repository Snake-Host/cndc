#!/bin/env python3
#md5sum="eb08329071ac99ccc2739640439152a3"

import os
from cli import *

srv = "192.168.0.1" # TODO: Change the TFTP server IP address accordingly to your environment

MAC = os.environ['POAP_MAC']

cli(f"copy tftp://{srv}/cfg/conf_{MAC}.cfg bootflash:poap.cfg vrf management")

cli(f"copy bootflash:poap.cfg scheduled-config")

cli(f"copy bootflash:poap.cfg running-config")

cli(f"copy running-config startup-config")