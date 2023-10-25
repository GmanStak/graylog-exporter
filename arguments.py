import argparse

def get_arts():
    parser = argparse.ArgumentParser(description="graylog exporter")
    parser.add_argument("-a","--ipaddress",type=str,default='0.0.0.0', help="指定Exporter启动地址")
    parser.add_argument("-p","--port",type=int,default=9088, help="指定Exporter启动端口")
    parser.add_argument("-c","--config",type=str,default="./conf/config.json", help="指定配置文件路径")
    parser.add_argument("-s","--grarlogserver",type=str,default='localhost', help="指定graylog server URL地址")
    parser.add_argument("-sp", "--graylogport", type=int, default=9000, help="指定graylog server 端口")
    # parser.add_argument("-h", "--help", action="help", help="参数信息")
    args = parser.parse_args()
    return args
