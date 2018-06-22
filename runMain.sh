#!/usr/bin/env bash
ssh cluster-cn-01 "cd $(pwd); qint $@ runAdvertisementDetection.sh"

