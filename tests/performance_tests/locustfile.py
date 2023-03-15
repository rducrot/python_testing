from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task
    def index(self):
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/show-summary", {"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get("/book/Spring%20Festival/Simply%20Lift")

    @task
    def purchase_places(self):
        self.client.post("/purchase-places", {"competition": "Spring Festival",
                                              "club": "Simply Lift",
                                              "places": "1"})

    @task
    def clubs_points(self):
        self.client.get("/clubs-points")

    @task
    def logout(self):
        self.client.get("/logout")
