#!/bin/bash
FILE_ID=1ApjDhGjtqfFEMzm6dmyhS-2aXnnYLxnj
FILE_NAME=scene.tar
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${FILE_ID}" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=${FILE_ID}" -o ${FILE_NAME}
