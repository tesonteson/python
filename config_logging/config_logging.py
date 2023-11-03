import configparser

#config = configparser.ConfigParser()
#config["Default"] = {
#    "debug": True
#}
#config["web_server"] = {
#    "host": "127.0.0.1",
#    "port": 80
#}
#config["db_server"] = {
#    "host": "127.0.0.1",
#    "port": 3306
#}
#
#with open("config.ini", "w") as config_file:
#    config.write(config_file)

#config = configparser.ConfigParser()
#config.read("config.ini")
#print(config["web_server"])
#print(config["web_server"]["host"])


#import yaml
#
#with open("config.yml", "w") as yaml_file:
#    yaml.dump({
#        "web_server": {
#            "host": "127.0.0.1",
#            "port": 80
#        },
#        "db_server": {
#            "host": "127.0.0.1",
#            "port": 3306
#        }
#    }, yaml_file, default_flow_style=False)
#
#with open("config.yml", "r") as yaml_file:
#    data = yaml.load(yaml_file, Loader=yaml.SafeLoader)
#    print(data, type(data))



import logging

#formatter = "%(asctime)s:%(levelname)s:%(message)s"
#logging.basicConfig(format=formatter, level=logging.DEBUG)
#
#logging.critical("critical")
#logging.error("error")
#logging.warning("warning")
#logging.info("info")
#logging.debug("debug")

logging.basicConfig(level=logging.INFO)
