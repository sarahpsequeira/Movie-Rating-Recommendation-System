from __future__ import division
import math
import copy

#Declare a list to hold the users
Train_Users=list()
Train_Data=list()
Train_IUF = list()

Test_User_ID=0
Test_Info=list()
Test_User=list()

Similarity_Data = list()
Similarity_Data_Tranied = list()

Similarity_Data_IUF = list()
Similarity_Data_Tranied_IUF = list()

Cosine_Value_Data = list()
Cosine_Value_Data_IUF = list()

Cosine_Tester = list()
Cosine_Train = list()

Euc_Similarity_Data = list()
Euc_Similarity_Data_Tranied = list()
Euc_Tester = list()
Euc_Train = list()
Euc_Value_data=list()

Cosine_Predicted_Info=list()
Euc_Predicted_Info=list()

Weighted_lst=list()
Weighted_Avg=list()
Pearson_weighted_avg=list()
Pearson_Predicted_info=list()

Item_based_Trans=list()
Item_based_Avg=list()
Item_based_Sim=list()

Train_Data_Avg=list()
Similar_Movie=list()
Tester_Movie=list()

IUF_Predicted_Info=list()
CaseAmp_Predicted_Info=list()
Item_Predicted_Info=list()
Custom=list()

#Function to calculate Cosine similarity
def Cosine_Similarity(movie):
    #Finding Users having watched the movie
    for user in Train_Data:
        if(user[int(movie)-1]!="0"):
            Similarity_Data.append(user)
    #Find Users with atleast one movie in common
    for user in Similarity_Data:
        Counter = False
        for tester in Test_User:
            if(tester[1]!="0"):
                if(user[int(tester[0])-1]!="0"):
                    Counter=True
                    break
        if Counter == True:
            Similarity_Data_Tranied.append(user)
    #Finding Cosine similarity value
    for user in Similarity_Data_Tranied:
        dot_product=0
        Tester_sq=0
        Train_sq=0
        Cosine_Sim_value=0
        index=0
        temp_list=list()
        for tester in Test_User:
            if(tester[1]!="0" and user[int(tester[0])-1]!="0"):
                Cosine_Tester.append(tester[1])
                Cosine_Train.append(user[int(tester[0])-1])
        #Calculations for Cosine value
        for item in Cosine_Tester:
            dot_product=dot_product+int(Cosine_Tester[index])*int(Cosine_Train[index])
            Tester_sq=Tester_sq + int(Cosine_Tester[index])**2
            Train_sq=Train_sq + int(Cosine_Train[index])**2
            index=index+1
        Cosine_Sim_value=dot_product/(math.sqrt(Tester_sq)* math.sqrt(Train_sq))

        temp_list=user[:]
        temp_list.append(math.fabs(Cosine_Sim_value))
        Cosine_Value_Data.append(temp_list)
        #Deleting old segments
        del Cosine_Tester[:]
        del Cosine_Train[:]
    # Sorting in descending value for top K
    Cosine_Value_Data.sort(key=lambda x: x[1000], reverse=True)
    #Deleting old segments
    del Similarity_Data_Tranied[:]
    del Similarity_Data[:]
    return

#Custom method Eucledean
def Eucledean_distance(movie):
    # Finding Users having watched the movie
    for user in Train_Data:
        if (user[int(movie) - 1] != "0"):
            Euc_Similarity_Data.append(user)
    # Find Users with atleast one movie in common
    for user in Euc_Similarity_Data:
        Counter = False
        for tester in Test_User:
            if (tester[1] != "0"):
                if (user[int(tester[0]) - 1] != "0"):
                    Counter = True
                    break
        if Counter == True:
            Euc_Similarity_Data_Tranied.append(user)
    #Eucledean Similarity
    for user in Euc_Similarity_Data_Tranied:
        temp=list
        Euc_Dist=0
        #Getting Similar Users
        for tester in Test_User:
            if(tester[1]!="0" and user[int(tester[0])-1]!="0"):
                Euc_Tester.append(tester[1])
                Euc_Train.append(user[int(tester[0])-1])
        #Calculation
        for index,unit in enumerate(Euc_Tester):
            Euc_Dist=Euc_Dist+(float(Euc_Tester[index])-float(Euc_Train[index]))**2
        Euc_Dist=math.sqrt(Euc_Dist)
        Euc_Dist=1/(Euc_Dist+1)
        temp=user[:]
        temp.append(Euc_Dist)
        Euc_Value_data.append(temp)
        del Euc_Train[:]
        del Euc_Tester[:]
    # Sorting in descending value for top 10
    Cosine_Value_Data.sort(key=lambda x: x[1000], reverse=True)
    # Deleting old segments
    del Euc_Similarity_Data_Tranied[:]
    del Euc_Similarity_Data[:]
    return

