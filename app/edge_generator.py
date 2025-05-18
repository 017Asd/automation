from typing import List, Dict, Any
from .models import TestCase
import random

def generate_edge_cases(test_case: TestCase) -> List[TestCase]:
    """
    Generate edge cases based on the input test case
    """
    edge_cases = []
    
    # Generate boundary value cases
    edge_cases.extend(generate_boundary_cases(test_case))
    
    # Generate null/empty cases
    edge_cases.extend(generate_null_cases(test_case))
    
    # Generate type mismatch cases
    edge_cases.extend(generate_type_mismatch_cases(test_case))
    
    return edge_cases

def generate_boundary_cases(test_case: TestCase) -> List[TestCase]:
    """
    Generate test cases with boundary values
    """
    edge_cases = []
    input_data = test_case.input_data
    
    for key, value in input_data.items():
        if isinstance(value, (int, float)):
            # Generate min, max, and zero cases
            edge_cases.append(create_edge_case(
                test_case,
                f"min_value_{key}",
                {**input_data, key: float('-inf')}
            ))
            edge_cases.append(create_edge_case(
                test_case,
                f"max_value_{key}",
                {**input_data, key: float('inf')}
            ))
            edge_cases.append(create_edge_case(
                test_case,
                f"zero_value_{key}",
                {**input_data, key: 0}
            ))
    
    return edge_cases

def generate_null_cases(test_case: TestCase) -> List[TestCase]:
    """
    Generate test cases with null/empty values
    """
    edge_cases = []
    input_data = test_case.input_data
    
    for key in input_data.keys():
        edge_cases.append(create_edge_case(
            test_case,
            f"null_{key}",
            {**input_data, key: None}
        ))
    
    return edge_cases

def generate_type_mismatch_cases(test_case: TestCase) -> List[TestCase]:
    """
    Generate test cases with type mismatches
    """
    edge_cases = []
    input_data = test_case.input_data
    
    for key, value in input_data.items():
        if isinstance(value, (int, float)):
            edge_cases.append(create_edge_case(
                test_case,
                f"string_{key}",
                {**input_data, key: str(value)}
            ))
        elif isinstance(value, str):
            edge_cases.append(create_edge_case(
                test_case,
                f"number_{key}",
                {**input_data, key: 123}
            ))
    
    return edge_cases

def create_edge_case(original_case: TestCase, name_suffix: str, input_data: Dict[str, Any]) -> TestCase:
    """
    Create a new edge case based on the original test case
    """
    return TestCase(
        name=f"{original_case.name}_edge_{name_suffix}",
        description=f"Edge case for {original_case.name}: {name_suffix}",
        input_data=input_data,
        expected_output=original_case.expected_output,
        is_edge_case=True,
        bug_id=original_case.bug_id
    ) 