import uuid
from datetime import datetime
from typing import Dict, Any, Optional
import json
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_id() -> str:
    """
    Generate a unique ID for bugs and test cases
    """
    return str(uuid.uuid4())

def format_datetime(dt: datetime) -> str:
    """
    Format datetime object to ISO format string
    """
    return dt.isoformat()

def parse_datetime(dt_str: str) -> datetime:
    """
    Parse ISO format string to datetime object
    """
    return datetime.fromisoformat(dt_str)

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Load and parse a JSON file
    """
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Failed to load JSON file {file_path}: {str(e)}")
        raise

def save_json_file(data: Dict[str, Any], file_path: str):
    """
    Save data to a JSON file
    """
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logger.error(f"Failed to save JSON file {file_path}: {str(e)}")
        raise

def validate_json_schema(data: Dict[str, Any], schema: Dict[str, Any]) -> bool:
    """
    Validate data against a JSON schema
    """
    # TODO: Implement JSON schema validation
    return True

def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input to prevent injection attacks
    """
    # TODO: Implement input sanitization
    return input_str 