
# coding: utf-8

# In[ ]:


import numpy as np
import heapq
import Puzzle


# In[ ]:


class SearchNode:
    
    def __init__(self, state, parent, action, cost, depth, f):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth
        self.f_val = f
        #print(state)
        #print("aye")
        
        
    def getF(self, h):
        self.f_val = h.guestimate(self.state.tiles)
        
        
        
        
    def childNodeFromAction(self):
        new = []
        print("ugh")
        
        a = self.state.successor("up")
        #print("Way")
        temp = self.__init__(a, self, "up", self.cost+1, self.depth +1, self.depth + 1)
        #print("wahhh?")
        new.append(temp)
        #print(temp)
        print(new)
        
        try:
            b = self.state.successor("down")
            new.append(self.__init__(b, self, "down", self.cost+1, self.depth +1, self.depth + 1))
        except:
            print("fail")
        
        try:
            c = self.state.successor("left")
            new.append(self.__init__(c, self, "left", self.cost+1, self.depth +1, self.depth + 1))
        except:
            print("fail")
        
        try:
            d = self.state.successor("right")
            new.append(self.__init__(d, self, "right", self.cost+1, self.depth +1, self.depth + 1))
        except:
            print("fail")
        
        print(new)
        return new
    
        
    def solution(self):
        current = self
        path = []
        path.append(current.action)
        while(current.parent):
            current = current.parent
            path.insert(current.action,0)
        return path
        
        
    def path(self):
        path = []
        thing = self
        while(thing.parent != None):
            path.insert(0, thing.parent)
            thing = thing.parent
        
        
    def __lt__(self, other):
        return self.f_val < other.f_val
        
        
    def __eq__(self, other):
        return self.f_val == other.f_val
        
        
    def __hash__(self):
        return hash(self.__str__())
        
        
    def __str__(self):
        return str(self.state)
        

        
        


# In[ ]:


class AStarSearch:
    
    
    def __init__(self, start):
        temp = Puzzle.Puzzle(start)
        print(1)
        print(temp)
        self.goalState = Puzzle.Puzzle(np.array([[1,2,3],[4,5,6],[7,8,0]]))
        #self.heuristic = Puzzle.ManhattenHeuristic()
        self.startState = SearchNode(Puzzle.Puzzle(start), None, None, 1, 0, 0)
        print(self.startState)
        self.visited = set()
        self.fringe = []
        heapq.heappush(self.fringe, self.startState)
        
        
        
    # Finds a series of actions that go from the start state to the goal state, returns None if no solution
    def search(self):
        temp = heapq.heappop(self.fringe)
        print(temp.state == self.goalState)
        while(temp):
            print("do we even get here")
            if (temp.state == self.goalState):
                #print("what?")
                return temp.solution()
            else:
                self.visited.add(temp)
                print(self.visited)
                print("made it here")
                new = temp.childNodeFromAction()
                print(new)
                for i in new:
                    #i.getF(self.heuristic)
                    if i not in self.visited:
                        #print("yo")
                        heapq.heappush(self.fringe, i)
                try:
                    temp = heapq.heappop(self.fringe)
                except:
                    temp = None
        
        return None
        
        
    def report(self):
        n = None
    
    
    
    
    


# In[ ]:


a = Puzzle.Puzzle(np.array([[1,2,3],[4,5,6],[7,8,0]]))
b = Puzzle.Puzzle(np.array([[7,2,4],[5,0,6],[8,3,1]]))
b = np.array([[7,2,4],[5,0,6],[8,3,1]])
#print(a)
#print(b)
c = AStarSearch(b)
print(c.search())

