#!/bin/sh

sudo kill -9 $(lsof -t -i:$1)