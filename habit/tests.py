from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create(email='test@mail.ru', password='test', is_staff=True, is_superuser=True)
        self.client.force_authenticate(user=self.user)  # Аутентификация пользователя

    def test_create_habit(self):
        """
        Тест создания привычки.
        """
        data = {
            'id': 1,
            'place': 'на улице',
            'time': '2022-11-11T17:30:00+03:00',
            'action': 'бегать',
            'enjoyable': True,
            'frequency': 1,
            'time_required': '00:01:30',
            'is_public': True,
            'owner': 1
        }

        response = self.client.post(

            '/habit/create/',
            data=data

        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1,
             'place': 'на улице',
             'time': '2022-11-11T17:30:00+03:00',
             'action': 'бегать',
             'enjoyable': True,
             'frequency': 1,
             'reward': None,
             'time_required': '00:01:30',
             'is_public': True,
             'owner': 1,
             'related_habit': None})

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """
        Тест списка привычек.
        """

        data = {
            "place": "дома",
            "time": "2022-11-11T17:30:00+03:00",
            "action": "бегать",
            "enjoyable": True,
            "frequency": 1,
            "time_required": "00:01:30",
            "is_public": True
        }

        res = self.client.post(
            '/habit/create/',
            data=data
        )

        response = self.client.get('/habit/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {"count": 1,
                          "next": None,
                          "previous": None,
                          "results": [
                              {
                                  "id": 3,
                                  "place": "дома",
                                  "time": "2022-11-11T17:30:00+03:00",
                                  "action": "бегать",
                                  "enjoyable": True,
                                  "frequency": 1,
                                  "reward": None,
                                  "time_required": "00:01:30",
                                  "is_public": True,
                                  "owner": 3,
                                  "related_habit": None
                              }
                          ]
                          }
                         )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_retrieve_habit(self):
        """
        Тест на просмотр привычки.
        """
        data = {
            "place": "дома",
            "time": "2022-11-11T17:30:00+03:00",
            "action": "бегать",
            "enjoyable": True,
            "frequency": 1,
            "time_required": "00:01:30",
            "is_public": True
        }

        res = self.client.post(
            '/habit/create/',
            data=data
        )

        habit_id = res.data['id']

        response = self.client.get(f'/habit/{habit_id}/')

        self.assertEqual(response.json(),
                         {
                             "id": 4,
                             "place": "дома",
                             "time": "2022-11-11T17:30:00+03:00",
                             "action": "бегать",
                             "enjoyable": True,
                             "frequency": 1,
                             "reward": None,
                             "time_required": "00:01:30",
                             "is_public": True,
                             "owner": 4,
                             "related_habit": None
                         }
                         )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_update_habit(self):
        """
        Тест на редактирование привычки.
        """
        data = {
            "place": "дома",
            "time": "2022-11-11T17:30:00+03:00",
            "action": "бегать",
            "enjoyable": True,
            "frequency": 1,
            "time_required": "00:01:30",
            "is_public": True
        }

        res = self.client.post(
            '/habit/create/',
            data=data
        )

        habit_id = res.data['id']

        data_update = {
            "place": "на улице",
            "time": "2022-11-11T17:30:00+03:00",
            "action": "бегать",
            "enjoyable": True,
            "frequency": 1,
            "time_required": "00:01:30",
            "is_public": True,
        }

        response = self.client.patch(f'/habit/update/{habit_id}/', data=data_update)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertTrue(Habit.objects.all().exists())

    def test_delete_habit(self):
        """
        Тест на удаление привычки.
        """
        data = {
            "place": "на улице",
            "time": "2022-11-11T17:30:00+03:00",
            "action": "бегать",
            "enjoyable": True,
            "frequency": 1,
            "time_required": "00:01:30",
            "is_public": True,
        }

        res = self.client.post(

            '/habit/create/',
            data=data

        )

        self.assertEqual(
            res.status_code,
            status.HTTP_201_CREATED
        )

        habit_id = res.data['id']

        response = self.client.delete(f'/habit/delete/{habit_id}/')

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(Habit.objects.all().exists())

        print(res.json())
