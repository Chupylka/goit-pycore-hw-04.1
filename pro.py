# 📦 Імпортування бібліотек
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 📥 Завантаження даних
df = pd.read_csv("House_Rent_Dataset - House_Rent_Dataset.csv")

# 🔍 Перевірка та очищення
df['Floor Level'] = df['Floor'].str.extract(r'(\d+|Ground)').replace('Ground', 0).astype(float)
df_encoded = pd.get_dummies(df, columns=['Area Type', 'Furnishing Status', 'Tenant Preferred', 'City'], drop_first=True)
df_encoded.drop(columns=['Posted On', 'Floor', 'Area Locality', 'Point of Contact'], inplace=True)

# 🎯 Визначення X, y
X = df_encoded.drop('Rent', axis=1)
y = df_encoded['Rent']

# ✂️ Тренувальна та тестова вибірки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🔁 Модель 1: Лінійна регресія
model_lr = LinearRegression()
model_lr.fit(X_train, y_train)
pred_lr = model_lr.predict(X_test)

# 🌲 Модель 2: Random Forest
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_rf.fit(X_train, y_train)
pred_rf = model_rf.predict(X_test)

# 📊 Оцінка якості
def evaluate(y_true, y_pred, model_name):
    print(f"\n📌 {model_name}")
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R2 Score:", r2_score(y_true, y_pred))

evaluate(y_test, pred_lr, "Лінійна регресія")
evaluate(y_test, pred_rf, "Random Forest")

# 📈 Візуалізація результатів
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=pred_lr)
plt.title("Лінійна регресія: Факт vs Прогноз")
plt.xlabel("Справжня ціна")
plt.ylabel("Прогнозована ціна")

plt.subplot(1, 2, 2)
sns.scatterplot(x=y_test, y=pred_rf)
plt.title("Random Forest: Факт vs Прогноз")
plt.xlabel("Справжня ціна")
plt.ylabel("Прогнозована ціна")

plt.tight_layout()
plt.show()