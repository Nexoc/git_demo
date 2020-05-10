import time


def time_track(funk):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = funk(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала {elapsed} секунды')
        return result
    return surrogate