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
from json import loads

class manager(object):
    """
        Load and start servers instance from the configuration file
    """
    
    def __init__(self, active_obj):
        # Services file config
        self.root_service_cfg = os.path.join("services-cfg", active_obj)
        # active service instances populated after start_service execution
        self.__service_instances = []
        # loggers
        self.__loggers = []
        # active service configurations
        self.__services_to_activate = self.__load_configuration(active_obj)

    def start_service(self):
        """
            Start the various service. Runtime importation of 
            single service instance will be executed. At the end
            a copy of this instance will saved in __service_instances
            attribure.
        """
        pass

    def load_services_instance(self):
        return self.__service_instances

    def shutdown(self):
        """
            Shutdown an active service instance
        """
        # TODO: Must check if instance is really active
        pass
        
    def __load_configuration(self, active):
        """
            In base of 'active' service found on system, this
            method loads only the configuration for active 
            service, from del service configuration file.
            @param active: list of active services
        """
        with loads(self.root_service_cfg) as config:
            print(config)
        