from ml.ml40.roles.dts.sensors.sensor import Sensor


class WaterLevelFlowSensor(Sensor):
    def __init__(self, namespace="wml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
