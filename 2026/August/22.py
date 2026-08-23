# Today will be focusing on coding 

# In memory file system 

class TrieNode:

  def __init__(self, isFile = False):
    self.isFile = isFile
    self.child = defaultdict(TrieNode)
    self.content = ""

class FileSystem:
   def __init__(self):
       self.root = TrieNode()

   def find(self, path, create = False): 
        if len(path) == 1:
          return self.root
        curr = self.root
        for word in path.split("/")[1:]:
            if word not in curr.child and not create:
              return None
            curr = curr.child[word]
         return curr

   def ls(self, path):
      curr = self.find(path)
      if curr.isFile:
        return path.split("/")[-1]
      return sorted(curr.child.keys())

   def addContent(self, path, content):
      node = self.find(path, True)
      node.isFile = True
      node.content += content

   def mkdir(self, path):
      node = self.find(path, True)

   def readContentFromFile(self, path):
      node = self.find(path)
      if node.isFile:
        return node.content
      return None
