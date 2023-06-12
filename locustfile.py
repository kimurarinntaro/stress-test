from locust import HttpUser, TaskSet, task, between, constant
import itertools

class UserBehavior(TaskSet):
    test_file = None

    #postでファイルを使い回す場合はここを変更
    def on_start(self):
        self.test_file = itertools.cycle()

    #GETリクエスト
    # @task(1)
    # def get(self):
    #     response = self.client.get("", verify=False)
    #     print(response.status_code)

    #POSTリクエスト
    # @task(1)
    # def post_file(self):
    #     url = ""
    #     file_path = next(self.test_file)

    #     with open(file_path, "rb") as f:
    #         files = {"file": f}
    #         response1 = self.client.post(url, files=files)
    #         print(response1.status_code)

    #PATCHリクエスト
    # @task(1)
    # def patch_file_member(self):
    #     url = ""
    #     headers = {"Content-Type": "application/json"}
    #     response = self.client.patch(url, headers=headers)
    #     print(response.status_code)


class WebsiteUser(HttpUser):
    wait_time = constant(0)
    tasks = [UserBehavior]
    
