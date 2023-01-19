# -*- coding: utf-8 -*-

import platform
from apimatic_core.api_call import ApiCall
from apimatic_core.types.error_case import ErrorCase
from square.exceptions.api_exception import APIException


class BaseApi(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        new_api_call_builder (APICall): Returns the API Call builder instance.
        auth_managers (dict): A dictionary which holds the instances of authentication managers.

    """

    @staticmethod
    def user_agent():
        return 'Square-Python-SDK/25.1.0.20230119 ({api-version}) {engine}/{engine-version} ({os-info}) {detail}'

    @staticmethod
    def user_agent_parameters():
        return {
            'engine': {'value': platform.python_implementation(), 'encode': False},
            'engine-version': {'value': "", 'encode': False},
            'os-info': {'value': platform.system(), 'encode': False},
        }

    def __init__(self, config):
        self._global_config = config
        self._config = self._global_config.get_http_client_configuration()
        self._http_call_back = self.config.http_callback
        self.api_call = ApiCall(config)

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    @property
    def new_api_call_builder(self):
        return self.api_call.new_builder

    @property
    def auth_managers(self):
        return self._global_config.get_auth_managers()
