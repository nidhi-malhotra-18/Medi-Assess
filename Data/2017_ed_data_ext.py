# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:16:57 2020

@author: Nidhi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:06:04 2020

@author: Nidhi
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 12:48:10 2020

@author: Nidhi
"""

import pandas as pd

df = pd.read_csv('data5.txt')

data = df.iloc[:,0]
age = []
sex = []
temp = []
hr = []
rr = []
sbp = []
dbp = []
po = []
#oxygen = []
pain = []
result = []
outcome = []
discharge = []
arrival = []
#length = []
reason1 = []
reason2 = []
reason3 = []
r1 = []
r2 = []
r3 = []
a=[[],[],[]]
b=[[],[],[]]
esi = []

#additional fields
cancer = []
cebvd = []
copd = []
# edidal = []
chf = []
dementia = []
diabetes = []
mihx = []
totchron = []
dvt = []
hiv = []
nonchron = []
df = pd.read_csv('reasons.csv')
# print((df[df['Code']==59160]['Reason'].values[0]))
print(type((df['Code']==59160)))
# print(((df['Code']==65000)))
print((df[df['Code']==90000]).shape)




for i in range(0,len(data)):
    for k in range(0,3):
         j=72+5*k
         number = int(data[i][j:j+5])
        # print(number)
        # reason1.append
        # print(df[df['Code']==number]['Reason'].values[0])
         if df[(df['Code']==number)].shape[0] == 0:
            print(number)
            print("Blannnk")
            b[k].append("Blank")
         else:
            print(number)
            b[k].append(df[df['Code']==number]['Reason'].values[0])
         if (int(data[i][j:j+5]) <= 10999 and int(data[i][j:j+5]) >= 10010):
             a[k].append(1)
         if (int(data[i][j:j+5]) <= 11999 and int(data[i][j:j+5]) >= 11000):
             a[k].append(2)
         if (int(data[i][j:j+5]) <= 12599 and int(data[i][j:j+5]) >= 12000):
             a[k].append(3)
         if (int(data[i][j:j+5]) <= 12999 and int(data[i][j:j+5]) >= 12600):
             a[k].append(4)
         if (int(data[i][j:j+5]) <= 13999 and int(data[i][j:j+5]) >= 13000):
             a[k].append(5)
         if (int(data[i][j:j+5]) <= 14999 and int(data[i][j:j+5]) >= 14000):
             a[k].append(6)
         if (int(data[i][j:j+5]) <= 16399 and int(data[i][j:j+5]) >= 15000):
             a[k].append(7)
         if (int(data[i][j:j+5]) <= 18299 and int(data[i][j:j+5]) >= 16400):
             a[k].append(8)
         if (int(data[i][j:j+5]) <= 18999 and int(data[i][j:j+5]) >= 18300):
             a[k].append(9)
         if (int(data[i][j:j+5]) <= 19999 and int(data[i][j:j+5]) >= 19000):
             a[k].append(10)
         if (int(data[i][j:j+5]) <= 20999 and int(data[i][j:j+5]) >= 20010):
             a[k].append(11)
         if (int(data[i][j:j+5]) <= 21999 and int(data[i][j:j+5]) >= 21000):
             a[k].append(12)
         if (int(data[i][j:j+5]) <= 22499 and int(data[i][j:j+5]) >= 22000):
             a[k].append(13)
         if (int(data[i][j:j+5]) <= 22999 and int(data[i][j:j+5]) >= 22500):
             a[k].append(14)
         if (int(data[i][j:j+5]) <= 23499 and int(data[i][j:j+5]) >= 23000):
             a[k].append(15)
         if (int(data[i][j:j+5]) <= 23999 and int(data[i][j:j+5]) >= 23500):
             a[k].append(16)
         if (int(data[i][j:j+5]) <= 24499 and int(data[i][j:j+5]) >= 24000):
             a[k].append(17)
         if (int(data[i][j:j+5]) <= 24999 and int(data[i][j:j+5]) >= 24500):
             a[k].append(18)
         if (int(data[i][j:j+5]) <= 25999 and int(data[i][j:j+5]) >= 25000):
             a[k].append(19)
         if (int(data[i][j:j+5]) <= 26499 and int(data[i][j:j+5]) >= 26000):
             a[k].append(20)
         if (int(data[i][j:j+5]) <= 26999 and int(data[i][j:j+5]) >= 26500):
             a[k].append(21)
         if (int(data[i][j:j+5]) <= 27999 and int(data[i][j:j+5]) >= 27000):
             a[k].append(22)
         if (int(data[i][j:j+5]) <= 28999 and int(data[i][j:j+5]) >= 28000):
             a[k].append(23)
         if (int(data[i][j:j+5]) <= 29499 and int(data[i][j:j+5]) >= 29000):
             a[k].append(24)
         if (int(data[i][j:j+5]) <= 29799 and int(data[i][j:j+5]) >= 29500):
             a[k].append(25)
         if (int(data[i][j:j+5]) <= 29999 and int(data[i][j:j+5]) >= 29800):
             a[k].append(26)
         if (int(data[i][j:j+5]) <= 31999 and int(data[i][j:j+5]) >= 31000):
             a[k].append(27)
         if (int(data[i][j:j+5]) <= 32999 and int(data[i][j:j+5]) >= 32000):
             a[k].append(28)
         if (int(data[i][j:j+5]) <= 33999 and int(data[i][j:j+5]) >= 33000):
             a[k].append(29)
         if (int(data[i][j:j+5]) <= 34999 and int(data[i][j:j+5]) >= 34000):
             a[k].append(30)
         if (int(data[i][j:j+5]) <= 35999 and int(data[i][j:j+5]) >= 35000):
             a[k].append(31)
         if (int(data[i][j:j+5]) <= 41999 and int(data[i][j:j+5]) >= 41000):
             a[k].append(32)
         if (int(data[i][j:j+5]) <= 42999 and int(data[i][j:j+5]) >= 42000):
             a[k].append(33)
         if (int(data[i][j:j+5]) <= 44999 and int(data[i][j:j+5]) >= 44000):
             a[k].append(34)
         if (int(data[i][j:j+5]) <= 45999 and int(data[i][j:j+5]) >= 45000):
             a[k].append(35)
         if (int(data[i][j:j+5]) <= 46999 and int(data[i][j:j+5]) >= 46000):
             a[k].append(36)
         if (int(data[i][j:j+5]) <= 47999 and int(data[i][j:j+5]) >= 47000):
             a[k].append(37)
         if (int(data[i][j:j+5]) <= 48999 and int(data[i][j:j+5]) >= 48000):
             a[k].append(38)
         if (int(data[i][j:j+5]) <= 57999 and int(data[i][j:j+5]) >= 50010):
             a[k].append(39)
         if (int(data[i][j:j+5]) <= 58999 and int(data[i][j:j+5]) >= 58000):
             a[k].append(40)
         if (int(data[i][j:j+5]) <= 59999 and int(data[i][j:j+5]) >= 59000):
             a[k].append(41)
         if (int(data[i][j:j+5]) <= 67009 and int(data[i][j:j+5]) >= 61000):
             a[k].append(42)
         if (int(data[i][j:j+5]) <= 71409 and int(data[i][j:j+5]) >= 71000):
             a[k].append(43)
         if (int(data[i][j:j+5]) <= 89999 and int(data[i][j:j+5]) >= 89900):
             a[k].append(44)
         if (int(data[i][j:j+5]) == -9):
             a[k].append(0)


for i in range(0,len(data)):
    age_data = int(data[i][15:18])
    sex_data = int(data[i][24])
    temp_data = float(data[i][47:51])
    hr_data = float(data[i][51:54])
    rr_data = float(data[i][54:57])
    sbp_data = float(data[i][57:60])
    dbp_data = float(data[i][60:63])
    po_data = float(data[i][63:66])
    #oxygen_data = 0
    pain_data = int(data[i][68:70])
    result_data = int(data[i][66:68])
    death_in_ed = int(data[i][492])
    icu_data = int(data[i][500:502])
    hospital_discharge_status = int(data[i][526:528])
    arrival_ambulance = int(data[i][32:34])
    #length_of_visit = 0
    obs_unit_discharge = int(data[i][498])
    esi_data = int(data[i][66:68])

    #new features 
    # cancer_data = int(data[i][154])
    # cebvd_data = int(data[i][155])
    # copd_data = int(data[i][157])
    # edidal_data = int(data[i][173])
    # chf_data = int(data[i][158])
    # if int(data[i][161])==1 or int(data[i][162])==1 or int(data[i][163]) ==1:
        # diabetes_data = 1
    # else:
        # diabetes_data = 0
    # diabetes_data = int(data[i][176])
    # mihx_data = int(data[i][159])
    # hiv_data = int(data[i][166])
    # nochron_data = int(data[i][180]) #filtering out null values subsequently, it takes value's 0(no), 1(yes), 2(null)
    # totchron_data = int(data[i][174:176]) #filter out -9 values      
    


    if death_in_ed == 1:
        if True:
        # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
            age.append(age_data)
            sex.append(sex_data)
            temp.append(float(temp_data/10))
            hr.append(hr_data)
            rr.append(rr_data)
            sbp.append(sbp_data)
            dbp.append(dbp_data)
            po.append(po_data)
            # oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(b[0][i])
            reason2.append(b[1][i])
            reason3.append(b[2][i])
            r1.append(a[0][i])
            r2.append(a[1][i])
            r3.append(a[2][i])
            outcome.append(1)
            esi.append(esi_data)

            # cancer.append(cancer_data)
            # cebvd.append(cebvd_data)
            # copd.append(copd_data)
            # edidal.append(edidal_data)
            # chf.append(chf_data)
            # dementia.append(dementia_data)
            # diabetes.append(diabetes_data)
            # mihx.append(mihx_data)
            # dvt.append(dvt_data)
            # totchron.append(totchron_data)
            # dvt.append(dvt_data)
            # hiv.append(hiv_data)

    if death_in_ed==0 and (icu_data == 1):
        if True:
        # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
            age.append(age_data)
            sex.append(sex_data)
            temp.append(float(temp_data/10))
            hr.append(hr_data)
            rr.append(rr_data)
            sbp.append(sbp_data)
            dbp.append(dbp_data)
            po.append(po_data)
            # oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(b[0][i])
            reason2.append(b[1][i])
            reason3.append(b[2][i])
            r1.append(a[0][i])
            r2.append(a[1][i])
            r3.append(a[2][i])
            outcome.append(2)
            esi.append(esi_data)
    if death_in_ed==0 and (icu_data == 2):
        if True:
        # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
            age.append(age_data)
            sex.append(sex_data)
            temp.append(float(temp_data/10))
            hr.append(hr_data)
            rr.append(rr_data)
            sbp.append(sbp_data)
            dbp.append(dbp_data)
            po.append(po_data)
            # oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(b[0][i])
            reason2.append(b[1][i])
            reason3.append(b[2][i])
            r1.append(a[0][i])
            r2.append(a[1][i])
            r3.append(a[2][i])
            outcome.append(3)
            esi.append(esi_data)
            # cancer.append(cancer_data)
            # cebvd.append(cebvd_data)
            # copd.append(copd_data)
            # edidal.append(edidal_data)
            # chf.append(chf_data)
            # dementia.append(dementia_data)
            # diabetes.append(diabetes_data)
            # mihx.append(mihx_data)
            # dvt.append(dvt_data)
            # totchron.append(totchron_data)
            # dvt.append(dvt_data)
            # hiv.append(hiv_data)
    if death_in_ed == 0 and icu_data == 6:
        if True:
        # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
            age.append(age_data)
            sex.append(sex_data)
            temp.append(float(temp_data/10))
            hr.append(hr_data)
            rr.append(rr_data)
            sbp.append(sbp_data)
            dbp.append(dbp_data)
            po.append(po_data)
            # oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(b[0][i])
            reason2.append(b[1][i])
            reason3.append(b[2][i])
            r1.append(a[0][i])
            r2.append(a[1][i])
            r3.append(a[2][i])
            outcome.append(4)
            esi.append(esi_data)
 
    if obs_unit_discharge==1:
        if True:
        # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
            age.append(age_data)
            sex.append(sex_data)
            temp.append(float(temp_data/10))
            hr.append(hr_data)
            rr.append(rr_data)
            sbp.append(sbp_data)
            dbp.append(dbp_data)
            po.append(po_data)
            # oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(b[0][i])
            reason2.append(b[1][i])
            reason3.append(b[2][i])
            r1.append(a[0][i])
            r2.append(a[1][i])
            r3.append(a[2][i])
            outcome.append(5)
            esi.append(esi_data)
    # if death_in_ed == 0 and (icu_data == 3 or icu_data == 4 or icu_data == 5 or icu_data == 6):
    #     if True:
    #     # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
    #         age.append(age_data)
    #         sex.append(sex_data)
    #         temp.append(float(temp_data/10))
    #         hr.append(hr_data)
    #         rr.append(rr_data)
    #         sbp.append(sbp_data)
    #         dbp.append(dbp_data)
    #         po.append(po_data)
    #         # oxygen.append(oxygen_data)
    #         pain.append(pain_data)
    #         arrival.append(arrival_ambulance)
    #         # length.append(length_of_visit)
    #         reason1.append(a[0][i])
    #         reason2.append(a[1][i])
    #         reason3.append(a[2][i])
    #         outcome.append(3)
    #         esi.append(esi_data)
            # cancer.append(cancer_data)
            # cebvd.append(cebvd_data)
            # copd.append(copd_data)
            # # edidal.append(edidal_data)
            # chf.append(chf_data)
            # # dementia.append(dementia_data)
            # diabetes.append(diabetes_data)
            # mihx.append(mihx_data)
            # # dvt.append(dvt_data)
            # totchron.append(totchron_data)
            # # dvt.append(dvt_data)
            # hiv.append(hiv_data)
            
    # if obs_unit_discharge==1:
    #     if True:
    #     # if temp_data!=-9 and hr_data!=-9 and rr_data!=-9 and sbp_data!=-9 and dbp_data!=-9 and po_data!=-9 and pain_data!=-9 and pain_data!=-8:
    #         age.append(age_data)
    #         sex.append(sex_data)
    #         temp.append(float(temp_data/10))
    #         hr.append(hr_data)
    #         rr.append(rr_data)
    #         sbp.append(sbp_data)
    #         dbp.append(dbp_data)
    #         po.append(po_data)
    #         # oxygen.append(oxygen_data)
    #         pain.append(pain_data)
    #         arrival.append(arrival_ambulance)
    #         # length.append(length_of_visit)
    #         reason1.append(a[0][i])
    #         reason2.append(a[1][i])
    #         reason3.append(a[2][i])
    #         outcome.append(4)
    #         esi.append(esi_data)
            # cancer.append(cancer_data)
            # cebvd.append(cebvd_data)
            # copd.append(copd_data)
            # # edidal.append(edidal_data)
            # chf.append(chf_data)
            # # dementia.append(dementia_data)
            # diabetes.append(diabetes_data)
            # mihx.append(mihx_data)
            # # dvt.append(dvt_data)
            # totchron.append(totchron_data)
            # # dvt.append(dvt_data)
            # hiv.append(hiv_data)






print(len(outcome))
# print(len(oxygen))
print(len(temp))
print(len(hr))
# print(len(cancer))
# print(len(cebvd))
# print(len(copd))
# # print(len(edidal))
# print(len(chf))
# print(len(rr))
print(len(age))
print(len(sex))
print(len(sbp))
print(len(dbp))
print(len(po))
print(len(pain))
print(len(arrival))
# print(len(length))
print(len(reason1))
print(len(reason2))
print(len(reason3))
# print(len(diabetes))
# # print(len(dementia))
# print(len(diabetes))
# print(len(mihx))
# print(len(totchron))
# print(len(outcome))
# print(len(mihx))
# print(len(totchron))
# # print(len(dvt))
# print(len(hiv))
data_final = {
    'Age' : age,
    'Sex' : sex,
    'Temperature' : temp,
    'Heart Rate' : hr,
    'Resp Rate' : rr,
    'Systolic BP' : sbp,
    'Diastolic BP' : dbp,
    'Pulse Oximetry' : po,
    'Pain' : pain,
    'Arrival' : arrival,
    'Result' : outcome,
    'Reason1':reason1,
    'Reason2':reason2,
    'Reason3':reason3,
    'R1':r1,
    'R2':r2,
    'R3':r3,
    'esi':esi
    # 'Cancer':cancer,
    # 'Cebvd':cebvd,
    # 'Copd':copd,
    # # 'Eddial':edidal,
    # 'CHF':chf,
    # 'Diabetes':diabetes,
    # 'MIHX':mihx,
    # 'Totchron':totchron,
    # 'hiv':hiv

}

df_final = pd.DataFrame(data_final, columns = ['Age','Sex','Temperature','Heart Rate','Resp Rate' ,
    'Systolic BP','Diastolic BP','Pulse Oximetry','Pain','Arrival','Result','Reason1','Reason2','Reason3','R1','R2','R3','esi'])

df_final.to_csv('data_2017_reasons.csv')

