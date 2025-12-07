import os

def get_tg_config() -> tuple[int, str, str]:
    """
    Get the Telegram API configuration from the environment variables.
    
    Returns:
        tuple[int, str, str]: (api_id, api_hash, BOT_TOKEN)
    
    Raises:
        ValueError: If any required environment variable is missing or invalid.
    """
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    
    if api_id is None:
        raise ValueError("Environment variable 'api_id' is not set")
    
    if api_hash is None:
        raise ValueError("Environment variable 'api_hash' is not set")
    
    if BOT_TOKEN is None:
        raise ValueError("Environment variable 'BOT_TOKEN' is not set")
    
    try:
        api_id_int = int(api_id)
    except ValueError as e:
        raise ValueError(f"Environment variable 'api_id' must be a valid integer, got '{api_id}'") from e

    return api_id_int, api_hash, BOT_TOKEN