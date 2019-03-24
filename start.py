#!/usr/bin/env python 3

"""
    AUTHOR : Cavallo Luigi
    DESCRIPTION:
    Entry file for the honeypot. Load system monitor e start all type of server's
    instance. It's also responsible to parse command line arguments and generate 
    port-fowarding for different service implemented in this honeypot. Before start
    it verify on the current system how many and what services are actualy active,
    and at the end of this analysis, start the instances of fake servers, based on 
    those found on the real machine. For convention the log file of all active 
    services on the system are stored in /machine-services/ dir; instead configuration
    file of the service the must be run are stored in /services-cfg/ dir.
    TODOS:
    -> Implement nmap scripts to scan the system
    -> Link Monitor instance
"""

import argparse
import os
import sys

from lib.utils.utils import message, is_root
from monitor import monitor

def help(parser):
    parser.print_help()

def check_service_cfg(file):
    """
        Verify the file
        @param file: JSON config file
    """
    services_cfg_root = os.path.join("services-cfg", file)
    
    if not os.path.exists(services_cfg_root) and file[-4:] is not "json":
        msg="%s is not a json file, or file doesn't exists yet" % file
        message(sym="[!]",message=msg, color="red")
        sys.exit(1)

def check_machine_services(params):
    """
        Verify if active.services file is been created
        @param file: .services log file 
    """
    if len(params) == 1:
        machine_services_root = os.path.join("machine-services", params[0])
        if not os.path.exists(machine_services_root):
            msg="%s doesn't not exists yet, use --createnow command to start scan now" % machine_services_root
            message(sym="[!]",message=msg, color="red")
            help(parser)
            sys.exit(1)
        else:
            if not machine_services_root.split(".")[1] == "services":
                msg="%s is not a 'services' file" % machine_services_root
                message(sym="[!]",message=msg, color="red")
                help(parser)
                sys.exit(1)
    elif len(params) == 2:
        # need to create now the file of services
        machine_services_root = os.path.join("machine-services", params[0])
        cmd = params[1]
        if not os.path.exists(machine_services_root):
            if cmd == "createnow":
                # start nmap default scan here
                pass
            else:
                msg="'%s' services file already exists" % cmd
                message(sym="[!]",message=msg, color="red")
                help(parser)
                sys.exit(1)
        else:
            msg="services file already exists don't use 'createnow' option"
            message(sym="[!]",message=msg, color="red")
            help(parser)
            sys.exit(1)
    else:
        msg="invalid arguments"
        message(sym="[!]",message=msg, color="red")
        help(parser)
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="start different fake services to research hacker's attack pattern to network services")
    parser.add_argument("scan_log_file", help="scan the machine searching for active services. Scan type depens on the list of command passed", 
                        nargs="+")
    parser.add_argument("service_config_file", help="start services from the configuration file passed")

    # get all values
    args  = parser.parse_args()

    if is_root():
        # check parsed value
        check_machine_services(args.scan_log_file)
        check_service_cfg(args.service_config_file)
        # start honeypot
        pass
    else:
        message(sym="[#]", message="root privileges are required", color="yellow")
    
