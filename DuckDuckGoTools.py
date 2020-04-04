import requests
import json
import urllib


def duck_search(query):
    html_query = urllib.parse.quote_plus(query)
    url = "https://api.duckduckgo.com/?q={}&format=json&pretty=1".format(
        html_query)
    response = requests.get(url)
    json_resp = json.loads(response.text)
    return json_resp


def duck_summary(query):
    json_resp = duck_search(query)
    if json_resp['Answer'] != '':
        return json_resp['Answer']
    elif json_resp['AbstractText'] != '':
        return json_resp['AbstractText'] + "\n _ [source: " + json_resp[
            'AbstractSource'] + "]_"
    elif json_resp['Abstract'] != '':
        return json_resp['Answer']
    elif json_resp['AbstractURL'] != '':
        return json_resp['AbstractURL']


from nested_lookup import nested_lookup


def duck_related_topics(query):
    results = []
    for result in (nested_lookup('Text', duck_search(query)['RelatedTopics'])):
        results.append(result)
    return results