#Calculating IUF
def IUF_calculation():
    Train_IUF_Temp=copy.deepcopy(Train_Data)
    # Calculating the IUF Value
    m = len(Train_IUF_Temp)
    for i in range(0,999):
        mj=0
        for j in range(0,199):
            if(Train_IUF_Temp[j][i]!="0"):
                mj=mj+1
        if(mj!=0):
            IUF=math.log1p(m/mj)
        else:
            IUF=1
        for j in range(0,199):
            Train_IUF_Temp[j][i]=float(Train_IUF_Temp[j][i])*IUF
    #Adding index to locate row
    index = 0
    for user in Train_IUF_Temp:
        temp = list()
        temp=user[:]
        temp.append(index)
        Train_IUF.append(temp)
        index=index+1
    return

#Calulating Transpose and Average
def Transpose():
    Train_Data_Avg=copy.deepcopy(Train_Data)
    for index,user in enumerate(Train_Data_Avg):
        temp=list()
        User_Avg=0
        User_Count=0
        for rating in user:
            if(rating!="0"):
                User_Avg=User_Avg+float(rating)
                User_Count=User_Count+1
        if User_Count==0:
            User_Avg=0
        else:
            User_Avg=(User_Avg/User_Count)
        temp=user[:]
        temp.append(User_Avg)
        Item_based_Avg.append(temp)
    Item_based=list(map(list, zip(*Item_based_Avg)))
    return Item_based

#Function to calculate Cosine similarity
def Cosine_Similarity_IUF(movie):
    #Finding Users having watched the movie
    for user in Train_IUF:
        if(user[int(movie)-1]!="0"):
            Similarity_Data_IUF.append(user)
    #Find Users with atleast one movie in common
    for user in Similarity_Data_IUF:
        Counter = False
        for tester in Test_User:
            if(tester[1]!="0"):
                if(user[int(tester[0])-1]!="0"):
                    Counter=True
                    break
        if Counter == True:
            Similarity_Data_Tranied_IUF.append(user)
    #Finding Cosine similarity value
    for user in Similarity_Data_Tranied_IUF:
        dot_product=0
        Tester_sq=0
        Train_sq=0
        Cosine_Sim_value=0
        index=0
        temp_list=list()
        for tester in Test_User:
            if(tester[1]!="0" and user[int(tester[0])-1]!="0"):
                Cosine_Tester.append(tester[1])
                Cosine_Train.append(user[int(tester[0])-1])
        #Calculations for Cosine value
        for item in Cosine_Tester:
            dot_product=dot_product+int(Cosine_Tester[index])*int(Cosine_Train[index])
            Tester_sq=Tester_sq + int(Cosine_Tester[index])**2
            Train_sq=Train_sq + int(Cosine_Train[index])**2
            index=index+1
        Cosine_Sim_value=dot_product/(math.sqrt(Tester_sq)* math.sqrt(Train_sq))

        temp_list=Train_Data[int(user[1000])]
        temp_list.append(math.fabs(Cosine_Sim_value))
        Cosine_Value_Data_IUF.append(temp_list)
        #Sorting in descending value for top 10
        Cosine_Value_Data_IUF.sort(key=lambda x: x[1000], reverse=True)
        del Cosine_Tester[:]
        del Cosine_Train[:]
    return

