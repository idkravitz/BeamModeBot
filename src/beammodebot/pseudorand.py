import mmh3

def roll100(key: str | int, unix_epoch: int) -> int:
    """
    Produces non crypto safe shitty presudorandom number in range [0, 100]
    """
    return roll(key, unix_epoch, 0, 100)


def roll150(key: str | int, unix_epoch: int) -> int:
    return roll(key, unix_epoch, 0, 150)


def roll(key: str | int, unix_epoch: int, range_from: int, range_to: int) -> int:
    return hash(key, unix_epoch) % (range_to - range_from + 1) + range_from


def hash(key: str | int, unix_epoch: int, time_resolution: int = 60) -> int:
    epoch_m = unix_epoch // time_resolution
    hash = mmh3.mmh3_x64_128_uintdigest(f'{key}|{epoch_m}'.encode('utf-8'))
    return hash