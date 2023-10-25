from prometheus_client import Gauge
from prometheus_client.core import CollectorRegistry

REGISTRY = CollectorRegistry(auto_describe=False)

graylog_index_count_num = Gauge("graylog_index_count_num", "graylog索引数量", ['id','index_prefix'],registry=REGISTRY)
graylog_index_size_bytes = Gauge("graylog_index_size_bytes", "graylog 索引容量", ['id','index_prefix'], registry=REGISTRY)
graylog_sidecar_count_num = Gauge("graylog_sidecar_count_num", "graylog sidecar 数量",['host'], registry=REGISTRY)
graylog_cluster_info = Gauge("graylog_cluster_info","graylog 集群参数", ['id','index_prefix'], registry=REGISTRY)