#Function to calculate Predicted rating
def Rating_Prediction(movie, Cosine_Value_Data_tmp):
    Cosine_denum=0
    Cosine_num=0
    Cosine_add=0
    #Calculate for top 100 values
    for i in range(0,199):
        if len(Cosine_Value_Data_tmp)==i:
            break
        Cosine_denum=Cosine_denum+float(Cosine_Value_Data_tmp[i][1000])
    for i in range(0,199):
        if len(Cosine_Value_Data_tmp)==i:
            break
        Cosine_num=float(Cosine_Value_Data_tmp[i][1000])* int(Cosine_Value_Data_tmp[i][int(movie)-1])
        Cosine_add=Cosine_add+(Cosine_num/Cosine_denum)
    return Cosine_add

#Wieghted Average for Pearson
def Weighted_Average(movie,Cosine_Value_Data_tmp,p):
    Tester_Avg=0
    Tester_Count=0
    Pearson_avg=0
    Pearson_Prediction = 0
    #Adding top 100 to new list
    for i in range(0,199):
        if len(Cosine_Value_Data_tmp)==i:
            break
        Weighted_lst.append(Cosine_Value_Data_tmp[i])
    #Calculating Average of tester
    for tester in Test_User:
        if tester[1]=="0":
            break
        Tester_Avg=Tester_Avg+int(tester[1])
        Tester_Count=Tester_Count+1
    Tester_Avg=Tester_Avg/Tester_Count
    #Calculating Average of Train
    for user in Weighted_lst:
        temp_list = list()
        Train_Avg=0
        Train_Count=0
        for rating in user:
            if rating!="0":
                Train_Avg=Train_Avg+int(rating)
                Train_Count=Train_Count+1
        Train_Avg=Train_Avg/Train_Count
        temp_list = user[:]
        temp_list.append(Train_Avg)
        Weighted_Avg.append(temp_list)
    #Calculating Weighted Average
    if(len(Weighted_Avg)==0):
        return Tester_Avg
    for user in Weighted_Avg:
        temp_list = list()
        Pearson_denom2=0
        Pearson_num=0
        Pearson_denom1=0
        for tester in Test_User:
            if(tester[1]!="0" and user[int(tester[0])-1]!="0"):
                Pearson_num=Pearson_num+((float(tester[1])-Tester_Avg)*(float(user[int(tester[0])-1])-float(user[1001])))
                Pearson_denom1=Pearson_denom1+((float(tester[1])-Tester_Avg)**2)
                Pearson_denom2=Pearson_denom2+((float(user[int(tester[0])-1])-float(user[1001]))**2)
        Pearson_denom1=math.sqrt(Pearson_denom1)
        Pearson_denom2=math.sqrt(Pearson_denom2)
        if(Pearson_denom1==0):
            return Tester_Avg
        if(Pearson_denom2==0):
            Pearson_denom2=1
        Pearson_avg=Pearson_num/(Pearson_denom1*Pearson_denom2)
        Pearson_avg=Pearson_avg*(math.fabs(Pearson_avg)**(p-1))
        temp_list=user[:]
        temp_list.append(Pearson_avg)
        Pearson_weighted_avg.append(temp_list)

    Final_num=0
    Final_den=0
    # Calculating Rating
    for user in Pearson_weighted_avg:
        Final_num=Final_num+((int(user[int(movie)-1]) - float(user[1001]))*(float(user[1002])))
        Final_den=Final_den+ math.fabs(float(user[1002]))
    if(Final_den==0):
        return Tester_Avg
    Pearson_Prediction=Tester_Avg+(Final_num/Final_den)
    del Weighted_Avg[:]
    del Weighted_lst[:]
    del Pearson_weighted_avg[:]
    return math.fabs(Pearson_Prediction)

