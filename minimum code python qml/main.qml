 import QtQuick 2.12
import QtQuick.Window 2.13
import QtQuick.Controls 2.0
import QtQuick.Controls.Styles 1.4
import QtQuick.Extras 1.4
import QtQuick.Extras.Private 1.0


Window {
	id : root
	width: 400
	maximumWidth : width
	minimumWidth : width
    height: 400
	maximumHeight : height
	minimumHeight : height
	title:"membuat windows"
	color : "grey"
    visible: true
    flags: Qt.Dialog
	
	Button {
		id: button1
		x :100
		y :200
		text: "button1"
		
		palette {
        button: "#00FF00"
		buttonText: "black"
		}
		
		onClicked:{
			backend.button("pressed")
		}
		
	}
	
	
	Text {
					id:text1
					x:90
					y:10
					font.family: "Times New Roman"
					font.pointSize: 14
					color: "white"
				}
	
	
	 Timer {
                id: guitimer
                repeat: true
				interval: 100
                running: true
                onTriggered: {
				text1.text = backend.text()
				}
				
				}
				
				
}













