class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for w in words for c in w}
        indegree={c:0 for c in adj}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            minlen=min(len(w1),len(w2))
            if len(w1)>len(w2)  and w1[:minlen]==w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break
        q=deque(c for c in indegree if indegree[c]==0)
        res=[]
        while q:
            char=q.popleft()
            res.append(char)
            for neigbhr in adj[char]:
                indegree[neigbhr]-=1
                if indegree[neigbhr]==0:
                    q.append(neigbhr)
        if len(indegree)==len(res):
            return "".join(res)
        else:
            return ""

                



        