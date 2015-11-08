"""
github-setup-irc-notifications - Configure all repositories in an organization
with irc notifications
"""

import argparse
import getpass

import github3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username'),
    parser.add_argument('--password'),
    args = parser.parse_args()

    if args.password is None:
        password = getpass.getpass(
            'Password for github user "{}":'.format(args.username))
    else:
        password = args.password

    github = github3.login(args.username, password=password)

    if github is None:
        print('Failed to sign into github')
