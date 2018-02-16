#!/usr/bin/env python

import os
import sys
import logging
import pandas as pd
from celery_connectors.utils import get_percent_done
from network_pipeline.log.setup_logging import setup_logging


setup_logging(
    default_path="log/console.json")
name = "find-row-with-string"
log = logging.getLogger(name)


version = 1

path_to_training = "./v{}/webapps/react-redux/training-ready".format(
    version)
training_file = "{}/v{}_react_cleaned.csv".format(
    path_to_training,
    version)
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

find_this = "08:00:27:89:2d:02"

total_records = len(df.index)

ridx = 1

for idx, row in df.iterrows():
    for h in df.columns.values:
        if str(row[h]) == find_this:
            log.info(("found={} row={} column_header={}")
                     .format(
                        find_this,
                        ridx,
                        h))
            sys.exit(0)
            break
    # end of all columns
    perc_done = get_percent_done(
                    ridx,
                    total_records)

    if ridx % 1000 == 0:
        log.info(("done {} - {}/{} rows")
                 .format(
                     perc_done,
                     ridx,
                     total_records))
    ridx += 1
# end of all rows

perc_done = get_percent_done(
                ridx,
                total_records)

log.info(("Done {} - {}/{} rows")
         .format(
            perc_done,
            ridx,
            total_records))


log.info(("Did not find={} in training_data={}")
         .format(
             find_this,
             training_file))

sys.exit(0)
