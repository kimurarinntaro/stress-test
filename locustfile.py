from locust import HttpUser, TaskSet, task, between, constant
import itertools

XLSX_MIMETYPE = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# filePath = "/Users/rintarokimura/Desktop/neko.xlsx"
# fileDataBinary = open(filePath, "rb")
# data = {"uploadFile": (filePath, fileDataBinary, XLSX_MIMETYPE)}

class UserBehavior(TaskSet):
    test_file = None

    def on_start(self):
        self.test_file = itertools.cycle(["/Users/rintarokimura/Desktop/neko.xlsx"])

# @task(1)
    # def search(self):
    #     self.client.get("/boards/KT662", verify=False)

    # @task(2)
    # def search(self):
    #     response = self.client.post(
    #         url="/api/kumi/KTZZZ/files",
    #         files=data,
    #     )
    #     print(response.text)

    # @task(1)
    # def search(self):
    #     self.client.get("/", verify=False)

    @task(1)
    def search(self):
        url = "/api/kumi/KT662/files"
        file_path = next(self.test_file)
        # headers = {
        #     "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"
        # }
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = self.client.post(url, files=files)
            print(response.status_code)

class WebsiteUser(HttpUser):
    wait_time = constant(0)
    tasks = [UserBehavior]
    
