
BUCKET_SIZE = 10
class Hash: 
    def __init__(self):
        self.table = [None] * BUCKET_SIZE
    def hash(self, key):
        return key % BUCKET_SIZE
    def insert(self, key):
        index = self.hash(key) #starts by setting index
        if self.table[index] == None: # checks if index is empty
            self.table[index] = key # if index is empty insert
        else: # if index is not empty
            while self.table[index] != None:
                index = (index + 1) % BUCKET_SIZE
            self.table[index] = key 
    def search(self, key):
        index = self.hash(key)
        if self.table[index] == key:
            return True
        else:
            while self.table[index] != None:
                if self.table[index] == key:
                    return True
                index = (index + 1) % BUCKET_SIZE
    def delete(self, key):
       index = self.hash(key)
       if self.table[index] == key:
              self.table[index] = None
       else:
            while self.table[index] != None:
                if self.table[index] == key:
                    self.table[index] = None
                index = (index + 1) % BUCKET_SIZE
    def resize(self, new_size):
        new_table = [None] * new_size # create new table with new size
        print(len(new_table))
        for i in range(len(self.table)): # iterate through the old table to capture values
            
            if self.table[i] != None: # if the value is not none
                new_table[i] = self.table[i] # and map the old value in new table
            else:
                continue
        self.table = new_table
    
       
        

hash = Hash()
hash.insert(10)
hash.insert(20)
hash.insert(30)
hash.delete(20)
print(hash.table)
hash.resize(30)
print(hash.table)