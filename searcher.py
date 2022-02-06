def beautifulresult(results:dict):
    major=results['result'];compressed=[];links=[]
    for x in major:compressed.append(x['accessibility']['title']);links.append(x['link'])
    return compressed,links