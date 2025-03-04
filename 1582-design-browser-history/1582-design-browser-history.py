class BrowserHistory:

    def __init__(self, homepage: str):
        self.home = homepage
        self.sites = [self.home]
        self.pt = 0

    def visit(self, url: str) -> None:
        self.sites = self.sites[:self.pt+1]
        self.sites.append(url)
        self.pt += 1
    def back(self, steps: int) -> str:
        self.pt -= steps
        if self.pt < 0:
            self.pt = 0
            return self.home
        return self.sites[self.pt]

    def forward(self, steps: int) -> str:
        self.pt += steps

        if self.pt < len(self.sites):
            return self.sites[self.pt]
        else:
            self.pt = len(self.sites)-1
            return self.sites[-1]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)