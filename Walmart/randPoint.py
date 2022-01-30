def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x,self.y = x_center,y_center

    def randPoint(self) -> List[float]:
        theta = uniform(0,2*pi)
        R = self.r*sqrt(uniform(0,1))
        return [self.x + R*cos(theta), self.y + R*sin(theta)]
