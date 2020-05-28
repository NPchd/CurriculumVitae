import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def logo(pos, image_name, ax):
    pos += 0.005
    image = mpimg.imread(f'image/{image_name}.png')
    imagebox = OffsetImage(image, zoom=0.035)
    ab = AnnotationBbox(imagebox, (0.705, pos), bboxprops=dict(alpha=0))
    ax.add_artist(ab)

def photo(image_name, ax):
    photo = mpimg.imread(f'image/{image_name}.png')
    imagebox = OffsetImage(photo, zoom=0.3)
    ab = AnnotationBbox(imagebox, (0.13, 0.9), bboxprops=dict(alpha=0))
    ax.add_artist(ab)