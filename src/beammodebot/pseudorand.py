import mmh3

def roll_100_for_string(s: str, unix_epoch: int) -> int:
    """
    Produces non crypto safe shitty presudorandom number in range [0, 100]
    """
    epoch_m = unix_epoch // 60
    hash = mmh3.mmh3_x64_128_uintdigest(f'{s}|{epoch_m}'.encode('utf-8'))
    return hash % 101

def roll_100_for_user(user_id: int, unix_epoch: int) -> int:
    """
    Produces non crypto safe shitty presudorandom number in range [0, 100]
    """
    epoch_m = unix_epoch // 60
    hash = mmh3.mmh3_x64_128_uintdigest(f'{user_id}|{epoch_m}'.encode('utf-8'))
    return hash % 101
