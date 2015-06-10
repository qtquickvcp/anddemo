import QtQuick 2.0
import QtQuick.Controls 1.1
import Machinekit.Application 1.0
import Machinekit.Application.Controls 1.0
import Machinekit.Service 1.0

ApplicationWindow {
    id: applicationWindow

    visible: true
    width: 500
    height: 700
    title: connectionWindow.title

    ConnectionWindow {
        id: connectionWindow

        anchors.fill: parent
        defaultTitle: "anddemo"
        autoSelectInstance: false
        applications: [
            ApplicationDescription {
                sourceDir: "qrc:/anddemo.AND-Demo/"
            }
        ]
        instanceFilter: ServiceDiscoveryFilter{ name: "" }
    }
}


