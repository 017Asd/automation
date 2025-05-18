# Bug Slayer

Bug Slayer is a powerful API-driven tool for automated bug testing and edge case generation. It helps developers identify potential issues in their code by automatically generating and running test cases, including edge cases that might be overlooked during manual testing.

## Features

- Automated test case generation
- Edge case detection and generation
- RESTful API for test management
- Bug tracking and management
- Test result reporting
- CI/CD integration with Jenkins

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bug-slayer.git
cd bug-slayer
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the API server:
```bash
uvicorn app.main:app --reload
```

2. Access the API documentation at `http://localhost:8000/docs`

### API Endpoints

- `POST /api/bugs/` - Create a new bug report
- `GET /api/bugs/` - List all bugs
- `GET /api/bugs/{bug_id}` - Get bug details
- `PUT /api/bugs/{bug_id}` - Update bug status
- `POST /api/test-cases/` - Create a new test case
- `GET /api/test-cases/` - List all test cases
- `POST /api/test-cases/{test_case_id}/run` - Run a test case
- `POST /api/test-cases/generate-edge-cases` - Generate edge cases

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

The project uses:
- Black for code formatting
- Flake8 for linting
- isort for import sorting

Run the linters:
```bash
flake8 app tests
black app tests
isort app tests
```

### CI/CD Pipeline

The project uses Jenkins for continuous integration and deployment. The pipeline includes:
- Code linting and style checking
- Unit testing with coverage reporting
- Build verification
- Deployment to staging/production environments

To set up the Jenkins pipeline:
1. Install Jenkins on your server
2. Install required Jenkins plugins:
   - Pipeline
   - Git
   - Cobertura
   - JUnit
3. Create a new pipeline job and point it to the Jenkinsfile in this repository

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- FastAPI for the web framework
- Pytest for testing framework
- Jenkins for CI/CD 