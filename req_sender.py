import base64
import json
import logging
import os
import sys

import api.app_config as app_config
import api.image_convert as image_convert

import requests

#logging.basicConfig(filename='log/logger.log', level=logging.DEBUG)

def send_image(path: str):
    if path is None or path == "":
        raise ValueError("Illegal Argument!")

    file_name = os.path.basename(path)
    enc = image_convert.encode((path))
    #res = requests.get("http://{0}:{1}".format(app_config.host(), app_config.port()),auth=('misumi','misumi3612'),params="amit")
    #print(res)
    res = requests.post("http://{0}:{1}/api/v1".format(app_config.host(), app_config.port()),
                        json.dumps({"file_name": file_name, "image": enc}),
                        auth=('misumi','misumi3612'),
                        headers={"Content-Type": "application/json"})
    print(res)
    logging.debug("response json: %s", res.json())


def resolve_path(path: str) -> str:
    ret = path
    sep = os.sep
    cwd = os.getcwd()
    if path.startswith("." + sep):
        ret = os.path.abspath(os.path.join(cwd, path))

    if not os.path.exists(ret) or os.path.isdir(ret) or not ret.startswith(cwd):
        raise ValueError("Illegal Path")
    return ret


if __name__ == "__main__":
    path = "images\sample.png"
    #path = sys.argv[1]
    #print("args1:{0}".format(sys.argv[1]))
    send_image(path)
