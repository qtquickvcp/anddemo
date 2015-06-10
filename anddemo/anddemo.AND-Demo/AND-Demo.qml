import QtQuick 2.0
import QtQuick.Controls 1.1
import QtQuick.Layouts 1.1
import Machinekit.Controls 1.0
import Machinekit.HalRemote.Controls 1.0
import Machinekit.HalRemote 1.0

HalApplicationWindow {
    id: main

    name: "anddemo"
    title: qsTr("AND-Demo")

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        Item {
            Layout.fillHeight: true
        }
        HalButton {
            Layout.alignment: Layout.Center
            name: "button0"
            text: "Button 0"
            checkable: true
        }
        HalButton {
            Layout.alignment: Layout.Center
            name: "button1"
            text: "Button 1"
        }
        HalLed {
            Layout.alignment: Layout.Center
            name: "led"
        }
        Label {
            Layout.fillWidth: true
            text: "The buttons are connected using the 'and2' component in HAL.\n" +
                  "The LED represents the output of the 'and2' component."
            horizontalAlignment: Text.AlignHCenter
            wrapMode: Text.WordWrap
        }
        Item {
            Layout.fillHeight: true
        }
    }
}

