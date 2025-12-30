# Steps to follow for the manual implementation:

- Install and configure the DHCP and TFTP services accrodingly to your environement using the predifined config files.

- Change the TFTP server ip address on the poap.py file

- Generate the md5 hash for the `poap.py` file using the appropriate script `poap_md5.sh`

- Keep in mind that the **DHCP** server ip address and range are temporary for the **POAP** process and should be changed later on.

- To generate the configuration files of the switches for the **POAP** process you have to modify the `poap.yml` accordingly to your environment and run the `cfg_gen.py` script. **NOTE**: if the `poap.yml` file does not exist, there's a sample file named `poap.example.yml` that you can copy from.