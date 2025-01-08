import os, sys
os.environ['OVITO_GUI_MODE'] = '1' # Request a session with OpenGL support

import math
import pandas as pd
import ovito
from ovito.io import import_file
from ovito.vis import Viewport, TachyonRenderer, OpenGLRenderer, TextLabelOverlay
from ovito.modifiers import CreateBondsModifier, TimeAveragingModifier
from ovito.qt_compat import QtCore

#bond length (approximate)
C_C = 1.6
C_H = 1.2
C_O = 1.5


# Import simulation dataset and add it to the scene:

data_list = []
Time_list = []
for a in range(0,1200,10):
    pipeline = import_file("FC2_heat3000.lammpstrj")
    pipeline.add_to_scene()
 # CreateBondsModifier
    mod = CreateBondsModifier()
    mod.mode = CreateBondsModifier.Mode.Pairwise
    pipeline.modifiers.append(mod)
    mod.set_pairwise_cutoff(1, 1, C_C)  # 1号为C，C-C bond length

    pipeline.modifiers.append(TimeAveragingModifier(interval=(a, a+10), operate_on='attribute:CreateBonds.num_bonds'))
    data = pipeline.compute()
    print(data.attributes['CreateBonds.num_bonds (Average)'])
    data_list.append(float(data.attributes['CreateBonds.num_bonds (Average)']))
    Time_list.append((a+1)*0.4)  #a为帧数，根据步长计算时间
    pipeline.remove_from_scene()
df_out = pd.DataFrame()
df_out['Time']= Time_list
df_out['C-C']= data_list
df_out.to_excel("FC2_heat3000_CCbond.xlsx",index=False)

data_list = []
Time_list = []
for a in range(0,1200,10):
    pipeline = import_file("FC2_heat3000.lammpstrj")
    pipeline.add_to_scene()
 # CreateBondsModifier
    mod = CreateBondsModifier()
    mod.mode = CreateBondsModifier.Mode.Pairwise
    pipeline.modifiers.append(mod)
    mod.set_pairwise_cutoff(1, 2, C_H)  # C-C bond length

    pipeline.modifiers.append(TimeAveragingModifier(interval=(a, a+10), operate_on='attribute:CreateBonds.num_bonds'))
    data = pipeline.compute()
    print(data.attributes['CreateBonds.num_bonds (Average)'])
    data_list.append(float(data.attributes['CreateBonds.num_bonds (Average)']))
    Time_list.append((a+1)*0.4)
    pipeline.remove_from_scene()
df_out = pd.DataFrame()
df_out['Time']= Time_list
df_out['C-H']= data_list
df_out.to_excel("FC2_heat3000_CHbond.xlsx",index=False)

data_list = []
Time_list = []
for a in range(0,1200,10):
    pipeline = import_file("FC2_heat3000.lammpstrj")
    pipeline.add_to_scene()
 # CreateBondsModifier
    mod = CreateBondsModifier()
    mod.mode = CreateBondsModifier.Mode.Pairwise
    pipeline.modifiers.append(mod)
    mod.set_pairwise_cutoff(1, 3, C_O)  # C-C bond length

    pipeline.modifiers.append(TimeAveragingModifier(interval=(a, a+10), operate_on='attribute:CreateBonds.num_bonds'))
    data = pipeline.compute()
    print(data.attributes['CreateBonds.num_bonds (Average)'])
    data_list.append(float(data.attributes['CreateBonds.num_bonds (Average)']))
    Time_list.append((a+1)*0.4)
    pipeline.remove_from_scene()
df_out = pd.DataFrame()
df_out['Time']= Time_list
df_out['C-O']= data_list
df_out.to_excel("FC2_heat3000_CObond.xlsx",index=False)

print("完成FC2_heat3000")


