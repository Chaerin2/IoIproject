from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 날씨 데이터와 옷 데이터 (예시)
weather_data = [
    [25, 70],  # 온도: 25°C, 습도: 70%
    [10, 45],
    # ... 다른 데이터 추가
]

clothing_labels = [
    "반팔 티셔츠와 반바지",
    "자켓과 청바지",
    # ... 다른 데이터 추가
]

# 데이터 전처리
X = weather_data
y = clothing_labels

# 데이터 분할 (학습 데이터와 테스트 데이터)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 머신러닝 모델 선택 및 학습
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 예측 및 평가
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("모델 정확도:", accuracy)

# 사용자에게 날씨 정보 입력 받기
temperature = float(input("현재 기온을 입력하세요 (°C): "))
humidity = float(input("현재 습도를 입력하세요 (%): "))

# 사용자 입력을 특성으로 변환
user_input = [[temperature, humidity]]

# 옷 추천 예측
recommended_clothing = model.predict(user_input)[0]

print("추천 옷차림:", recommended_clothing)
