import os
import json
import configparser

settings = None

class Settings(object):
    """Simple singleton class for managing and accessing settings"""
    def __init__(self):
        self.config = configparser.ConfigParser(inline_comment_prefixes=('#',))
        self.config.optionxform = str  
        self.config.read(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini'), encoding='utf-8')
        self.automation_type = self.config['TEST']['TYPE']
        print(self.config['TEST']['TYPE'])
        if self.automation_type == 'MOBILE':
            self.avd_server = self.config['AVDdata']['AVD_SERVER']
            self.capabilities = {
                "app": self.config['AVDdata']['AVD_APP'],
                "deviceName": self.config['AVDdata']['AVD_DEVICE'],
                "platformName": self.config['AVDdata']['PLATFORM_NAME']
                #"enforceAppInstall" : "true"
            }
        elif self.automation_type == 'WEB':
            self.url = self.config['WEB']['url']
            self.browser = self.config['WEB']['browser']
            self.driver_timeout = int(self.config['WEB']['driver_timeout'])
        else:
            print("Automation type inserted by wrong value")

settings = Settings()
