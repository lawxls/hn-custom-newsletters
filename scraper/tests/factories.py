from factory import Faker
from factory.django import DjangoModelFactory

from scraper.models import Thread


class ThreadFactory(DjangoModelFactory):
    thread_id = Faker("pyint")
    title = Faker("sentence")
    link = Faker("url")
    comments_link = Faker("url")
    score = Faker("pyint")
    comments_count = Faker("pyint")
    thread_created_at = Faker("date_time")

    class Meta:
        model = Thread
