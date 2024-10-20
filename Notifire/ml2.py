import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


data = pd.read_csv("C:\\Users\\Bijaya KC\\Documents\\pyy\\try.csv")


X = data[['Latitude', 'Longitude', 'Wind_Speed', 'Wind_Direction', 'Elevation', 'Soil_Moisture', 'Precipitation', 'Temp_Celsius']]
y = data['Fire_Occurrence']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

print(classification_report(y_test, y_pred, zero_division=1))


new_data = pd.DataFrame([['35.129','-120.462','4.2','220','830','12.6','0.0','36.0']],
                        columns=['Latitude', 'Longitude', 'Wind_Speed', 'Wind_Direction', 'Elevation', 'Soil_Moisture', 'Precipitation', 'Temp_Celsius'])

prediction = model.predict(new_data)
print(prediction)
if prediction[0] == 1:
    print("There is a risk of a forest fire.")
else:
    print(" no risk of a forest fire.")
