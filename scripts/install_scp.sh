#!/bin/bash
set -eo pipefail
# Define the path to the destination directory
destination_dir="../ostis-web-platform/scp-machine"
destination_dir2="../ostis-web-platform/ims.ostis.kb"

# Clone the SCP-Machine repository into the destination directory
git clone https://github.com/ostis-ai/scp-machine.git "$destination_dir"

git clone https://github.com/ostis-dev/ims.ostis.kb.git "$destination_dir2"
