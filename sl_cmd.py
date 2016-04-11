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

    command = ' '.join(args[0].split(' ')[1:])

    if command == 'list':
        sl_client = SoftLayer.create_client_from_env(username=username, api_key=apikey)
        hw_mgr = SoftLayer.HardwareManager(sl_client)
        for hw in hw_mgr.list_hardware():
            wf.add_item(title='%s' % hw['fullyQualifiedDomainName'],
                        subtitle='IP: %s/%s, CPU: %s cores, Mem: %s GB, ' % (hw['primaryIpAddress'], hw['primaryBackendIpAddress'], hw['processorPhysicalCoreAmount'], hw['memoryCapacity']),
                        valid=True)
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
