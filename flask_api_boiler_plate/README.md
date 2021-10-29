## Documentation

## Local Development Setup

### Environment Variables

We are using `dotenv` package to utilize environment variables in this project. Refer to `.env.example` file in the repo to see the existing environment variables. Then make a new copy of this file and rename it to `.env` in the root of the project.

## Tests:

Test scripts are located in `manage.py > tests`. To run the tests you have three options to run them. You must have following environment variable set before running tests from the comand line:

```bash
export FLASK_APP=manage.py

```

1. Running in **watch** mode: will keep your tests watching for changes and run them
   ```bash
   flask tests watch
   ```
2. Running in **debug** mode: will prompt you to debugging console if any error is thrown during running tests
   ```bash
   flask tests debug
   ```
3. Running in in coverage mode: will generate html files of the coverage report. You can open `./tests/coverage/html_report/index.html` to see the whole report.

   ```bash
   flask tests coverage
   ```

4. Runnning without passing any parameters: will run the whole tests and generates `coverage.xml` report which needs to be committed with your MR.
   ```bash
   flask tests
   ```
