import os
import logging

# Configure logging without exposing secrets
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_aws_secret_key():
    """
    Retrieve AWS secret key from environment variables.

    Returns:
        str: AWS secret key from environment.

    Raises:
        ValueError: If AWS_SECRET_KEY is not set in environment.
    """
    secret_key = os.getenv("AWS_SECRET_KEY")
    if not secret_key:
        raise ValueError(
            "AWS_SECRET_KEY not found. Set it in environment variables or .env file."
        )
    return secret_key


def connect():
    """
    Connect to AWS using credentials from environment variables.

    Logs connection status without exposing the actual secret key.
    """
    try:
        secret_key = get_aws_secret_key()
        # Log safely without exposing the full key
        key_preview = secret_key[:8] + "..." if len(secret_key) > 8 else "***"
        logger.info(f"Connecting to AWS (key starts with: {key_preview})")
        # Actual connection logic would go here
        return True
    except ValueError as e:
        logger.error(f"Connection failed: {e}")
        return False


if __name__ == "__main__":
    connect()
