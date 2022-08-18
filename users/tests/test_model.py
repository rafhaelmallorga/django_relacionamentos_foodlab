from xml.dom import ValidationErr

from django.test import TestCase
from users.models import User


class UserTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        print("=" * 100)
        print("setUpData executado")
        print("=" * 100)

        cls.user_1_data = {
            "first_name": "Raf",
            "last_name": "Tyson",
            "email": "raf@email.com",
            "favorite_season": "Inverto",
        }

        cls.user_2_data = {
            "first_name": "Raf",
            "last_name": "Tyson",
            "email": "raf@email.com",
        }

        cls.user_3_data = {
            "first_name": "Raf",
            "last_name": "Tyson",
            "email": "raf@email.com",
            "favorite_season": "Wrong choice",
        }

        cls.favorite_season_default = "Não especificado"

        cls.user_1 = User.objects.create(**cls.user_1_data)
        cls.user_2 = User.objects.create(**cls.user_2_data)
        cls.user_3 = User(**cls.user_3_data)

    def test_user_fields(self):
        self.assertEqual(self.user_1.first_name, self.user_1_data["first_name"])
        self.assertEqual(self.user_1.last_name, self.user_1_data["last_name"])
        self.assertEqual(self.user_1.email, self.user_1_data["email"])
        self.assertEqual(
            self.user_1.favorite_season, self.user_1_data["favorite_season"]
        )

    def test_favorite_season_default_choice(self):
        result_favorite_default = self.user_2.favorite_season
        msg = f"Verifique se o valor padrao e igual a {self.favorite_season_default}"

        self.assertEqual(result_favorite_default, self.favorite_season_default, msg)

    def test_favorite_season_wrong_choice(self):
        # with self.assertRaises(ValidationErr):
        #     self.user_3.full_clean()

        self.assertRaises(ValidationErr, self.user_3.full_clean)
