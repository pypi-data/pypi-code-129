# -*- coding: utf-8 -*-
import copy

from manoutils.config.defualtConfig import configItems


class ConfigManager(object):
    def __init__(self):
        self.configs = dict()
        self.loadConfigJsonItmes(configItems=configItems)

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(ConfigManager, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance

    def makeConfigName(mod, sub_mod="", desc=""):
        if sub_mod:
            return "{}_{}_{}".format(mod.upper(), sub_mod.upper(), desc.upper())
        else:
            return "{}_{}".format(mod.lower(), desc.lower())

    def getConfigItem(self, name=None, defaultVal=""):
        if not name:
            return copy.deepcopy(self.configs)
        else:
            return self.configs.get(name, defaultVal)

    def setConfigItem(self, name, value):
        setattr(self, name, value)
        self.configs.update({name: value})

    def getManoIp(self):
        return self.getConfigItem("MANO_IP")

    def getManoPort(self):
        return self.getConfigItem("MANO_PORT")

    def setManoIp(self, ip):
        self.setConfigItem("MANO_IP", ip)

    def setManoPort(self, port):
        self.setConfigItem("MANO_PORT", port)

    def loadConfigFile(self):
        pass

    def loadConfigJsonItmes(self,configItems):
        for name, value in configItems.items():
            self.setConfigItem(name=name, value=value)


configMgr = ConfigManager()
