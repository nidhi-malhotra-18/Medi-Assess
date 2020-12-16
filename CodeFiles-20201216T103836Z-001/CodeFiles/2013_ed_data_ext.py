import pandas as pd

df = pd.read_csv('data1.txt')

data = df.iloc[:,0]
age = []
sex = []
temp = []
hr = []
rr = []
sbp = []
dbp = []
po = []
oxygen = []
pain = []
result = []
outcome = []
discharge = []
arrival = []
length = []
reason1 = []
reason2 = []
reason3 = []
a=[[],[],[]]




#additional fields
cancer = []
cebvd = []
copd = []
edidal = []
chf = []
dementia = []
diabetes = []
mihx = []
totchron = []
dvt = []
hiv = []
nonchron = []
df = pd.read_csv('../reasons.csv')
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
            a[k].append("Blank")
        else:
            print(number)
            a[k].append(df[df['Code']==number]['Reason'].values[0])
        # if (int(data[i][j:j+5]) <= 10999 and int(data[i][j:j+5]) >= 10010):
        #     a[k].append(1)
        # if (int(data[i][j:j+5]) <= 11999 and int(data[i][j:j+5]) >= 11000):
        #     a[k].append(2)
        # if (int(data[i][j:j+5]) <= 12599 and int(data[i][j:j+5]) >= 12000):
        #     a[k].append(3)
        # if (int(data[i][j:j+5]) <= 12999 and int(data[i][j:j+5]) >= 12600):
        #     a[k].append(4)
        # if (int(data[i][j:j+5]) <= 13999 and int(data[i][j:j+5]) >= 13000):
        #     a[k].append(5)
        # if (int(data[i][j:j+5]) <= 14999 and int(data[i][j:j+5]) >= 14000):
        #     a[k].append(6)
        # if (int(data[i][j:j+5]) <= 16399 and int(data[i][j:j+5]) >= 15000):
        #     a[k].append(7)
        # if (int(data[i][j:j+5]) <= 18299 and int(data[i][j:j+5]) >= 16400):
        #     a[k].append(8)
        # if (int(data[i][j:j+5]) <= 18999 and int(data[i][j:j+5]) >= 18300):
        #     a[k].append(9)
        # if (int(data[i][j:j+5]) <= 19999 and int(data[i][j:j+5]) >= 19000):
        #     a[k].append(10)
        # if (int(data[i][j:j+5]) <= 20999 and int(data[i][j:j+5]) >= 20010):
        #     a[k].append(11)
        # if (int(data[i][j:j+5]) <= 21999 and int(data[i][j:j+5]) >= 21000):
        #     a[k].append(12)
        # if (int(data[i][j:j+5]) <= 22499 and int(data[i][j:j+5]) >= 22000):
        #     a[k].append(13)
        # if (int(data[i][j:j+5]) <= 22999 and int(data[i][j:j+5]) >= 22500):
        #     a[k].append(14)
        # if (int(data[i][j:j+5]) <= 23499 and int(data[i][j:j+5]) >= 23000):
        #     a[k].append(15)
        # if (int(data[i][j:j+5]) <= 23999 and int(data[i][j:j+5]) >= 23500):
        #     a[k].append(16)
        # if (int(data[i][j:j+5]) <= 24499 and int(data[i][j:j+5]) >= 24000):
        #     a[k].append(17)
        # if (int(data[i][j:j+5]) <= 24999 and int(data[i][j:j+5]) >= 24500):
        #     a[k].append(18)
        # if (int(data[i][j:j+5]) <= 25999 and int(data[i][j:j+5]) >= 25000):
        #     a[k].append(19)
        # if (int(data[i][j:j+5]) <= 26499 and int(data[i][j:j+5]) >= 26000):
        #     a[k].append(20)
        # if (int(data[i][j:j+5]) <= 26999 and int(data[i][j:j+5]) >= 26500):
        #     a[k].append(21)
        # if (int(data[i][j:j+5]) <= 27999 and int(data[i][j:j+5]) >= 27000):
        #     a[k].append(22)
        # if (int(data[i][j:j+5]) <= 28999 and int(data[i][j:j+5]) >= 28000):
        #     a[k].append(23)
        # if (int(data[i][j:j+5]) <= 29499 and int(data[i][j:j+5]) >= 29000):
        #     a[k].append(24)
        # if (int(data[i][j:j+5]) <= 29799 and int(data[i][j:j+5]) >= 29500):
        #     a[k].append(25)
        # if (int(data[i][j:j+5]) <= 29999 and int(data[i][j:j+5]) >= 29800):
        #     a[k].append(26)
        # if (int(data[i][j:j+5]) <= 31999 and int(data[i][j:j+5]) >= 31000):
        #     a[k].append(27)
        # if (int(data[i][j:j+5]) <= 32999 and int(data[i][j:j+5]) >= 32000):
        #     a[k].append(28)
        # if (int(data[i][j:j+5]) <= 33999 and int(data[i][j:j+5]) >= 33000):
        #     a[k].append(29)
        # if (int(data[i][j:j+5]) <= 34999 and int(data[i][j:j+5]) >= 34000):
        #     a[k].append(30)
        # if (int(data[i][j:j+5]) <= 35999 and int(data[i][j:j+5]) >= 35000):
        #     a[k].append(31)
        # if (int(data[i][j:j+5]) <= 41999 and int(data[i][j:j+5]) >= 41000):
        #     a[k].append(32)
        # if (int(data[i][j:j+5]) <= 42999 and int(data[i][j:j+5]) >= 42000):
        #     a[k].append(33)
        # if (int(data[i][j:j+5]) <= 44999 and int(data[i][j:j+5]) >= 44000):
        #     a[k].append(34)
        # if (int(data[i][j:j+5]) <= 45999 and int(data[i][j:j+5]) >= 45000):
        #     a[k].append(35)
        # if (int(data[i][j:j+5]) <= 46999 and int(data[i][j:j+5]) >= 46000):
        #     a[k].append(36)
        # if (int(data[i][j:j+5]) <= 47999 and int(data[i][j:j+5]) >= 47000):
        #     a[k].append(37)
        # if (int(data[i][j:j+5]) <= 48999 and int(data[i][j:j+5]) >= 48000):
        #     a[k].append(38)
        # if (int(data[i][j:j+5]) <= 57999 and int(data[i][j:j+5]) >= 50010):
        #     a[k].append(39)
        # if (int(data[i][j:j+5]) <= 58999 and int(data[i][j:j+5]) >= 58000):
        #     a[k].append(40)
        # if (int(data[i][j:j+5]) <= 59999 and int(data[i][j:j+5]) >= 59000):
        #     a[k].append(41)
        # if (int(data[i][j:j+5]) <= 67009 and int(data[i][j:j+5]) >= 61000):
        #     a[k].append(42)
        # if (int(data[i][j:j+5]) <= 71409 and int(data[i][j:j+5]) >= 71000):
        #     a[k].append(43)
        # if (int(data[i][j:j+5]) <= 89999 and int(data[i][j:j+5]) >= 89900):
        #     a[k].append(44)
        # if (int(data[i][j:j+5]) == -9):
        #     a[k].append(0)


