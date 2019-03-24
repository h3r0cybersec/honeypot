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

class manager(object):
    """
        Load and start servers instance from the configuration file
    """
    
    def __init__(self, config_obj):
        # active service instances
        self.__service_instances = []
        # loggers
        self.__loggers = {}
        # active service configurations
        self.__fileconfig = self.__load_configuration(config_obj)

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
        
    def __load_configuration(self, config):
        """
            Load configurations
            @param config: JSON obj that contain all configurations
        """
        pass


