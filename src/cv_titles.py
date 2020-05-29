import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#SET FONT FOR TITLES
path = '../font/Sunday Best.ttf'
prop = FontProperties(fname=path)
prop.set_weight = 'regular'

def title_right(pos, title_name):
    pos -= 0.05
    plt.text(.69, pos, title_name, fontproperties=prop, size = 12, color='#1d9393')
    pos -= 0.04
    return pos

def title_left(pos, title_name):
    plt.text(.25, pos, title_name, fontproperties=prop, size = 12, color='#1d9393')
    pos -= 0.05
    return pos

def subtitle(pos, title_name):
    plt.text(.69, pos, title_name, weight='bold', fontsize=12)
    pos -= 0.025
    return pos