for i in range(0,len(data)):
    age_data = int(data[i][15:18])
    sex_data = int(data[i][24])
    temp_data = float(data[i][45:49])
    hr_data = float(data[i][49:52])
    rr_data = float(data[i][52:55])
    sbp_data = float(data[i][55:58])
    dbp_data = float(data[i][58:61])
    po_data = float(data[i][61:64])
    oxygen_data = int(data[i][64:66])
    pain_data = int(data[i][68:70])
    result_data = int(data[i][66:68])
    death_in_ed = int(data[i][348])
    icu_data = int(data[i][356:358])
    hospital_discharge_status = int(data[i][401:403])
    arrival_ambulance = int(data[i][32:34])
    length_of_visit = int(data[i][364:368])
    obs_unit_discharge = int(data[i][354])  


    # #new features 
    # cancer_data = int(data[i][170])
    # cebvd_data = int(data[i][171])
    # copd_data = int(data[i][172])
    # edidal_data = int(data[i][173])
    # chf_data = int(data[i][174])
    # diabetes_data = int(data[i][176])
    # mihx_data = int(data[i][177])
    # hiv_data = int(data[i][179])
    # # nochron_data = int(data[i][180]) #filtering out null values subsequently, it takes value's 0(no), 1(yes), 2(null)
    # totchron_data = int(data[i][181:183]) #filter out -9 values

    

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
            oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(a[0][i])
            reason2.append(a[1][i])
            reason3.append(a[2][i])
            outcome.append(1)

    if death_in_ed==0 and (icu_data == 1 or icu_data == 2):
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
            oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(a[0][i])
            reason2.append(a[1][i])
            reason3.append(a[2][i])
            outcome.append(2)

    # if death_in_ed == 0 and (icu_data == 3 or icu_data == 4 or icu_data == 5 or icu_data == 6):
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
            oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(a[0][i])
            reason2.append(a[1][i])
            reason3.append(a[2][i])
            outcome.append(3)
 
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
            oxygen.append(oxygen_data)
            pain.append(pain_data)
            arrival.append(arrival_ambulance)
            # length.append(length_of_visit)
            reason1.append(a[0][i])
            reason2.append(a[1][i])
            reason3.append(a[2][i])
            outcome.append(4)


#length check
print(len(rr))
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

data_final = {
    'Age' : age,
    'Sex' : sex,
    'Temperature' : temp,
    'Heart Rate' : hr,
    'Resp Rate' : rr,
    'Systolic BP' : sbp,
    'Diastolic BP' : dbp,
    'Pulse Oximetry' : po,
    'Oxygen' : oxygen,
    'Pain' : pain,
    'Arrival' : arrival,
    'Result' : outcome,
    'Reason1':reason1,
    'Reason2':reason2,
    'Reason3':reason3,


}

df_final = pd.DataFrame(data_final, columns = ['Age','Sex','Temperature','Heart Rate','Resp Rate' ,
    'Systolic BP','Diastolic BP','Pulse Oximetry','Oxygen','Pain','Arrival','Result','Reason1','Reason2','Reason3'])

df_final.to_csv('data_2013_reasons.csv')


