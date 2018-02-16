#!/usr/bin/env python

import os
import sys
import logging
import pandas as pd
from celery_connectors.utils import get_percent_done
from network_pipeline.log.setup_logging import setup_logging


setup_logging(
    default_path="log/console.json")
name = "describe-training-data"
log = logging.getLogger(name)


version = 1

path_to_training = "./v{}/webapps/react-redux/training-ready".format(
    version)
training_file = "{}/v{}_react_cleaned.csv".format(
    path_to_training,
    version)

if len(sys.argv) > 1:
    training_file = str(sys.argv[1])

if not os.path.exists(training_file):
    log.error(("Missing file={} stopping")
              .format(
                    training_file))
    sys.exit(1)

log.info(("loading training dataset={}")
         .format(
             training_file))

df = pd.read_csv(
        training_file,
        encoding="UTF-8")

if len(df.index) == 0:
    log.error(("No rows={} found in training dataset={}")
              .format(
                len(df.index),
                training_file))
    sys.exit(2)
if len(df.columns.values) == 0:
    log.error(("No columns={} found in training dataset={}")
              .format(
                len(df.columns.values),
                training_file))
    sys.exit(3)

log.info(("found rows={} columns={} in dataset={}")
         .format(
            len(df.index),
            len(df.columns.values),
            training_file))

ATTACK_VALUE = 1
NON_ATTACK_VALUE = 0
filter_num_attacks = (df["label_value"] == ATTACK_VALUE)
filter_num_nonattacks = (df["label_value"] == NON_ATTACK_VALUE)
df_attacks = df[filter_num_attacks]
df_nonattacks = df[filter_num_nonattacks]

num_attacks = len(df_attacks.index)
num_nonattacks = len(df_nonattacks.index)

total_records = len(df.index)

percent_attack = get_percent_done(num_attacks, total_records)
percent_nonattack = get_percent_done(num_nonattacks, total_records)

log.info(("total records={} attack={} nonattack={} "
          "percent_attack={}% percent_nonattack={}%")
         .format(
            total_records,
            num_attacks,
            num_nonattacks,
            percent_attack,
            percent_nonattack))

sys.exit(0)
