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

export S88_REPO="https://github.com/PuninskiyID/s88-ostis.git"
export S88_BRANCH="master"
export S88_COMMIT=""
export S88_PATH="${APP_ROOT_PATH}/kb/s88"

export isa51_REPO="https://github.com/Danshicu/isa-5.1-ostis.git"
export isa51_BRANCH="master"
export isa51_COMMIT=""
export isa51_PATH="${APP_ROOT_PATH}/kb/isa51"

