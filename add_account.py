#!/usr/bin/env python
# encoding: utf-8
import sys
from workflow import Workflow


def main(wf):
    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    account_alias = args[0].split(' ')[0]
    username = args[0].split(' ')[1]
    apikey = ' '.join(args[0].split(' ')[2:])
    wf.settings[account_alias] = username
    wf.save_password(username, apikey)


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
