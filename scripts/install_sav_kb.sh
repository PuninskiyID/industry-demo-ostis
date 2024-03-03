#!/usr/bin/env bash
set -eo pipefail

source "$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)/set_vars_sav.sh"

echo ${HUTOROK_PATH}

if [ -z "${HUTOROK_PATH}" ]
  then
    echo "HUTOROK_PATH is not specified, add this var to " "$(cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd)/set_vars_sav.sh"
    exit 1
fi

install_kb_module() {
  git clone "$1" --branch "$2" --single-branch "$3" --recursive
  if [ -n "$4" ]
    then
      cd "$3"
      git checkout "$4"
  fi
}

install_kb_module ${HUTOROK_REPO} ${HUTOROK_BRANCH} ${HUTOROK_PATH} ${HUTOROK_COMMIT}
install_kb_module ${S88_REPO} ${S88_BRANCH} ${S88_PATH} ${S88_COMMIT}
install_kb_module ${isa51_REPO} ${isa51_BRANCH} ${isa51_PATH} ${isa51_COMMIT}
