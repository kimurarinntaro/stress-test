from locust import HttpUser, TaskSet, task, between, constant
import itertools

XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

class UserBehavior(TaskSet):
    test_file = None

    def on_start(self):
        self.test_file = itertools.cycle(["/Users/rintarokimura/Desktop/neko.xlsx"])

    @task(1)
    def get(self):
        self.client.get("/boards/KT662", verify=False)

    @task(1)
    def post_file(self):
        url = "/api/kumi/KT662/files"
        file_path = next(self.test_file)

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = self.client.post(url, files=files)
            print(response.status_code)

class WebsiteUser(HttpUser):
    wait_time = constant(0)
    tasks = [UserBehavior]
    
