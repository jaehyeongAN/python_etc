import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

#### 0. Load data - Breast Cancer Dataset
cancer = pd.read_csv('./input/data.csv')
cancer.drop(['id','Unnamed: 32'], axis=1, inplace=True)


#### 1. Column distribution by target ###########################################################
for cnt, col in enumerate(cancer):
    try:
        if cnt==0:
            continue
            
        plt.figure(figsize=(12, 6))
        sns.distplot(cancer[col][cancer['diagnosis']=='M'])
        sns.distplot(cancer[col][cancer['diagnosis']=='B'])
        plt.legend(['malignant','benign'], loc='best')
        plt.title('histogram of features '+str(col))
        plt.show()
    except Exception as e:
        pass


#### 2. 2D plot  ###########################################################
X = cancer.drop(['diagnosis'], axis=1)
y = cancer['diagnosis']
scaler = StandardScaler()
cancer_scale = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

pca2 = PCA(n_components=2)
data_pca2 = pca2.fit_transform(cancer_scale)

plt.figure(figsize=(12, 8))
plt.scatter(data_pca2[:,0], data_pca2[:,1], c=cancer['diagnosis'], s=40, edgecolors='white')
plt.title("2D of Target distribution by diagnosis")
plt.xlabel('pcomp 1')
plt.ylabel('pcomp 2')
plt.show()


#### 3. 3D plot   ###########################################################
pca3 = PCA(n_components=3)
data_pca3 = pca3.fit_transform(cancer_scale)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data_pca3[:,0], data_pca3[:,1], data_pca3[:,2], c=cancer['diagnosis'], s=60, edgecolors='white')
ax.set_title('3D of Target distribution by diagnosis')
ax.set_xlabel('pcomp 1')
ax.set_ylabel('pcomp 2')
ax.set_zlabel('pcomp 3')
plt.show()


#### 4. Corrleation  ###########################################################
cancer_tmp = cancer.copy()
cancer_tmp['diagnosis'] = cancer['diagnosis'].replace({'M':1, 'B':0})
corrmat = cancer_tmp.corr()
top_corr_features = corrmat.index[abs(corrmat["diagnosis"])>=0.3]

plt.figure(figsize=(13,10))
g = sns.heatmap(cancer[top_corr_features].corr(), annot=True, cmap="RdYlGn")
plt.show()


#### 5. Feature Importance   ###########################################################
clf = RandomForestClassifier(random_state=42, max_depth=6)
clf.fit(X, y)
feature_importance = clf.feature_importances_

df_fi = pd.DataFrame({'columns':X.columns, 'importances':feature_importance})
df_fi = df_fi[df_fi['importances'] > 0] # importance가 0이상인 것만 
df_fi = df_fi.sort_values(by=['importances'], ascending=False)

fig = plt.figure(figsize=(15,7))
ax = sns.barplot(df_fi['columns'], df_fi['importances'])
ax.set_xticklabels(df_fi['columns'], rotation=80, fontsize=13)
plt.tight_layout()
plt.show()