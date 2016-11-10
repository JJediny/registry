import json
import rawes

def test_multiindex_search():
    es_client = rawes.Elastic('localhost:9200')
    es_client.put('/index1/data/1', data = {
        'text' : 'here is some text'
    })
    es_client.put('/index2/data/1', data = {
        'text' : 'here is more text in another index'
    })

    # search over multiple indexes like so
    response = es_client.get('/index1,index2/_search?q=*:*')
    assert response['hits']['total'] == 2
