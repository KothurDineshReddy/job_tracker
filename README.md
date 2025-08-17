# Job Tracker

A Python application for tracking job applications and opportunities.

## Features

- Job application tracking
- CI/CD pipeline with GitHub Actions
- Automated testing and deployment

## Development Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd job_tracker
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest
```

4. Format code:
```bash
black .
```

5. Lint code:
```bash
flake8
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. The pipeline includes:

### Triggers
- **Push to main/master branch**: Runs full CI/CD pipeline
- **Pull requests**: Runs tests and linting only

### Stages

1. **Test Stage**
   - Runs on multiple Python versions (3.8, 3.9, 3.10, 3.11)
   - Installs dependencies
   - Runs linting with flake8
   - Checks code formatting with black
   - Runs tests with pytest
   - Generates coverage reports

2. **Build Stage** (main/master only)
   - Builds the Python package
   - Uploads build artifacts

3. **Deploy Stage** (main/master only)
   - Downloads build artifacts
   - Deploys to production environment
   - Sends deployment notifications

## Configuration Files

- `.github/workflows/ci-cd.yml`: Main CI/CD workflow
- `requirements.txt`: Python dependencies
- `pyproject.toml`: Project configuration and build settings
- `.flake8`: Linting configuration
- `tests/`: Test directory with sample tests

## Customization

### Adding Dependencies
Add your project dependencies to `requirements.txt`:
```
your-package>=1.0.0
```

### Deployment Configuration
Edit the deploy job in `.github/workflows/ci-cd.yml` to add your specific deployment commands:
```yaml
- name: Deploy to production
  run: |
    # Add your deployment commands here
    # Examples:
    # - Deploy to AWS, GCP, Azure
    # - Deploy to container registry
    # - Deploy to server
```

### Environment Variables
Add environment variables in GitHub repository settings:
1. Go to Settings > Secrets and variables > Actions
2. Add your secrets (API keys, deployment credentials, etc.)

## Contributing

1. Create a feature branch
2. Make your changes
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

The CI/CD pipeline will automatically run tests and checks on your pull request.
