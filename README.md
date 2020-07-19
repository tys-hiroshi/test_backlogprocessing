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
