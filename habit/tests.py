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

        print(response.json())

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

        print(response.json())

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """
        Тест списка привычек.
        """

        data = {'id': 2,
                'place': 'на улице',
                'time': '2022-11-11T17:30:00+03:00',
                'action': 'бегать',
                'enjoyable': True,
                'frequency': 1,
                'time_required': '00:01:30',
                'is_public': True,
                'owner': 1,
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

        print(response.json())

        self.assertEqual(response.json(),
                         {'count': 0,
                          'next': None,
                          'previous': None,
                          'results':
                              [
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
                                   'related_habit': None},
                                  {'id': 2,
                                   'place': 'на улице',
                                   'time': '2022-11-11T17:30:00+03:00',
                                   'action': 'бегать',
                                   'enjoyable': True,
                                   'frequency': 1,
                                   'reward': None,
                                   'time_required': '00:01:30',
                                   'is_public': True,
                                   'owner': 1,
                                   'related_habit': None
                                   }
                              ]
                          }
                         )

        self.assertTrue(
            Habit.objects.all().exists()
        )
