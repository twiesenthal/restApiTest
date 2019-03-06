from __future__ import absolute_import
from .__version__ import version
import logging
import argparse
import sys
import os

log = logging.getLogger(__name__)


def get_parser():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='example cli\n\n%s',
        )
    verbosity = parser.add_mutually_exclusive_group(required=False)
    verbosity.add_argument(
        '-v', '--verbose',
        action='count', dest='verbose', default=False,
        help='be more verbose',
        )
    verbosity.add_argument(
        '-q', '--quiet',
        action='count', dest='quiet',
        help='be less verbose',
        )
    parser.add_argument(
        '--version',
        action='version',
        version='%s' % version,
        help='the current installed version of ceph-deploy',
        )
    parser.add_argument(
        '--log-config',
        action='store',
        help='Logfile configuration file, (overrides command line).',
        metavar='LOG_CONFIG'
        )
    parser.add_argument(
        '--task-one',
        action='store',
        help='Create an example config file.',
        metavar='CONFIG_GEN'
        )
    parser.add_argument(
        '--task-two',
        action='store',
        help='Read config file.',
        metavar='CONFIG'
        )
    return parser


def main(argv=None, namespace=None):
    parser = get_parser()
    args = parser.parse_args(argv, namespace)
    logFile = None
    # Set up log file
    LoggingLevel = logging.INFO
    LoggingLevelCounter = 1
    if args.verbose:
        LoggingLevelCounter = LoggingLevelCounter - args.verbose
    if args.quiet:
        LoggingLevelCounter = LoggingLevelCounter + args.quiet
    if LoggingLevelCounter <= 0:
        LoggingLevel = logging.DEBUG
    if LoggingLevelCounter == 1:
        LoggingLevel = logging.INFO
    if LoggingLevelCounter == 2:
        LoggingLevel = logging.WARNING
    if LoggingLevelCounter == 3:
        LoggingLevel = logging.ERROR
    if LoggingLevelCounter == 4:
        LoggingLevel = logging.FATAL
    if LoggingLevelCounter >= 5:
        LoggingLevel = logging.CRITICAL

    if args.log_config:
        logFile = args.log_config
    if logFile is not None:
        if os.path.isfile(logFile):
            logging.config.fileConfig(logFile)
        else:
            logging.basicConfig(level=LoggingLevel)
            log = logging.getLogger("main")
            log.error("Logfile configuration file '%s' was not found." % (args.log_config))
            sys.exit(1)
    else:
        logging.basicConfig(level=LoggingLevel)

    log = logging.getLogger("cli.main")
    actions = set([])
    if args.task_one:
        actions.add('task_one')
    if args.task_two:
        actions.add('task_two')
    print(actions)
