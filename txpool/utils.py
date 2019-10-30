import pickle
import txpool.worker


def wrap_callable(func, args, kwargs):
    if isinstance(func, str):
        func = txpool.worker.import_callable(func)
    return func(*args, **kwargs)
