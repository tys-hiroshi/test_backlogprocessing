# 

```
deactivate
python3 -m venv .venv
source .venv/bin/activate
pip3 install backlogprocessing
pip3 install azure-functions
pip3 freeze | grep -v "pkg-resources" > requirements.txt
pip install --upgrade pip setuptools
pip3 install -r requirements.txt
```

pip3 install setuptools==45


## Alert to chatwork

Write config.yml blow elements

### config.yml

```
ALERT:
  CHATWORK_API_TOKEN : 
  CHATWORK_ROOM_ID : 
  CHATWORK_TO_ACCOUNT_LIST : 
   - ID : ""
     NAME : ""
```

### NOTE: it's example

```
chatwork_config = Config(ConfigFilePath).content["ALERT"]
api_token = chatwork_config["CHATWORK_API_TOKEN"]
room_id = chatwork_config["CHATWORK_ROOM_ID"]
to_account_list = chatwork_config["CHATWORK_TO_ACCOUNT_LIST"]
accounts_dict = []
for account in to_account_list:
    accounts_dict.append({"account_id" : account["ID"], "name" : account["NAME"]})
chatwork_rooms = Rooms(api_token, room_id)
import traceback  ## NOTE: it's example
error_message = traceback.format_exc()  ## NOTE: it's example
chatwork_rooms.send_message(error_message, accounts_dict)
```