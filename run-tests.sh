#!/usr/bin/env bash
set -e

SELENIUM_REMOTE_URL=${SELENIUM_REMOTE_URL:-http://localhost:4444/wd/hub}
export SELENIUM_REMOTE_URL

mkdir -p reports

pytest script/test_xyz_home.py \
  --html=reports/report.html \
  --self-contained-html \
  --maxfail=1 --disable-warnings -v
