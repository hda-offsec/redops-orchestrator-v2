from rq import Queue, Worker
from redis import Redis
from core.config import settings

redis_conn = Redis.from_url(settings.redis_url)


def enqueue(job_func, *args, queue_name: str):
    q = Queue(queue_name, connection=redis_conn)
    job = q.enqueue(job_func, *args)
    return job.id


def get_job(job_id: str, queue_name: str):
    q = Queue(queue_name, connection=redis_conn)
    return q.fetch_job(job_id)


def run_worker(queue: str):
    Worker([queue], connection=redis_conn).work(with_scheduler=True)
