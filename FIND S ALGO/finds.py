import pandas as pd
df = pd.read_csv('enjoySport.csv')
column_length = df.shape[1]
df.head()

# OUTPUT

# sunny	warm	normal	strong	warm.1	same	yes
# 0	sunny	warm	high	strong	warm	same	yes
# 1	rainy	cold	high	strong	warm	change	no
# 2	sunny	warm	high	strong	cool	change	yes

h=['0']*(column_length-1)
hp=[]
hn=[]

for training_example in df.values:
    if training_example[-1]!='no':
        hp.append(list(training_example))
    else:
        hn.append(list(training_example))

for i in range(len(hp)):
    for j in range(column_length-1):
        if(h[j]=='0'):
            h[j]=hp[i][j]
        if(h[j]!=hp[i][j]):
            h[j]='?'
        else:
            h[j]=hp[i][j]

print(f'positive hpo:\n{hp}')
print(f'negative hpo:\n{hn}')
print(f'maximally specific hpo:\n{h}')



# OUTPUT


# positive hypothesies 
#  [['sunny', 'warm', 'high', 'strong', 'warm', 'same', 'yes'], ['sunny', 'warm', 'high', 'strong', 'cool', 'change', 'yes']]
# negative hypothesies 
#  [['rainy', 'cold', 'high', 'strong', 'warm', 'change', 'no']]
# max specific hypothesies 
#  ['sunny', 'warm', 'high', 'strong', '?', '?']

