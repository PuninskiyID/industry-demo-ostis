#!/usr/bin/env bash
set -eo pipefail

source "$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)/set_vars_sav.sh"

echo ${HUTOROK_PATH}

if [ -z "${HUTOROK_PATH}" ]
  then
    echo "HUTOROK_PATH is not specified, add this var to " "$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)/set_vars_sav.sh"
    exit 1
fi


install_hutorok() {
  git clone "${HUTOROK_REPO}" --branch "${HUTOROK_BRANCH}" --single-branch "${HUTOROK_PATH}" --recursive
  if [ -n "${HUTOROK_COMMIT}" ]
    then
      cd "${HUTOROK_PATH}"
      git checkout "${HUTOROK_COMMIT}"
  fi
}

install_hutorok
