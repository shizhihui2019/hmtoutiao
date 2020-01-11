import os
import yaml
from config import BASE_URL

print(BASE_URL)

def read_yaml(filename):
    with open(BASE_URL+os.sep+"data"+os.sep+filename,"r",encoding="utf-8") as  f:
        arr = []
        for data in yaml.load(f,Loader=yaml.FullLoader).values():
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))