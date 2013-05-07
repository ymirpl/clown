from locust import Locust, TaskSet, task
import random

TOTAL_USERS_COUNT = 2000
TOTAL_TUITS_COUNT = 10000


class WebsiteTasks(TaskSet):
    @task(10)
    def get_tuits_page(self):
        # get random page from 1..1000 (we assume we have 10 000 tuits, 10 per page)
        self.client.get("/?page=" + str(random.randint(1, TOTAL_TUITS_COUNT / 10)), name='main')
        # self.client.get("/", data={'page': str(random.randint(1, TOTAL_TUITS_COUNT / 10))})

    @task(1)
    def get_profile_page(self):
        self.client.get("/accounts/show/" + str(random.randint(1, TOTAL_USERS_COUNT)) + '/', name="profile")


class SomePopularTuits(TaskSet):
    @task(80)
    def get_popular_tuit(self):
        self.client.get("/tuit/show/" + str(random.randint(1, 10)) + '/', name="popular")

    @task(1)
    def get_unpopular_tuit(self):
        self.client.get("/tuit/show/" + str(random.randint(11, TOTAL_TUITS_COUNT)) + '/', name="unpopular")


class WebsiteUser(Locust):
    task_set = SomePopularTuits
    min_wait = 0.5 * 1000
    max_wait = 1 * 1000
