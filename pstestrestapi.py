import unittest
import requests


class TasksTestCase(unittest.TestCase):
    def test_task_creation(self):
        url = 'http://127.0.0.1:5000/todo/tasks'
        data = {'title': 'get a pocket of milk'}
        response = requests.post(url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json()['status'])

    def test_get_task(self):
        url = 'http://127.0.0.1:5000/todo/tasks/1'
        response = requests.get(url)
        task = response.json()['task']
        self.assertEqual(task['id'], 1001)

    def test_delete_task(self):
        url = 'http://127.0.0.1:5000/todo/tasks/1'
        response = requests.delete(url)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()