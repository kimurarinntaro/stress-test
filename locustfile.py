from locust import HttpUser, TaskSet, task, between, constant
import itertools

XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

class UserBehavior(TaskSet):
    test_file = None

    def on_start(self):
        self.test_file = itertools.cycle(["/Users/rintarokimura/Desktop/neko.xlsx"])

    # @task(1)
    # def get(self):
    #     response = self.client.get("/boards/KT662/", verify=False)
    #     print(response.status_code)

    @task(1)
    def post_file(self):
        url = "/api/kumi/KT662/files"
        file_path = next(self.test_file)

        with open(file_path, "rb") as f:
            files = {"file": f}
            response = self.client.post(url, files=files)
            print(response.status_code)

    # @task(1)
    # def patch_file_member(self):
    #     url = "/api/kumi/KT662/files/bcd197a5-fd06-4fa0-b203-aac1d01dd23b/member/e85c0cd3-5444-4487-a1b1-8e75672edc58"
    #     headers = {"Content-Type": "application/json"}
    #     response = self.client.patch(url, headers=headers)
    #     print(response.status_code)


class WebsiteUser(HttpUser):
    wait_time = constant(0)
    tasks = [UserBehavior]
    
