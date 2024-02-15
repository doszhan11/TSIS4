import json

str_json = """{
    "totalCount": "400",
    "imdata": [
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/33]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/33",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/34]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/34",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        },
        {
            "l1PhysIf": {
                "attributes": {
                    "adminSt": "up",
                    "autoNeg": "on",
                    "brkoutMap": "none",
                    "bw": "0",
                    "childAction": "",
                    "delay": "1",
                    "descr": "",
                    "dn": "topology/pod-1/node-201/sys/phys-[eth1/35]",
                    "dot1qEtherType": "0x8100",
                    "ethpmCfgFailedBmp": "",
                    "ethpmCfgFailedTs": "00:00:00:00.000",
                    "ethpmCfgState": "0",
                    "fecMode": "inherit",
                    "id": "eth1/35",
                    "inhBw": "unspecified",
                    "layer": "Layer3",
                    "lcOwn": "local",
                    "linkDebounce": "100",
                    "linkLog": "default",
                    "mdix": "auto",
                    "medium": "broadcast",
                    "modTs": "2016-11-28T16:03:29.317-05:00",
                    "mode": "trunk",
                    "monPolDn": "uni/fabric/monfab-default",
                    "mtu": "9150",
                    "name": "",
                    "pathSDescr": "",
                    "portT": "fab",
                    "prioFlowCtrl": "auto",
                    "qiqL2ProtTunMask": "",
                    "routerMac": "not-applicable",
                    "snmpTrapSt": "enable",
                    "spanMode": "not-a-span-dest",
                    "speed": "inherit",
                    "status": "",
                    "switchingSt": "disabled",
                    "trunkLog": "default",
                    "usage": "fabric,fabric-ext"
                }
            }
        }
    ]
}"""

data = json.loads(str_json)

faces = data["imdata"]

for interface in faces:
    attributes = interface["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes.get("mtu", "")

    print("{:<40} {:<20} {:<20} {:<10}".format(dn, description, speed, mtu))
