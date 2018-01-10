import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.cross_validation import cross_val_score as crossVS
from xgboost import XGBClassifier as XGBC

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
#print(train.info())
#print(test.info())
select_features = ['Pclass','Sex','Age','Embarked','SibSp','Parch','Fare']

X_train = train[select_features]
X_test = test[select_features]
y_train = train['Survived']

#print(X_train['Embarked'].value_counts())
#print(y_train)

X_train['Embarked'].fillna('S',inplace=True)
X_test['Embarked'].fillna('S',inplace=True)

X_train["Age"].fillna(X_train["Age"].mean(),inplace=True)
X_test['Age'].fillna(X_test['Age'].mean(),inplace=True)
X_test['Fare'].fillna(X_test['Fare'].mean(),inplace=True)

#X_train.info()
dict_vec = DictVectorizer(sparse=False)
X_train = dict_vec.fit_transform(X_train.to_dict(orient='record'))
X_test  = dict_vec.transform(X_test.to_dict(orient='record'))
rfc = RFC()
xgbc = XGBC()
#print(crossVS(rfc , X_train, y_train, cv=5).mean())
#print(crossVS(xgbc , X_train, y_train, cv=5).mean())
#print(dict_vec.get_feature_names())

rfc.fit(X_train,y_train)
rfc_y_predict =rfc.predict(X_test)

rfc_submission = pd.DataFrame({'PassengerId':test['PassengerId'],'Survived':rfc_y_predict})

#rfc_submission.to_csv('rfc_submission.csv',index=False)


xgbc.fit(X_train,y_train)
xgbc_y_predict = xgbc.predict(X_test)
xgbc_submission = pd.DataFrame({'PassengerId':test['PassengerId'],'Survived':xgbc_y_predict})
xgbc_submission.to_csv('xgbc_submission.csv',index=False)
