from functions.pluginid import pluginid_gen

class PluginOptions:
    def set(self, options = list):
        self.options = options;    

class Plugin:
    def __init__(self, name = str, util = list()):
        self.name = name
        self.util = util
        self.id = pluginid_gen()
        self.options = any;

    def getInfo(self):
        return self.name, self.util, self.id
    