#Adjusted Cosine
def Adjusted_based_Cosine(test_movie):
    for tester in Test_User:
        if(tester[1]!="0"):
            temp_list = list()
            temp_list=copy.deepcopy(Item_based_Trans[int(tester[0])-1])
            temp_list.append(tester[1])
            Similar_Movie.append(temp_list)

    Tester_Movie=copy.deepcopy(Item_based_Trans[int(test_movie)-1])
    for movie in Similar_Movie:
        Item_Num = 0
        Item_Denom1 = 0
        Item_Denom2 = 0
        temp = list()
        for index,user_rating in enumerate(movie):
            if(index!=len(movie)-1):
                if (user_rating != "0" and Tester_Movie[index]!="0"):
                    Item_Num =Item_Num+((float(user_rating)-float(Item_based_Trans[1000][index]))*(float(Tester_Movie[index])-float(Item_based_Trans[1000][index])))
                    Item_Denom1=Item_Denom1+(float(user_rating)-float(Item_based_Trans[1000][index]))**2
                    Item_Denom2=Item_Denom2+(float(Tester_Movie[index])-float(Item_based_Trans[1000][index]))**2
        if(Item_Denom1==0):
            Item_sim=0
        elif(Item_Denom2==0):
            return 1
        else:
            Item_sim=(Item_Num/(math.sqrt(Item_Denom1)*math.sqrt(Item_Denom2)))
        temp=movie[:]
        temp.append(math.fabs(Item_sim))
        Item_based_Sim.append(temp)
    del Similar_Movie[:]
    del Tester_Movie[:]
    #Item_based_Sim.sort(key=lambda x: x[201], reverse=True)
    return 0

#Item based prediction
def Item_Rating(case):
    if(case==1):
        return int(Test_User[0][1])
    item_num=0
    item_denom=0
    for i in range(0,999):
        if len(Item_based_Sim)==i:
            break
        item_denom=item_denom+float(Item_based_Sim[i][201])
    if(item_denom==0):
        return int(Test_User[0][1])
    for i in range(0,999):
        if len(Item_based_Sim)==i:
            break
        item_num= item_num+float(Item_based_Sim[i][201])*float(Item_based_Sim[i][200])
    item_num=item_num/item_denom
    return item_num

#Round of Rating
def Round_Rating(rating):
    Tester_Average = 0
    Tester_Count = 0
    # When Predicted value is 0
    if (rating == 0):
        for tester in Test_User:
            if (tester[1] == "0"):
                break
            Tester_Average = Tester_Average + int(tester[1])
            Tester_Count = Tester_Count + 1
        rating = Tester_Average / Tester_Count
    # Rounding off value
    rating = int(round(rating))
    if (rating > 5):
        rating = 5
    if(rating < 0):
        rating = 3
    if (rating == 0):
        rating = 1
    return rating

