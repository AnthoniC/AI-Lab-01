
# coding: utf-8

# Stuff

# In[9]:


#imports?
import numpy as np


# In[10]:


class Puzzle:
    ACTIONS = ["up", "down", "left", "right"]
    
    
    def __init__(self, newTiles = None):
        self.tiles = newTiles #2d 3x3 array
        
        
    def successor(self, action):
        print("zzzzz")
        temp = np.array(self.tiles, copy = True)
        for i in range(3):
            for k in range(3):
                if(temp[i][k] == 0):
                    r,c = i, k
        
        try:
            print(action)
            if(action == "up"):
                if(r == 0):
                    raise InvalidPuzzleStateException("InvalidPuzzleStateException")
                temp[r][c] = temp[r-1][c]
                temp[r-1][c] = 0
            elif(action == "down"):
                if(r == 2):
                    raise InvalidPuzzleStateException("InvalidPuzzleStateException")
                temp[r][c] = temp[r+1][c]
                temp[r+1][c] = 0
            elif(action == "left"):
                if(c == 0):
                    print("nooooo")
                    raise InvalidPuzzleStateException("InvalidPuzzleStateException")
                    
                temp[r][c] = temp[r][c-1]
                temp[r][c-1] = 0
            elif(action == "right"):
                if(c == 2):
                    raise InvalidPuzzleStateException("InvalidPuzzleStateException")
                temp[r][c] = temp[r][c+1]
                temp[r][c+1] = 0
                
        except InvalidPuzzleStateException:
            temp = None
        
        #print(temp)
        return temp
        
        
    def __str__(self): # Working
        return "%i %i %i\n%i %i %i\n%i %i %i\n" %(self.tiles[0][0], self.tiles[0][1], self.tiles[0][2],
                                                  self.tiles[1][0], self.tiles[1][1], self.tiles[1][2], 
                                                  self.tiles[2][0], self.tiles[2][1], self.tiles[2][2])
        
        
    def __eq__(self, other): # Working
        istrue = True
        for i in range(3):
            for k in range(3):
                if (self.tiles[i][k] != other.tiles[i][k]):
                    istrue = False
        return istrue
            
        
        
 


# In[11]:


class InvalidPuzzleStateException(Exception):
    pass


# In[12]:


from abc import ABC, abstractmethod

class Heuristic(object):
    
    
    def __init__(self, goal = None):
        self.goal = goal
    
    @abstractmethod
    def guestimate(self, state):
        pass


# In[13]:


class MisplacedHeuristic(Heuristic):
    
    
    def __init__(self, goal = None):
        super(MisplacedHeuristic, self).__init__(goal)
        
    def guestimate(self, state):
        num = 0
        for i in range(3):
            for k in range(3):
                if(state[i][k] != i*3 +k + 1):
                    num += 1
                    
        if(state[2][2] == 0):
            num -= 1
        return num


# In[14]:


class ManhattenHeuristic(Heuristic):
    
    
    
    def __init__(self, goal = None):
        super(ManhattenHeuristic,self).__init__(goal)
        
    def guestimate(self, state):
        s = 0
        for i in range(3):
            for k in range(3):
                if(state[i][k] != i*3 +k + 1):
                    if(state[i][k] == 0):
                        s += 2-i
                        s += 2-k
                    else:
                        r = (state[i][k]-1)//3
                        c = (state[i][k]-1)%3
                        s += abs(r-i)
                        s += abs(c-k)
        return s
                    


# In[15]:


a = MisplacedHeuristic()
print(a.guestimate(np.array([[1,8,6],[4,5,6],[7,1,0]])))


# In[16]:


b = ManhattenHeuristic()
print(b.guestimate(np.array([[1,8,6],[4,5,6],[7,1,0]])))

