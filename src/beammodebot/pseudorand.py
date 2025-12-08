import mmh3

def roll100(key: str | int, unix_epoch: int) -> int:
    """
    Produces non crypto safe shitty presudorandom number in range [0, 100]
    """
    epoch_m = unix_epoch // 60
    hash = mmh3.mmh3_x64_128_uintdigest(f'{key}|{epoch_m}'.encode('utf-8'))
    return hash % 101
