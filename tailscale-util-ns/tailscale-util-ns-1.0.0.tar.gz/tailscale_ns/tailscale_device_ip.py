import json
import os
import jmespath
import sys


class TailScaleDeviceIp:

    @staticmethod
    def tailscale_path():
        if sys.platform == 'darwin':
            default = '/Applications/Tailscale.app/Contents/MacOS/Tailscale'
        elif sys.platform == 'win32':
            default = 'C:\\Program Files\\Tailscale'
        else:
            raise RuntimeError('Please set `TAILSCALE_PATH` in environment variable. \n '
                               'Example: export TAILSCALE_PATH=/Applications/Tailscale.app/Contents/MacOS/Tailscale')
        return os.getenv('TAILSCALE_PATH', default=default)

    @staticmethod
    def value_at_json_path(json, path):
        expression = jmespath.compile(path)
        return expression.search(json)

    @staticmethod
    def get_device_details():
        command = f"{TailScaleDeviceIp.tailscale_path()} status --json"
        output = os.popen(command).read()
        return json.loads(output)

    @staticmethod
    def get_ip_for_all_devices():
        results = TailScaleDeviceIp.get_device_details()
        jpath = "Peer.*.{device: HostName,ip: TailscaleIPs[0]}]"
        return TailScaleDeviceIp.value_at_json_path(results, jpath)

    @staticmethod
    def get_ip_for_device(device_name: str):
        results = TailScaleDeviceIp.get_device_details()
        jpath = "Peer.{device:*}.device[?HostName==`" + device_name + "`].TailscaleIPs | [0] | [0]"
        return TailScaleDeviceIp.value_at_json_path(results, jpath)
