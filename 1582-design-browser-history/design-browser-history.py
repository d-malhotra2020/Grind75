class ListNode:
    def __init__(self, val, previous=None, next=None):
        self.val = val
        self.previous = previous
        self.next = next
class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = ListNode(homepage)

    def visit(self, url: str) -> None:
        self.current.next = ListNode(url, self.current)
        self.current = self.current.next

    def back(self, steps: int) -> str:
        while self.current.previous and steps > 0:
            self.current = self.current.previous
            steps -=1
        return self.current.val
    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -=1
        return self.current.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)