
class prediction:
    def __init__(self,sepal_l,sepal_w,petal_l,petal_w):
        self.sepal_length=sepal_l
        self.sepal_width=sepal_w
        self.petal_length=petal_l
        self.petal_width=petal_w
    
    def get_petal_length(self):
        return self.petal_length
    def get_petal_width(self):
        return self.petal_width
    def get_sepal_length(self):
        return self.sepal_length
    def get_sepal_width(self):
        return self.sepal_width
    
    def set_petal_length(self, set_petal_length):
        self.petal_length=set_petal_length
    
    def set_petal_width(self, set_petal_width):
        self.petal_width=set_petal_width

    def set_sepal_length(self, set_sepal_length):
        self.sepal_length=set_sepal_length

    def set_sepal_width(self, set_sepal_width):
        self.sepal_width=set_sepal_width
    

