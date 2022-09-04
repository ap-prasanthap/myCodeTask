#!/bin/bash

# run pytest website test - step2
echo "Run login tests"
py.test
echo "login tests complete"

allure generate reports/allure-results/ --clean
