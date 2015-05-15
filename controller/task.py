class DeployTask(object):
    def __init__(self,xml_config):
        self.config = xml_config

class CheckTask(object):
    def __init__(self,sys_id):
        self.sys_id = sys_id
