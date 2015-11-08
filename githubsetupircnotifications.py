"""
github-setup-irc-notifications - Configure all repositories in an organization
with irc notifications
"""

import argparse

import github3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username'),
    parser.add_argument('--password'),
    args = parser.parse_args()
