#!/opt/conda/bin/python3

import argparse
import logging
import os
import sys

def get_logger():
    logger = logging.getLogger("job-tutorial")
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger




def run_job():
    logger = get_logger()
    logger.debug("Start")
    logger.debug("finished")


if __name__ == "__main__":
    run_job()

