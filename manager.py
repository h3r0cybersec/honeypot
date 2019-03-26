#!/usr/bin/env python3 

"""
    AUTHOR : Cavallo Luigi
    DESCRIPTION:
    This module is responsible for loading the various server configurations with
    consequent instantiation of the individual defined servers. Instances that will 
    be created are that in /trap_servers directory.
    TODOS:
    -> Finish implementing
"""
import os
from lib.utils.utils import message
from importlib import import_module
from pprint import pprint

class manager(object):
    """
        Load and start servers instance from the configuration file.
        it parses the file in search of the services active in the machine, 
        saved in the 'active' field and starts the false services equal to 
        those currently active. After this it waits for any commands from 
        the user.
    """
    
    def __init__(self, cfg: object):
        # active service instances populated after start_service execution
        self.__service_instances = []
        # loggers
        self.__loggers = []
        # active service configurations
        self.__services_to_activate = None

    def start_service(self):
        """
            Start the various service. Runtime importation of 
            single service instance will be executed. At the end
            a copy of this instance will saved in __service_instances
            attribure.
        """
        pass

    def get_active_services_instance(self):
        return self.__service_instances

    def shutdown(self):
        """
            Shutdown an active service instance
        """
        # TODO: Must check if instance is really active
        pass
        