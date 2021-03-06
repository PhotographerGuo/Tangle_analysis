import matplotlib.pyplot as plt
import networkx as nx
import json
#from memory_profiler import profile

#profile
def cumulative():
    G_tmp = nx.DiGraph()

    # links = [(1,0),(2,0),(3,2),(4,2),(5,4),(6,4),(4,1),(6,3)]
    # for link in links:
    #   G_tmp.add_edge(link[0], link[1])

    ####################
    with open("branch_link_IRI_1.1.2.2_13157.json") as f0:
        branch_link = json.load(f0)
    with open("trunk_link_IRI_1.1.2.2_13157.json") as f1:
        trunk_link = json.load(f1)
    with open("transactions_2016 with c_weight_correct.json") as f:
        data = json.load(f)
    for e in range(len(trunk_link)):
        a = trunk_link[e][0]
        b = trunk_link[e][1]
        G_tmp.add_edge(a, b)
    for e in range(len(branch_link)):
        a = branch_link[e][0]
        b = branch_link[e][1]
        G_tmp.add_edge(a, b)
    ################

    # print(G_tmp.nodes)
    d = dict()
    for n in G_tmp.nodes:
        d[n] = {n}

    num = 0
    site = []
    while G_tmp.nodes:
        print("Iteration: ", num)
        print("Calculate leafs")
        leafs = []
        for i in G_tmp.nodes:
            if G_tmp.in_degree(i) ==0:
                leafs.append(i)

        # leafs = [i for i in G_tmp.nodes if G_tmp.in_degree(i) == 0]

        for n in leafs:
            print("for",n,"in leaf")
            site.append(n)
            for (j,s) in G_tmp.edges:
                if j !=n:
                    continue
                    # print('n,s',n,s)
                d[s] = nx.ancestors(G_tmp,s)
                    # print('d[s]',d[s])
                d.update({s:d[n].union(d[s])})

            # print("Number of entries: ", len([e for k in d.keys() for e in list(d[k])]))
            # leaf.append(s)
            # leaf.remove(n)
        print("#Leafs = ", len(leafs), "Prepare update of dictionary")
        print("site: ",len(site))
        #print("Leaf is: ", (data[i]["hash"] for i in leafs))
        G_tmp.remove_nodes_from(leafs)
        num+=1
        # if num == 1000 :
        #     return

        # for s in nx.descendants(G_tmp,n):
        #     d.update({s:d[n].union(d[s])})
        # leaf.append(s)
        # leaf.remove(n)

    result = dict()
    for k, v in d.items():
        result[k] = len(v)
    print(result)

    with open("dict.json", "w+") as f:
        json.dump(result,f)

cumulative()
