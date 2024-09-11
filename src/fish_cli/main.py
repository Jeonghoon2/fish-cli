import requests
import json

class App:

    def __init__(self) -> None:
        self.ip_address = None
        self.length = None
        self.weight = None

    def lr_api(self, length: float, api: str):
        headers = {'accept': 'application/json'}
        params = {'length': length}
        response = requests.get(f"{api}/fish/weight", params=params, headers=headers)
        data = response.json()  # JSON 데이터를 직접 파싱
        return data  # 'data'는 이제 float 객체가 되며, 직접 반환


    def kn_api(self, length: float, weight: float, api: str):
        headers = {'accept': 'application/json'}
        params = {'length': length, 'weight': weight}
        response = requests.get(f"{api}/fish/type", params=params, headers=headers)
        data = response.json()  # JSON 데이터를 직접 파싱
        return data['type']  # 'type' 키로 데이터를 반환


    def run(self):
        # IP 주소 입력 받기
        address = input("[ 🧭 ] 연결할 아이피 주소를 입력해주세요. < 예시 > 127.0.0.1:8080 : ")
        self.ip_address = "http://" + address

        # 물고기 길이 입력 받기
        self.length = float(input("[ 💬 ] 물고기의 길이를 입력하세요 : "))

        # 무게 도출
        self.weight = self.lr_api(self.length, api=self.ip_address)

        print(f"[ 🤖 ] 물고기의 무게 추정 {self.weight}")

        # 물고기 종류 도출
        fish_type = self.kn_api(self.length, self.weight, api=self.ip_address)

        print(f"[ 🤖 ] 길이가 {self.length}인 물고기는 무게가 {self.weight}으로 예측되며, 종류는 {fish_type} 예측됩니다.")


app = App()

if __name__ == "__main__":
    app.run()
