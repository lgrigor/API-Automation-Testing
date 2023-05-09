#!/usr/bin/bash

# Configurable Variables
PYTEST_TAG=API
PARALLEL_EXEC=2

# Paths
PYTEST_LOG="./Results/pytest.log"
PYTEST_RESULT="./Results/pytest_results"
ALLURE_REPORT_DIR="./Results/allure-report"
PYTEST_RESULT_HISTORY="$PYTEST_RESULT/history"
ALLURE_REPORT_HISTORY="$ALLURE_REPORT_DIR/history"


# Function to run PyTest
pytest_runner() {
  printf "\nEXECUTOR: PyTest Execution Started...\n"
  echo "EXECUTOR: PyTest Execution Log -> $PYTEST_LOG"
  echo "EXECUTOR: pytest -s --alluredir=$PYTEST_RESULT $PYTEST_TAG $PARALLEL_EXEC"
  pytest -s --alluredir="$PYTEST_RESULT" -m "$PYTEST_TAG" -n "$PARALLEL_EXEC"> "$PYTEST_LOG"

  if grep -q 'ERROR' "$PYTEST_LOG"; then
    cleanup_after_pytest
    echo "EXECUTOR: ERROR Detected! Skipping Allure report generation..."
    echo "EXECUTOR: Press any key to Exit..."
    read -r
    exit 1
  fi
  printf "EXECUTOR: PyTest Execution Finished Successfully!\n"
}

# Function to remove junk files after PyTest
cleanup_after_pytest() {
    printf "\nEXECUTOR: Removing Junk Files after PyTest...\n"
    rm -rf .pytest_cache
    rm -rf Resource/__pycache__
    rm -rf Resource/Pages/__pycache__
    rm -rf Resource/Common/__pycache__
    rm -rf Tests/__pycache__
}

# Function to generate Allure report
generate_allure_report() {
    printf "\nEXECUTOR: Generating Allure report...\n"

    # Remove old result history if it exists
    if [ -d "$ALLURE_REPORT_HISTORY" ] && [ -d "$PYTEST_RESULT_HISTORY" ]; then
        echo "EXECUTOR: Removing old result history!"
        rm -rf "$PYTEST_RESULT_HISTORY"
    fi

    # Move new result history before generating report
    if [ -d "$ALLURE_REPORT_HISTORY" ]; then
        echo "EXECUTOR: Moving new result history before generation!"
        mv -f "$ALLURE_REPORT_HISTORY" "$PYTEST_RESULT"
    fi

    # Generate Allure report and open it in the browser
    allure generate "$PYTEST_RESULT" --clean -o "$ALLURE_REPORT_DIR"
}

# Function to add environment properties
add_env_properties() {
  printf "\nEXECUTOR: Adding environment properties file\n"
  {
    echo Server=QA
    echo Pytest.Tag=$PYTEST_TAG
    echo Pytest.Parallel.Execution=$PARALLEL_EXEC
    echo "Pytest.Version=$(pip show pytest | grep Version)"
    echo "Allure.Version=$(pip show allure-pytest | grep Version)"
  } > $PYTEST_RESULT/environment.properties
}

# Function to open Allure report in browser
open_allure_report() {
    printf "\nEXECUTOR: Opening Allure report in browser...\n"
    allure open "$ALLURE_REPORT_DIR"
}


pytest_runner
cleanup_after_pytest
add_env_properties
generate_allure_report
open_allure_report
