#!/bin/bash
cd /home/kavia/workspace/code-generation/tech-haven-customer-support-bot-1313-1322/tech_haven_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

