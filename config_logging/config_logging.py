#import configparser
#
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


"""
ログレベル順

critical
error
warning
info
debug
"""

import logging
import logging_test
import logging.config
import logging.handlers


#logging.basicConfig(level=logging.DEBUG, filename="test.log")
#formatter = "[%(asctime)s] %(levelname)s\nerror filepath -> %(filename)s"
#logging.basicConfig(level=logging.INFO, format=formatter)

#logging.basicConfig(level=logging.INFO)


#class NoPassFilter(logging.Filter):
#    def filter(self, record):
#        log_message = record.getMessage()
#        return "password" not in log_message
#
#
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
#logger.addFilter(NoPassFilter())
#logger.info("from main password = 'XXXXX'")
#logger.info("from main")

#logging.jsonのファイルに書かれている設定を反映することができる
#import json
#
#with open("logging_config.json", "r") as json_file:
#    json_config = json.load(json_file)
#
#logging.config.dictConfig(json_config)
#logger = logging.getLogger("my_application")
#
#logger.info ("info message")

#
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText
#
#def send_gmail(subject, body, to_email, from_email, from_password):
#    # MIMEメッセージを作成
#    msg = MIMEMultipart()
#    msg['From'] = from_email
#    msg['To'] = to_email
#    msg['Subject'] = subject
#
#    # メールの本文を追加
#    msg.attach(MIMEText(body, 'plain'))
#
#    with open("config_logging.py", "r") as f:
#        attachment = MIMEText(f.read(), "plain")
#        attachment.add_header(
#            "Content-Disposition",
#            "attachment",
#            filename="lesson.txt"
#            )
#        msg.attach(attachment)
#
#    try:
#        # GmailのSMTPサーバに接続
#        server = smtplib.SMTP('smtp.gmail.com', 587)
#        server.starttls()  # TLS(Transport Layer Security)を開始
#        server.login(from_email, from_password)  # Gmailにログイン
#        server.send_message(msg)  # メールを送信
#        server.quit()
#        print("メール送信成功！")
#    except Exception as e:
#        print(f"メール送信エラー: {e}")
#
## 送信するメールの情報を設定
#subject = "テストメールの件名"
#body = "これはテストメールの本文です。"
#to_email = "XXXXX@gmail.com"
#from_email = "XXXXX@gmail.com"
#from_password = "XXXXX"
#
## メールを送信する関数を呼び出す
#send_gmail(subject, body, to_email, from_email, from_password)
#
#

import logging.handlers

smtp_host = "smtp.gmail.com"
smtp_port = 587
from_email = "XXXXX@gmail.com"
to_email = "XXXXX@gmail.com"
username = "XXXXX@gmail.com"
password = "XXXXX"

logger = logging.getLogger("email")
logger.setLevel(logging.CRITICAL)
smpt_handler = logging.handlers.SMTPHandler(
    (smtp_host, smtp_port), from_email, to_email,
    subject="Admin test log",
    credentials=(username, password),
    secure=(),
    timeout=20
)
logger.addHandler(smpt_handler)

logger.critical("critical")
logger.info("info")
