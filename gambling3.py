import numpy as np
import ROOT as r


import random

h_money = r.TH1D("money", "money", 100, 0, 0)
h_earning = r.TH1D("earning", "earning", 100, 0, 0)
h_total = r.TH1D("total", "total", 100, 0, 0)
c1 = r.TCanvas("", "")

money = 100
earning = 0
step = 0
list = []
total = 0
for j in range(1000):
    money = 100
    earning = 0
    step = 0
    list = []
    for i in range(100000):
        k = random.randint(0, 1) # decide on k once
        #print(k) # print k over and over again
        if (k == 0):
            money = money -1
        else:
            money = money+1
            if (money>100):
                money = money -1
                earning = earning + 1
            #else:
            #    money = money +1
        list.append(k)
        if (money<1):
            #step = i
            print("Step=", i)
            break
    h_money.Fill(money)
    h_earning.Fill(earning)
    total = money + earning
    h_total.Fill(total)
    print(total)
    
#h_money.Draw()
#h_earning.Draw()
h_total.Draw()

c1.Print("h_total")

#print("Step = {}".format(step))    
print("Money in your hand=", money)
print("Reserved earnings=",earning)
