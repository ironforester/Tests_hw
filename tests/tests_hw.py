from unittest import TestCase
from parameterized import parameterized
from main import vote
from main import courses_duration
from main import solution

class TestPreviuosHomeWork(TestCase):

    @parameterized.expand(
        [
            ([1,1,1,22,3,3,3,3,14,14,14,14, 1], '1, 3, 14'),
            ([1,2,3,2,2], '2'),
        ]
    )
    def test_vote(self, votes, expected_res):
        result = vote(votes)
        self.assertEqual(result, expected_res)

    @parameterized.expand(
        [
            (["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"], [14, 20, 12, 20], {'Python-разработчик с нуля': 12, 'Java-разработчик с нуля': 14, 'Fullstack-разработчик на Python': 20, 'Frontend-разработчик с нуля': 20})
        ]
    )
    def test_courses_duration(self, courses, duration, expected_res):
        result = courses_duration(courses, duration)
        self.assertEqual(result, expected_res)

    @parameterized.expand([
        (1, 8, 15, (-3.0, -5.0)),
        (1, -13, 12, (12.0, 1.0)),
        (-4, 28, -49, 3.5),
        (1, 1, 1, None)
    ])
    def test_solution(self, a, b, c,  expected_result):
        result = solution(a, b, c)
        self.assertEqual(result, expected_result)
