import requests
import pytest

class TestDogAPI:

    base_url = "https://dog.ceo/api"

    def test_random_dog_image(self):
        url = f"{self.base_url}/breeds/image/random"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['status'] == 'success'
        print("Случайное изображение собаки:")
        print(data)

    def test_list_all_breeds(self):
        url = f"{self.base_url}/breeds/list/all"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['status'] == 'success'
        print("Список всех пород собак:")
        print(data)

    def test_specific_breed_images(self):
        breed = "bulldog"
        url = f"{self.base_url}/breed/{breed}/images/random/3"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['status'] == 'success'
        print(f"Изображения породы {breed}:")
        print(data)

    def test_sub_breeds_list(self):
        breed = "hound"
        url = f"{self.base_url}/breed/{breed}/list"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert data['status'] == 'success'
        print(f"Подпороды породы {breed}:")
        print(data)

    def test_invalid_breed(self):
        invalid_breed = "nonexistent"
        url = f"{self.base_url}/breed/{invalid_breed}/images/random"
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 404
        assert data['status'] == 'error'
        print(f"Результат для несуществующей породы {invalid_breed}:")
        print(data)
