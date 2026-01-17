import matplotlib
import matplotlib.pyplot as plt
from flet.matplotlib_chart import MatplotlibChart
import math

is_int = lambda num: isinstance(int(num), int)

def validate(min,max,inter):
    try:
        return is_int(min) and is_int(max) and is_int(inter)
    except:
        return False

def choose_func(func):
    match(func):
        case 'sin':
            return lambda num: math.sin(num)
        case 'cos':
            return lambda num: math.cos(num)
        case 'tan':
            return lambda num: math.tan(num)
    
def calc_func(min, max, inter, func):
    calc_val = choose_func(func)
    x_axis = range(int(min),int(max),int(inter))
    y_axis = [calc_val(y) for y in x_axis]
    return x_axis, y_axis


class Space:
    def __init__(self):
        self.space = None
        self.size = [16.5,6.7]
        self.bg_color = [0.38, 0.38, 0.38, 0.49]
        self.default_plot()

    def default_plot(self):
        fig, axs = plt.subplots()
        axs.set_facecolor(self.bg_color)
        axs.set_xlabel("x")
        axs.set_ylabel("y")
        axs.grid(True)
        
        fig.set_size_inches(self.size[0],self.size[1],forward=True)
        fig.tight_layout()
        self.space = MatplotlibChart(fig, expand=True)
    
    def update_plot(self, x_values, y_values):
        fig, axs = plt.subplots(1, 1)
        axs.plot(x_values,y_values)
        axs.set_facecolor(self.bg_color)
        axs.set_xlabel("x")
        axs.set_ylabel("y")

        fig.set_size_inches(self.size[0],self.size[1],forward=True)
        fig.tight_layout()
        self.space = MatplotlibChart(fig, expand=True)