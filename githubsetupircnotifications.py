"""
github-setup-irc-notifications - Configure all repositories in an organization
with irc notifications
"""

import argparse
import getpass
import sys

import github3


def error(message):
    print(message)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username', help='github username')
    parser.add_argument('--password', help='password for github user')
    parser.add_argument('organization', help='organization containing the '
                                             'repositories to add '
                                             'notifications to')
    parser.add_argument('channel', help='irc channel to send notifications to')
    args = parser.parse_args()

    if args.password is None:
        password = getpass.getpass(
            'Password for github user "{}":'.format(args.username))
    else:
        password = args.password

    github = github3.login(args.username, password=password)

    if github is None:
        error('Failed to sign into github')

    org = github.organization(args.organization)

    if org is None:
        error('Organization "{}" does not appear to exist'.format(args.org))

    conf = {'nickserv_password': '',
            'no_colors': '0',
            'password': '',
            'branch_regexes': '',
            'room': args.channel,
            'ssl': '0',
            'port': '',
            'branches': '',
            'server': 'chat.freenode.net',
            'long_url': '0',
            'notice': '0',
            'message_without_join': '1',
            'nick': 'github'
    }

    events = [
        'push',
        'delete',
        'create',
        'issues',
        'pull_request'
    ]

    for r in org.iter_repos():
        r.create_hook('irc', conf, events=events)
