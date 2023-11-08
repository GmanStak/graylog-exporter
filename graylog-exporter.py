import prometheus_client
import requests, json
from flask import Flask, Response
from arguments import get_arts
from metrics import *
from collect import *
from gevent import pywsgi

app = Flask(__name__)

args = get_arts()
host = args.ipaddress
port = args.port
graylog_server = args.grarlogserver
graylog_port = args.graylogport

@app.route('/')
def index():
    return "<h1>Customized Exporter</h1><br><a href='metrics'>Metrics</a>"

@app.route('/metrics')
def get_Graylog():
    graylog = Graylog(graylog_server, graylog_port,'admin','UMM_Admin67657')
    index_id_dic = graylog.get_index_id()
    for index_id,index_prefix in index_id_dic.items():
        id_size = graylog.get_index_id_size(index_id)
        documents = id_size['documents']
        size = id_size['size']
        graylog_index_count_num.labels(id=index_id,index_prefix=index_prefix).set(documents)
        graylog_index_size_bytes.labels(id=index_id,index_prefix=index_prefix).set(size)
    sidecar_num = graylog.get_sidecar_num()
    graylog_sidecar_count_num.labels(host=graylog_server).set(sidecar_num)
        sidecar_info_list = graylog.get_sidecar_node_status()
    for sidecar_info in sidecar_info_list:
        sidecar_node_name = sidecar_info['node_name']
        sidecar_node_system = sidecar_info['node_details']['operating_system']
        sidecar_node_ip = sidecar_info['node_details']['ip']
        collector_status = sidecar_info['node_details']['status']['collectors']
        if not collector_status:
           sidecar_node_collector_status = "None"
           graylog_sidecar_node_status.labels(sidecar_node_name=sidecar_node_name,sidecar_node_system=sidecar_node_system,sidecar_node_ip=sidecar_node_ip,sidecar_node_collect_status=sidecar_node_collector_status).set(0)
        else:
           sidecar_node_collector_status = collector_status[0]['message']
           if sidecar_node_collector_status == 'Running':
              graylog_sidecar_node_status.labels(sidecar_node_name=sidecar_node_name,sidecar_node_system=sidecar_node_system,sidecar_node_ip=sidecar_node_ip,sidecar_node_collect_status=sidecar_node_collector_status).set(1)
           else:
              graylog_sidecar_node_status.labels(sidecar_node_name=sidecar_node_name,sidecar_node_system=sidecar_node_system,sidecar_node_ip=sidecar_node_ip,sidecar_node_collect_status=sidecar_node_collector_status).set(0)
    graylog.logout()
    return Response(prometheus_client.generate_latest(REGISTRY), mimetype="text/plain")

if __name__ == '__main__':
    # app.run(host=host,port=port)
    server = pywsgi.WSGIServer((host, port), app)
    server.serve_forever()
