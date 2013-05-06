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


class WebsiteUser(Locust):
    task_set = WebsiteTasks
    min_wait = 0.5 * 1000
    max_wait = 1 * 1000
