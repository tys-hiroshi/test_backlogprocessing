import sys
#sys.path.append('/Users/maccat/projects/github/tys-hiroshi/test_backlogprocessing/.venv/lib/python3.8/site-packages')
# pip install PyYAML
# import yaml

# with open('config.yml') as file:
#     yml = yaml.load(file , Loader=yaml.SafeLoader)
#     print(yml)
from backlogapiprocessmodule import *
import os

ConfigFilePath = os.path.join(os.getcwd(), "config.yml")
LoggingConfigFilePath = os.path.join(os.getcwd(), "logging_debug.conf")
backlogapiprocess.run(ConfigFilePath, LoggingConfigFilePath)

