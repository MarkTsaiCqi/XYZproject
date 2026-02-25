#!/usr/bin/env bash
set -e

SELENIUM_REMOTE_URL=${SELENIUM_REMOTE_URL:-http://localhost:4444/wd/hub}
export SELENIUM_REMOTE_URL

mkdir -p reports

pytest script/test_xyz_home.py script/test_xyz_login_email.py script/test_google_login_mobile.py \
  --html=reports/report.html \
  --disable-warnings -v
