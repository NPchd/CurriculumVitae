import matplotlib.pyplot as plt
import json
from math import *

from cv_image import *

def add_formation(pos):
    formations_file = open('../data/formations.json', encoding='utf-8')
    formations_dict = json.load(formations_file)
    formations_file.close()
    for formation in formations_dict:
        plt.text(.2, pos, formation["school"], ha='right', weight='bold', fontsize=10)
        plt.text(.25, pos, formation["formation"], weight='regular', fontsize=9, wrap=True)
        plt.text(.2, pos - 0.02, formation["date"], ha='right', fontsize=8)
        plt.text(.25, pos - 0.02, formation["description"], color='#747474', weight='regular', fontsize=7)
        plt.text(.25, pos - 0.0325, formation["description2"], color='#747474', weight='regular', fontsize=7)
        plt.text(.25, pos - 0.045, formation["description3"], color='#747474', weight='regular', fontsize=7)
        if (formation["description2"] == ""):
            pos -= 0.05
        elif (formation["description3"] == ""):
            pos -= 0.06
        else:
            pos -= 0.07
    return pos

def add_experience(pos):
    experiences_file = open('../data/experiences.json', encoding='utf-8')
    experiences_dict = json.load(experiences_file)
    experiences_file.close()
    for experience in experiences_dict:
        plt.text(.2, pos, experience["position"], ha='right', weight='bold', fontsize=10, wrap=True)
        plt.text(.25, pos, experience["company"] + " - " + experience["localisation"], weight='regular', fontsize=9, wrap=True)
        plt.text(.2, pos - 0.02, experience["date"], ha='right', fontsize=8)
        plt.text(.25, pos - 0.02, experience["description"], weight='regular', fontsize=7, color='#747474', wrap=True)
        plt.text(.25, pos - 0.0325, experience["description2"], color='#747474', weight='regular', fontsize=7)
        plt.text(.25, pos - 0.045, experience["description3"], color='#747474', weight='regular', fontsize=7)
        if (experience["description2"] == ""):
            pos -= 0.05
        elif (experience["description3"] == ""):
            pos -= 0.06
        else:
            pos -= 0.07
    return pos

def add_information(pos, ax):
    info_file = open('../data/info.json', encoding='utf-8')
    info_dict = json.load(info_file)
    info_file.close()
    for info in info_dict:
        plt.text(.74, pos, info_dict[info], fontsize=11)
        logo(pos, info, ax)
        pos -= 0.035
    return pos

def add_skill_multi(pos, skill_type):
    skills_file = open('../data/skills.json', encoding='utf-8')
    skills_dict = json.load(skills_file)
    skills_file.close()
    index = 0
    for skill in skills_dict[skill_type]:
        if index < ceil(len(skills_dict[skill_type])/2):
            plt.text(.69, pos, skill["name"], fontsize=10)
        else:
            plt.text(.84, pos + 0.02*ceil(len(skills_dict[skill_type])/2), skill["name"], fontsize=10)
        pos -= 0.02
        index += 1
    pos += (index - 1) * 0.02 - 0.02*ceil(len(skills_dict[skill_type])/2)
    return pos

def add_skill_single(pos, skill_type):
    skills_file = open('../data/skills.json', encoding='utf-8')
    skills_dict = json.load(skills_file)
    skills_file.close()
    for skill in skills_dict[skill_type]:
        plt.text(.69, pos, skill["name"] + " " + skill["description"], fontsize=10)
        pos -= 0.02
    return pos

def add_link(pos, skills_dict, ax):
    skills_file = open('../data/skills.json', encoding='utf-8')
    skills_dict = json.load(skills_file)
    skills_file.close()
    for skill in skills_dict['links']:
        plt.text(.74, pos, skill["name"], fontsize=10, wrap=True)
        logo(pos, skill["type"], ax)
        pos -= 0.035
    return pos