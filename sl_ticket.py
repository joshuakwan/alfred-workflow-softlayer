#!/usr/bin/env python
# encoding: utf-8
import sys
from workflow import Workflow
import SoftLayer

def main(wf):
    # Get args from Workflow as normalized Unicode
    args = wf.args

    # Do stuff here ...
    account_alias = args[0].split(' ')[0]
    username = wf.settings.get(account_alias)
    apikey = wf.get_password(username)
    sl_client = SoftLayer.create_client_from_env(username=username, api_key=apikey)

    ticket_id = ' '.join(args[0].split(' ')[1:])
    updates = sl_client['Ticket'].getUpdates(id=ticket_id)

    updates.reverse()
    for update in updates:
        wf.add_item(title=update['entry'],
                    subtitle='%s: %s (%s)%s' % (update['createDate'], update['ticketId'], update['editorType'], update['editorId']),
                    arg="Update on %s:\n %s" % (update['createDate'], update['entry']),
                    valid=True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
