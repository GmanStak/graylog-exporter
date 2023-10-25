import json
from requests import Session

class Graylog(object):
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.password = password
        self.username = username
        self.password = password
        self.session = Session()
        self.session.auth = (self.username,self.password)

    def get_index_id(self):
        id_index_prefix = {}
        url = f"http://{self.host}:{self.port}/api/system/indices/index_sets"
        response = self.session.get(url)
        graylog_info = json.loads(response.text)
        index_sets_total = graylog_info['index_sets']
        for index_sets in index_sets_total:
            id_index_prefix[index_sets['id']] = index_sets['index_prefix']
        response.close()
        return (id_index_prefix)
    def get_index_id_size(self,id):
        try:
            url = f"http://{self.host}:{self.port}/api/system/indices/index_sets/{id}/stats"
            response = self.session.get(url)
            index_id_size = json.loads(response.text)
            response.close()
            return index_id_size
        except:
            return False
    def get_sidecar_num(self):
        try:
            url = f"http://{self.host}:{self.port}/api/sidecars?query=sssssss"
            response = self.session.get(url)
            sidecar_total = json.loads(response.text)
            sidecar_num = sidecar_total['total']
            response.close()
            return sidecar_num
        except:
            return False
