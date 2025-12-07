def random_func(user_id: int, unix_epoch: int) -> int:
    """
    Produces non crypto safe shitty presudorandom number in range [0, 100]
    """
    epoch_m = unix_epoch // 60
    seed = user_id ^ ((epoch_m * 0x517cc1b727220a95) & 0xFFFFFFFFFFFFFFFF)
    h = fmix64(seed)
    return h % 101


def fmix64(k: int) -> int:
    """
    Finalization mix function for 64-bit integers (MurmurHash3 style).
    
    Args:
        k: Input integer, should fit in 64 bits (0 <= k <= 0xFFFFFFFFFFFFFFFF)
    
    Returns:
        Mixed 64-bit unsigned integer
    """
    # Assert that k fits in 64 bits (unsigned)
    assert 0 <= k <= 0xFFFFFFFFFFFFFFFF, f"k must be a 64-bit unsigned integer (0 <= k <= {0xFFFFFFFFFFFFFFFF}), got {k}"
    # Ensure k is treated as unsigned 64-bit
    k = k & 0xFFFFFFFFFFFFFFFF
    k ^= k >> 33
    k = (k * 0xff51afd7ed558ccd) & 0xFFFFFFFFFFFFFFFF
    k ^= k >> 33
    k = (k * 0xc4ceb9fe1a85ec53) & 0xFFFFFFFFFFFFFFFF
    k ^= k >> 33
    return k