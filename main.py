import sys
#sys.path.append('/Users/maccat/projects/github/tys-hiroshi/test_backlogprocessing/.venv/lib/python3.8/site-packages')
# pip install PyYAML
# import yaml

# with open('config.yml') as file:
#     yml = yaml.load(file , Loader=yaml.SafeLoader)
#     print(yml)
from backlogapiprocessmodule import *
import os

from chatworkpy.chatwork.rooms import Rooms
from chatworkpy.config import Config

ConfigFilePath = os.path.join(os.getcwd(), "config.yml")
try:
    LoggingConfigFilePath = os.path.join(os.getcwd(), "logging_debug.conf")
    raise ValueError("Error aaaaa")
    backlogapiprocess.run(ConfigFilePath, LoggingConfigFilePath)
except Exception as e:
    chatwork_config = Config(ConfigFilePath).content["ALERT"]
    api_token = chatwork_config["CHATWORK_API_TOKEN"]
    room_id = chatwork_config["CHATWORK_ROOM_ID"]
    to_id_list = chatwork_config["CHATWORK_TO_ID_LIST"].split(',')
    chatwork_rooms = Rooms(api_token, room_id)
    import traceback
    error_message = traceback.format_exc()
    chatwork_rooms.send_message(error_message, to_id_list)