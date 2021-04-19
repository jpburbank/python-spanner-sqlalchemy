# Copyright 2021 Google LLC
#
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file or at
# https://developers.google.com/open-source/licenses/bsd

import argparse

from sqlalchemy import create_engine


def enable_autocommit_mode(url):
    """Enables autocommit mode."""
    # [START sqlalchemy_spanner_autocmmit_on]

    conn = create_engine(url).connect()
    level = conn.get_isolation_level()

    print("Connection autocommit default mode is {}".format(level))
    print("Spanner DBAPI default autocommit mode is {}".format(conn.connection.connection.autocommit))

    conn.execution_options(isolation_level="AUTOCOMMIT")
    print("Connection autocommit mode is {}".format(level))
    print("Spanner DBAPI autocommit mode is {}".format(conn.connection.connection.autocommit))

    # [END sqlalchemy_spanner_autocmmit_on]
    return conn


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("url", help="Your Cloud Spanner url which contains "
                                    "project-id, instance-id, databas-id.")

    subparsers = parser.add_subparsers(dest="command")
    subparsers.add_parser("enable_autocommit_mode", help=enable_autocommit_mode.__doc__)
    args = parser.parse_args()
    if args.command == "enable_autocommit_mode":
        enable_autocommit_mode(args.url)
    else:
        print(f"Command {args.command} did not match expected commands.")
