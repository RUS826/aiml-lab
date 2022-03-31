import numpy as np
import pandas as pd
data = pd.DataFrame(data=pd.read_csv('data.csv'))
print('The Dataset is: \n')
print(data)
concepts = np.array(data)[:,0:-1]
print('\n The Concepts are: \n',concepts)
target = np.array(data)[:,-1]
print('\nThe target is: \n',target)
def learn(concepts, target):
 specific_h = concepts[0].copy()
 general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
 for i, h in enumerate(concepts):
   print("")
   print(specific_h)
   print(general_h)
   if target[i] == "Yes":
     for x in range(len(specific_h)):
       if h[x] != specific_h[x]:
         specific_h[x] = '?'
         general_h[x][x] = '?'
   if target[i] == "No":
     for x in range(len(specific_h)):
       if h[x] != specific_h[x]:
         general_h[x][x] = specific_h[x]
       else:
         general_h[x][x] = '?'
   indices = [i for i,val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
 for i in indices:
    general_h.remove(['?', '?', '?', '?', '?', '?'])
 return specific_h, general_h
 s_final, g_final = learn(concepts, target)
print("\n\nFinal S:", s_final)
print("\n\nFinal G:", g_final)
