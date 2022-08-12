import logging
from katatachi.worker import WorkFactory
from katatachi.utils import WorkerQueue

logger = logging.getLogger(__name__)


def start_worker_blocking(worker_queue: WorkerQueue, work_factory: WorkFactory):
    try:
        while True:
            payload = worker_queue.blocking_dequeue()
            module_name, args = payload.module_name, payload.args
            work_func_and_id = work_factory.get_work_func(module_name, args)
            if not work_func_and_id:
                return
            work_func, worker_id = work_func_and_id
            work_func()

    except (KeyboardInterrupt, SystemExit):
        logger.info("Worker stopping...")
