"""
github-setup-irc-notifications - Configure all repositories in an organization
with irc notifications
"""

import argparse
import getpass
import sys

import github3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username')
    parser.add_argument('--password')
    parser.add_argument('--org')
    args = parser.parse_args()

    if args.password is None:
        password = getpass.getpass(
            'Password for github user "{}":'.format(args.username))
    else:
        password = args.password

    github = github3.login(args.username, password=password)

    if github is None:
        print('Failed to sign into github')
        sys.exit(1)

    org = github.organization(args.org)

    if org is None:
        print('Organization "{}" does not appear to exist'.format(args.org))
        sys.exit(1)
