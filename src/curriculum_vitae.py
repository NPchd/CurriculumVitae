import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import json

from cv_titles import *
from cv_parts import *
from cv_image import *

def separator(pos):
    plt.axhline(y=pos_right, xmin=0, xmax=1, color='#ffffff', linewidth=3)

def header():
    person_file = open('../data/person.json', encoding='utf-8')
    person_dict = json.load(person_file)
    person_file.close()
    #PERSON
    plt.text(.27, .94, person_dict["name"], weight='regular', fontproperties=prop, size = 18)
    plt.text(.28, .89, person_dict["status"], fontproperties=prop, size=14, color = "#f89870")
    plt.text(.27, .83, person_dict["intro"], weight='regular', fontsize=8)
    #PHOTO
    photo('photo', ax)

#------------------INITIALISATION------------------#
pos_right = 1
pos_left = 0.75

#CREATE PLOT AND RIGHT COLUMN
fig, ax = plt.subplots(figsize=(8.3, 11.7))
plt.axvline(x=.99, color='#f89870', linewidth=300, alpha=0.8)
plt.axis('off')

#SET FONT FOR THE DOCUMENT
plt.rcParams['font.family'] = 'Helvetica'
#SET FONT FOR TITLES
path = '../font/Sunday Best.ttf'
prop = FontProperties(fname=path)
prop.set_weight = 'regular'

#------------------LEFT PART------------------#
header()

#FORMATIONS
pos_left = title_left(pos_left, "FORMATION")
pos_left = add_formation(pos_left)

pos_left -=0.02

#EXPERIENCES
pos_left = title_left(pos_left, "EXPERIENCE")
pos_left = add_experience(pos_left)

#------------------RIGHT PART------------------#
#INFORMATIONS
pos_right = title_right(pos_right, "INFORMATIONS")
pos_right = add_information(pos_right, ax)

#SEPARATOR
separator(pos_right)

#SKILLS
pos_right = title_right(pos_right, "SKILLS")
pos_right = subtitle(pos_right, "TECHNICAL")
pos_right = add_skill_multi(pos_right, 'technical_languages')

#LOGICIELS
pos_right = subtitle(pos_right, "SOFTWARE")
pos_right = add_skill_multi(pos_right, 'softwares')

#LANGUES
pos_right = subtitle(pos_right, "LANGUAGE")
pos_right = add_skill_single(pos_right, 'languages')

#LIENS UTILES
pos_right -= 0.015
pos_right = add_link(pos_right, 'links', ax)

#SEPARATOR
separator(pos_right)

#CENTRES D'INTERET
pos_right = title_right(pos_right, "HOBBIES")
pos_right = add_skill_single(pos_right, 'hobbies')

#------------------END------------------#

#ADD FOOTER LINK TO GITHUB DEPOSIT
plt.text(.65, .01, "> CV généré: https://github.com/NPchd/CurriculumVitae", ha='right', weight='regular', fontsize=8, color="#989898")

#SAVE FILE AS PDF
fig.savefig('../cv_2020.pdf', dpi=600, bbox_inches='tight')