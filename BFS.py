# 添加已检测的队列，防止陷入死循环

# -*- coding:UTF-8 -*-

from collections import deque

def person_is_seller(person):
    return person[-1] == 'm'





def search(firstname):

    search_queue = deque()

    graph = {}
    graph['you'] = ['alice','bob','claire']
    graph['bob'] = ['anuj','peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom','jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []
    print(search_queue)
    print(graph)

    search_queue += graph[firstname]
    print('*' * 20 + '\n')
    print(search_queue)
    searched = set()
    # searched = set() #已检查的序列

    while search_queue:
        person = search_queue.popleft()

        if person not in searched:
            if person_is_seller(person):
                print('this person: '+ person + " is seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False




if __name__=="__main__":
    search('you')