from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from enum import Enum

class BugSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class BugStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    FIXED = "fixed"
    CLOSED = "closed"

class Bug(BaseModel):
    id: Optional[str] = None
    title: str
    description: str
    severity: BugSeverity
    status: BugStatus = BugStatus.OPEN
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    test_cases: List[str] = []

class TestCase(BaseModel):
    id: Optional[str] = None
    name: str
    description: str
    input_data: dict
    expected_output: dict
    is_edge_case: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    bug_id: Optional[str] = None 