from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry

REGISTRY = CollectorRegistry(auto_describe=False)

graylog_index_count_num = Gauge("graylog_index_count_num", "graylog索引数量", ['id','index_prefix'],registry=REGISTRY)
graylog_index_size_bytes = Gauge("graylog_index_size_bytes", "graylog 索引容量", ['id','index_prefix'], registry=REGISTRY)
graylog_sidecar_count_num = Gauge("graylog_sidecar_count_num", "graylog sidecar 数量",['host'], registry=REGISTRY)
graylog_cluster_info = Gauge("graylog_cluster_info","graylog 集群参数", ['id','index_prefix'], registry=REGISTRY)
graylog_sidecar_node_status = Gauge("sidecar_node_status","graylog sidecar 节点运行状态",['sidecar_node_name','sidecar_node_system','sidecar_node_ip','sidecar_node_collect_status'],registry=REGISTRY)
def clear_metrics():
  graylog_index_count_num.clear()
  graylog_index_size_bytes.clear()
  graylog_sidecar_count_num.clear()
  graylog_cluster_info.clear()
  graylog_sidecar_node_status.clear()
