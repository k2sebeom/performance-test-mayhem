from locust import HttpUser, task, between
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np


class HelloWorldUser(HttpUser):
    log = []
    wait_time=between(1, 3)

    @task
    def hello_world(self):
        resp = self.client.get("/")
        HelloWorldUser.log.append(resp.elapsed.microseconds // 1000)

    def on_stop(self):
        super().on_stop()
        mean, std = norm.fit(HelloWorldUser.log)
        plt.hist(HelloWorldUser.log, bins=20, density=True)

        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, mean, std)
        plt.plot(x, p, 'k', linewidth=2)

        percentiles = [1, 5, 10, 25, 50, 75, 90, 95, 99]
        for p in percentiles:
            value = np.percentile(HelloWorldUser.log, p)
            print(f"{p}th percentile: {value:.2f}")

        plt.show()
        HelloWorldUser.log.clear()

