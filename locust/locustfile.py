from locust import Locust, TaskSet, task
import random

TOTAL_USERS_COUNT = 2000
TOTAL_TUITS_COUNT = 10000


class WebsiteTasks(TaskSet):
    @task(10)
    def get_tuits_page(self):
        # get random page from 1..1000 (we assume we have 10 000 tuits, 10 per page)
        self.client.get("/?page=" + str(random.randint(1, TOTAL_TUITS_COUNT / 10)), name='main')

    @task(1)
    def get_profile_page(self):
        self.client.get("/accounts/show/" + str(random.randint(1, TOTAL_USERS_COUNT)) + '/', name="profile")


class SomePopularTuits(TaskSet):
    @task(30)
    def get_popular_tuit(self):
        self.client.get("/tuit/show/" + str(random.randint(1, 10)) + '/', name="popular")

    @task(1)
    def get_unpopular_tuit(self):
        self.client.get("/tuit/show/" + str(random.randint(11, TOTAL_TUITS_COUNT)) + '/', name="unpopular")


class TestAPI(TaskSet):
    @task(10)
    def get_api_page(self):
        self.client.get('/api/v1/tuit/?format=json&limit=10&offest='+str(random.randint(1, TOTAL_TUITS_COUNT)), name="api main")

    @task(10)
    def get_tuits_page(self):
        # get random page from 1..1000 (we assume we have 10 000 tuits, 10 per page)
        self.client.get("/without_user/?page=" + str(random.randint(1, TOTAL_TUITS_COUNT / 10)), name='main w/o user')


class TestTemplates(TaskSet):
    @task(10)
    def get_tuits_page_django(self):
        # get random page from 1..1000 (we assume we have 10 000 tuits, 10 per page)
        self.client.get("/?page=" + str(random.randint(1, TOTAL_TUITS_COUNT / 10)), name='main django templates')

    @task(10)
    def get_tuits_page_jinja2(self):
        # get random page from 1..1000 (we assume we have 10 000 tuits, 10 per page)
        self.client.get("/jinja2/?page=" + str(random.randint(1, TOTAL_TUITS_COUNT / 10)), name='main Jinja2')


class WebsiteUser(Locust):
    task_set = TestTemplates
    min_wait = 0.5 * 1000
    max_wait = 1 * 1000
