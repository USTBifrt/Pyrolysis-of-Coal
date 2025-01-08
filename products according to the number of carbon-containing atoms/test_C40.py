import pandas as pd
import re
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_excel("CC1_heat3000.xlsx")
# print(data)
# print(df)
Time_list = []
count40_list = []
count14_list = []
count5_list = []
count1_list = []
count1_40_list = []
count1_14_list = []
count1_5_list = []
count1_1_list = []
count2_40_list = []
count2_14_list = []
count2_5_list = []
count2_1_list = []
for i in range(0,data.shape[0],2):
    Time = float(data.iloc[i + 1].iloc[0]) * 0.2 / 1000
    count40 = 0
    count14 = 0
    count5 = 0
    count1 = 0
    count1_40 = 0
    count1_14 = 0
    count1_5 = 0
    count1_1 = 0
    count2_40 = 0
    count2_14 = 0
    count2_5 = 0
    count2_1 = 0
    formula_list = data.iloc[i]
    for j in range(3,data.shape[1]):
        formula = formula_list.iloc[j]
        if str(formula) != "nan":
            ff_str = re.findall("(C[a-z])(\d*)",str(formula))
            #print(ff_str)
            f_num_list=[]
            f_dic={
                'Cc':0,
                'Cn':0
            }
            for f_str in ff_str:
                #print(f_str)
                f_ele = f_str[0]
                #print(f_ele)
                f_num = f_str[1]
                #print(f_num)
                if f_num =="":
                    f_num = 1
                else:
                    f_num=int(f_num)
                #print(f_num)
                f_dic[f_ele]+=f_num
                f_num_list.append(f_num)
            #print(f_dic)
            num =sum(f_num_list)
            #print(num)
            if int(num) > 40:
                count40 += int(num) * data.iloc[i+1].iloc[j]
                count1_40+=int(f_dic['Cc']) * data.iloc[i+1].iloc[j]
                count2_40+=int(f_dic['Cn']) * data.iloc[i + 1].iloc[j]
            elif int(num) >= 14:
                count14 += int(num) * data.iloc[i + 1].iloc[j]
                count1_14 += int(f_dic['Cc']) * data.iloc[i + 1].iloc[j]
                count2_14 += int(f_dic['Cn']) * data.iloc[i + 1].iloc[j]
            elif int(num) >= 5:
                count5 += int(num) * data.iloc[i + 1].iloc[j]
                count1_5 += int(f_dic['Cc']) * data.iloc[i + 1].iloc[j]
                count2_5 += int(f_dic['Cn']) * data.iloc[i + 1].iloc[j]
            else:
                count1 += int(num) * data.iloc[i + 1].iloc[j]
                count1_1 += int(f_dic['Cc']) * data.iloc[i + 1].iloc[j]
                count2_1 += int(f_dic['Cn']) * data.iloc[i + 1].iloc[j]
    Time_list.append(Time)
    count40_list.append(count40)
    count14_list.append(count14)
    count5_list.append(count5)
    count1_list.append(count1)
    count1_40_list.append(count1_40)
    count1_14_list.append(count1_14)
    count1_5_list.append(count1_5)
    count1_1_list.append(count1_1)
    count2_40_list.append(count2_40)
    count2_14_list.append(count2_14)
    count2_5_list.append(count2_5)
    count2_1_list.append(count2_1)
df_out = pd.DataFrame()
df_out['Time']= Time_list
df_out['C40+']= count40_list
df_out['C14-40']= count14_list
df_out['C5-13']= count5_list
df_out['C1-4']= count1_list
df_out['Cc_C40+']= count1_40_list
df_out['Cc_C14-40']= count1_14_list
df_out['Cc_C5-13']= count1_5_list
df_out['Cc_C1-4']= count1_1_list
df_out['Cn_C40+']= count2_40_list
df_out['Cn_C14-40']= count2_14_list
df_out['Cn_C5-13']= count2_5_list
df_out['Cn_C1-4']= count2_1_list
df_out.to_excel("CNumber_CC1_heat3000fragments.xlsx",index=False)
