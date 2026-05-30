#! /usr/bin/env bash
protoc -I=./ --python_out=./ ./enum_example.proto