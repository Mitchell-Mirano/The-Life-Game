
class Cell():
    def __init__(self,position_x:int,position_y:int,state:int):
        self.position_x = position_x
        self.position_y = position_y
        self.state = state

    def __str__(self):
        if self.state==1:
            return f"Living in ({self.position_x},{self.position_y})"

        if self.state==0:
            return f"Dead in ({self.position_x},{self.position_y})"