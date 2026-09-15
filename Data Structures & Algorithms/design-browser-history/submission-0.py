class Node:

    def __init__(self,url:str):
        self.url = url
        self.prev = None
        self.next = None

class BrowserHistory:
    
    def __init__(self, homepage: str):
        first = Node(homepage)
        self.curr = first
        
    def visit(self, url: str) -> None:
        new = Node(url)
        self.curr.next = new
        new.prev = self.curr
        self.curr = new
        self.curr.next = None

    def back(self, steps: int) -> str:
        count = steps
        while self.curr.prev != None and count > 0 :
            self.curr = self.curr.prev
            count -= 1
        return self.curr.url
        
    def forward(self, steps: int) -> str:
        count = steps
        while self.curr.next != None and count > 0 :
            self.curr = self.curr.next
            count -= 1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)