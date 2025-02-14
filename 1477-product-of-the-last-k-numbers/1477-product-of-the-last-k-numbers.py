class ProductOfNumbers:
    def __init__(self):
        self.my_list = [1]  # Store prefix products

    def add(self, num: int) -> None:
        if num == 0:
            self.my_list = [1]  # Reset prefix product list
        else:
            self.my_list.append(self.my_list[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.my_list):  
            return 0  # If k is out of bounds, return 0

        return self.my_list[-1] // self.my_list[-1-k]
