import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')

tips = sns.load_dataset("tips") # 데이터 로드
print(tips.columns)	# 칼럼명 
print(tips.head())	# 첫 5개 행

### EDA 
# 데이터 요약 정보 
tips_summary = tips.describe()
print(tips_summary) 	


# 칼럼별 데이터 분포 살펴보기
# 성별별 지불(total_bill) 금액
f, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,4))
ax1.hist(tips.total_bill[tips.sex=='Male'])
ax1.set_title('Male')
ax2.hist(tips.total_bill[tips.sex=='Female'])
ax2.set_title('Female')
plt.xlabel('Sex'); plt.ylabel('Total Bill($)')
plt.show()

# time별 팁(tip) 금액
f, (ax1, ax2) = plt.subplots(2,1, sharex=True, figsize=(12,4))
ax1.hist(tips.tip[tips.time=='Dinner'])
ax1.set_title('Dinner')
ax2.hist(tips.tip[tips.time=='Lunch'])
ax2.set_title('Lunch')
plt.xlabel('Time'); plt.ylabel('Tip($)')       
plt.show()

# 데이터별 상관관계(heatmap)
ht = tips.corr(method='pearson')
sns.heatmap(data=ht, annot=True)
plt.show()


### Boxplot
#ax = sns.boxplot(x="day", y="total_bill", data=tips)	# 요일별 지불금액 
#plt.show()
ax = sns.boxplot(x=tips["total_bill"])	# 지불금액 boxplot
plt.show()

Q1 = np.percentile(tips['total_bill'], 25, axis=0)	# 1 사분위
Q3 = np.percentile(tips['total_bill'], 75, axis=0)	# 3 사분위

# Inter Quartile Range
IQR = Q3 - Q1
up_iqr = Q3 + (1.5 * IQR)
down_iqr = Q1 - (1.5 * IQR)

# 이상치 출력 
outliers = []
for i in tips['total_bill']:
	if i>= up_iqr or i <= down_iqr:		# IQR의 범위를 벗어나면 outlier
		outliers.append(i)

print('Outliers : \n',outliers)


