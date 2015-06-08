# -*- coding: utf-8 -*-

"""
Module to display your AG DSN traffic

Show how much of your AG DSN traffic you used today in your
statusbar

Configuration parameters:
    - cache_timeout : refresh intervall in seconds

@author Matthes Lipke matthes.lipke@gmail.com
@license BSD
"""

import time
import requests

class Py3status:
    # available configuration parameters
    cache_timeout = 120
    traffic_url = "https://atlantis.wh2.tu-dresden.de/traffic/getMyTraffic.php"

    def __init__(self):
        pass

    def kill(self, i3s_output_list, i3s_config):
        pass

    def on_click(self, i3s_output_list, i3s_config, event):
        pass
    
    def traffic(self, i3s_output_list, i3s_config):
        response = requests.get(traffic_url).json()
        total = response.get("traffic").get("in") + response.get("traffic").get("out")
        num, dec = str(total).split(".")
        traffic = num + "." + dec[0:3] + " MiB"
        output = {
                "cached_until": time.time() + self.cache_timeout,
                "full_text": traffic
                }
        return output

class Traffic:
    def __init__(self):
        self.TRAFFIC_URL = "https://atlantis.wh2.tu-dresden.de/traffic/getMyTraffic.php"
    
    def get(self):
        response

        try:
            response = requests.get(self.TRAFFIC_URL).json()
        except:
            print("Error")

        if response.get("version") == 2:
            return response.get("")

class ResponseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

if __name__ == "__main__":
    status = Py3status()

    config = {
        "color_bad": "#FF0000",
        "color_degraded": "#FFFF00",
        "color_good": "#00FF00"
    }

    while True:
        print(status.traffic([], config))
        time.sleep(1)
