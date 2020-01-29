from py2neo import Node, Graph, Relationship, NodeMatcher, RelationshipMatcher


def get_drug(symptomname):  # 由疾病名称查询对症药物
    graph = Graph("bolt://localhost:7687", username="neo4j", password="123456")
    #  nodematcher=NodeMatcher(graph)
    # relamatcher=RelationshipMatcher(graph)
    #   node=nodematcher.match('symptom',name=symptomname).first()#找到了该疾病
    # relamatcher.match((node,),r_type='适用于')

    str = 'MATCH a=(symptom{name:\'' + symptomname + '\'})-[:可使用]->(drug) return drug.name'
    print(str)
    result_list = list(graph.run(str).data())
    result=[]
    for oneresult in result_list:
        result.append(oneresult['drug.name'])
    print(result)
    return result