#Function to Predict
def Predictor():
    #Consine Similarity
    for tester in Test_User:
        if(tester[1]=="0"):
            #Find the Cosine Similarity
            temp_list = list()
            Cosine_Similarity(tester[0])
            #Find the predicted value for each value
            Cosine_add=Rating_Prediction(tester[0],Cosine_Value_Data)
            Cosine_add=Round_Rating(Cosine_add)
            #Appending to output
            temp_list=tester[:]
            temp_list.insert(0,Test_User_ID)
            temp_list[2]=Cosine_add
            Cosine_Predicted_Info.append(temp_list)

            #Pearson method
            temp_list=list()
            Pearson_Prediction=Weighted_Average(tester[0],Cosine_Value_Data,1)
            Pearson_Prediction=Round_Rating(Pearson_Prediction)
            #Appending to Output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = Pearson_Prediction
            Pearson_Predicted_info.append(temp_list)

            #IUF Method
            Cosine_Similarity_IUF(tester[0])
            temp_list = list()
            IUF_Prediction = Weighted_Average(tester[0], Cosine_Value_Data_IUF,1)
            IUF_Prediction=Round_Rating(IUF_Prediction)
            # Appending to Output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = IUF_Prediction
            IUF_Predicted_Info.append(temp_list)

            #Case Amplification method
            temp_list = list()
            CaseAmp_Prediction = Weighted_Average(tester[0], Cosine_Value_Data, 2.5)
            CaseAmp_Prediction=Round_Rating(CaseAmp_Prediction)
            # Appending to Output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = CaseAmp_Prediction
            CaseAmp_Predicted_Info.append(temp_list)

            #Item based Method
            temp_list =list()
            # Adjusted Cosine Similarity
            case=Adjusted_based_Cosine(int(tester[0]))
            # Rating
            Item_add = Item_Rating(case)
            Item_add = Round_Rating(Item_add)
            # Appending to Output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = Item_add
            Item_Predicted_Info.append(temp_list)

            #Eucledean Method
            temp_list = list()
            # Find the Eucledean Similarity
            Eucledean_distance(tester[0])
            # Find the predicted value for each value
            Euc_add = Rating_Prediction(tester[0], Euc_Value_data)
            Euc_add = Round_Rating(Euc_add)
            # Appending to output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = Euc_add
            Euc_Predicted_Info.append(temp_list)

            #Custom
            temp_list=list()
            Custom_add=Euc_add*(5/15)+Cosine_add*(4/15)+IUF_Prediction*(3/15)+Pearson_Prediction*(2/15)+CaseAmp_Prediction*(1/15)
            Custom_add=Round_Rating(Custom_add)
            #Appending to output
            temp_list = tester[:]
            temp_list.insert(0, Test_User_ID)
            temp_list[2] = Custom_add
            Custom.append(temp_list)


        '''else:
            temp_list=tester[:]
            temp_list.insert(0,Test_User_ID)
            Cosine_Predicted_Info.append(temp_list)'''
        #Deleting old values for New segment
        del Cosine_Value_Data[:]
        del Similarity_Data_Tranied[:]
        del Similarity_Data[:]
        del Euc_Value_data[:]
        del Euc_Similarity_Data[:]
        del Euc_Similarity_Data_Tranied[:]
        del Similarity_Data_Tranied_IUF[:]
        del Similarity_Data_IUF[:]
        del Weighted_Avg[:]
        del Weighted_lst[:]
        del Pearson_weighted_avg[:]
        del Train_IUF[:]
        del Similar_Movie[:]
        del Item_based_Sim[:]
    del Test_User[:]
    return

filename="train.txt"
#Opening the file
fh = open(filename)
for line in fh:
    line=line.rstrip()
    Train_Users=line.split()
    Train_Data.append(Train_Users)
IUF_calculation()
Item_based_Trans=Transpose()

#Reading the test5 file
TestFile5="test5.txt"
tf5=open(TestFile5)
for line in tf5:
    line= line.rstrip()
    if(Test_User_ID==0 or Test_User_ID==line.split()[0]):
        Test_User_ID=line.split()[0]
        Test_Info=line.split()[1:]
        Test_User.append(Test_Info)
    else:
        #Call function to predict
        Predictor()
        Test_User_ID=line.split()[0]
        Test_Info=line.split()[1:]
        Test_User.append(Test_Info)
Predictor()


#Writing to a file
thefile = open('Cosine/result5.txt', 'w')
thefile.truncate()
for item in Cosine_Predicted_Info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('Pearson/result5.txt', 'w')
thefile.truncate()
for item in Pearson_Predicted_info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('IUF/result5.txt', 'w')
thefile.truncate()
for item in IUF_Predicted_Info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('Case/result5.txt', 'w')
thefile.truncate()
for item in CaseAmp_Predicted_Info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('EUC/result5.txt', 'w')
thefile.truncate()
for item in Euc_Predicted_Info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('Custom/result5.txt', 'w')
thefile.truncate()
for item in Custom:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )

#Writing to a file
thefile = open('ItemCF/result5.txt', 'w')
thefile.truncate()
for item in Item_Predicted_Info:
    Info=item[0]+" "+item[1]+" "+str(item[2])
    thefile.write("%s\n" %Info )
