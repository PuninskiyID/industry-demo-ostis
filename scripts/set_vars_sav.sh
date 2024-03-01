#!/usr/bin/env bash
set -eo pipefail

ROOT_PATH=$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && cd .. && pwd)

export APP_ROOT_PATH="${ROOT_PATH}"
export ROOT_CMAKE_PATH="${APP_ROOT_PATH}"
export CONFIG_PATH="${APP_ROOT_PATH}/ostis-example-app.ini"
export REPO_PATH="${APP_ROOT_PATH}/repo.path"

export HUTOROK_REPO="https://github.com/PuninskiyID/khutorok-ostis.git"
export HUTOROK_BRANCH="main"
export HUTOROK_COMMIT=""
export HUTOROK_PATH="${APP_ROOT_PATH}/kb/hutorok"
