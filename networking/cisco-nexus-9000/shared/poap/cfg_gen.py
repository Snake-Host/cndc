#!/usr/bin/env python3

import yaml
import re
import os
import sys


try:
    with open("poap.yml", "r") as file:
        cfg = yaml.safe_load(file)
except FileNotFoundError:
    print("The configuration file 'poap.yml' does not exist!")
    sys.exit(1)


if not os.path.isdir("/srv/tftp/cfg"):
    print("The required folder to store the configuration '/srv/tftp/cfg' does not exist!")
    sys.exit(1)


# Extract the switch image
switch_img = cfg["switch-img"]


# Function to transform MAC address
def transform_mac(mac):
    # Remove separators (colon, hyphen, dot) and convert to uppercase
    cleaned_mac = re.sub(r"[.:-]", "", mac).upper()
    return cleaned_mac


# Loop through each switch
for switch_entry in cfg["switch-id"]:
    # Get switch name and data
    switch_name = list(switch_entry.keys())[0]
    switch_data = switch_entry[switch_name]
    ip_address = switch_data["ipv4_address"]  # Includes the /24 mask
    mac_id = transform_mac(switch_data["mac_address"])

    # Build user configuration lines by looping through each user
    user_lines_list = []
    for user_entry in cfg["credentials"]:
        username = list(user_entry.keys())[0]
        user_data = user_entry[username]
        pwd = user_data["pwd"]
        ssh_key = user_data["ssh-key"]
        role = user_data["role"]

        user_lines_list.append(f"username {username} password 5 {pwd} role {role}")
        user_lines_list.append(f"username {username} sshkey {ssh_key}")

    user_lines = "\n".join(user_lines_list) + "\n" if user_lines_list else ""

    # Remove the trailing newline for the last user entry if exists
    if user_lines.endswith("\n"):
        user_lines = user_lines[:-1]

    # Generate the config template for this switch
    n9k_cfg = f"""\
!
hostname {switch_name}
!
{user_lines}
!
interface mgmt0
    vrf member management
    ip address {ip_address}
!
boot nxos bootflash:{switch_img}
!\
"""

    with open(f"/srv/tftp/cfg/conf_{mac_id}.cfg", "w") as cfg_file:
        cfg_file.write(n9k_cfg)

