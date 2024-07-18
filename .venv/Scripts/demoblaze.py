from locust import HttpUser, TaskSet, task, between, LoadTestShape

class UserBehavior(TaskSet):

    @task
    def register(self):
        self.client.get("/index.html")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)

class StagesShape(LoadTestShape):
    stages = [
        {"duration": 60, "users": 100, "spawn_rate": 100},
        {"duration": 60, "users": 100, "spawn_rate": 10},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None

if __name__ == "__main__":
    import os
    os.system("locust -f demoblaze.py --host=https://www.demoblaze.com")
