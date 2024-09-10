import requests
import json

class App:

    def __init__(self) -> None:
        self.ip_address = None

    def lr_api(self, length: float, api: str):
        headers = {'accept': 'application/json'}
        params = {'length': length}
        response = requests.get(f"{api}:8080", params=params, headers=headers)
        data = json.loads(response.text)
        return data['weight']

    def kn_api(self, length: float, weight: float, api: str):
        headers = {'accept': 'application/json'}
        params = {'length': length, 'weight': weight}
        response = requests.get(f"{api}:8080", params=params, headers=headers)
        data = json.loads(response.text)
        return data['prediction']

    def run(self):
        # IP 주소 입력 받기
        address = input("🧭 연결할 아이피 주소를 입력해주세요. < 예시 > 127.0.0.1:8080 : ")
        self.ip_address = "http://" + address

        # 물고기 길이 입력 받기
        length = float(input("[ 💬 ] 물고기의 길이를 입력하세요 : "))

        # 무게 도출
        weight = self.lr_api(length, api=self.ip_address)

        # 물고기 종류 도출
        fish_type = self.kn_api(length, weight, api=self.ip_address)

        print(f"[ 🤖 ] 길이가 {length}인 물고기는 무게가 {weight}으로 예측되며, 종류는 {fish_type} 예측됩니다.")


# 모듈 수준에서 app 인스턴스 생성
app = App()

if __name__ == "__main__":
    app.run()
