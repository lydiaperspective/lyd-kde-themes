import QtQuick

Rectangle {
    id: root

    color: "#170F22"
    opacity: 1.0

    // Plasma advances the splash stage while the desktop starts.
    // Fade the artwork away when the workspace is ready.
    property int stage: 0

    Behavior on opacity {
        NumberAnimation {
            duration: 450
            easing.type: Easing.OutCubic
        }
    }

    onStageChanged: {
        if (stage >= 2) {
            opacity = 0.0
        }
    }

    Image {
        id: moonGlow
        anchors.centerIn: parent
        width: Math.min(root.width, root.height) * 0.49
        height: width
        source: "images/moon-glow.svg"
        fillMode: Image.PreserveAspectFit
        smooth: true
    }

    Image {
        id: crescent
        anchors.centerIn: parent
        width: Math.min(root.width, root.height) * 0.34
        height: width
        source: "images/crescent-moon.svg"
        fillMode: Image.PreserveAspectFit
        smooth: true
    }

    // The star follows one open, curved sweep above the crescent.
    // No orbit line or circular path is drawn.
    Path {
        id: starPath

        startX: root.width * 0.19
        startY: root.height * 0.37 - shootingStar.height / 2

        PathCubic {
            x: root.width * 0.81
            y: root.height * 0.37
            control1X: root.width * 0.34
            control1Y: root.height * 0.10
            control2X: root.width * 0.66
            control2Y: root.height * 0.10
        }
    }

    Image {
        id: shootingStar
        width: Math.min(root.width, root.height) * 0.19
        height: width * 0.42
        source: "images/shooting-star.svg"
        fillMode: Image.PreserveAspectFit
        smooth: true
        x: starPath.startX
        y: starPath.startY
        opacity: 0.0
    }

    SequentialAnimation {
        running: true
        loops: Animation.Infinite

        NumberAnimation {
            target: shootingStar
            property: "opacity"
            from: 0.0
            to: 1.0
            duration: 250
        }

        PathAnimation {
            target: shootingStar
            path: starPath
            duration: 3000
            easing.type: Easing.InOutSine
        }

        NumberAnimation {
            target: shootingStar
            property: "opacity"
            from: 1.0
            to: 0.0
            duration: 350
        }

        PropertyAction {
            target: shootingStar
            property: "x"
            value: starPath.startX
        }

        PropertyAction {
            target: shootingStar
            property: "y"
            value: starPath.startY
        }

        PauseAnimation {
            duration: 450
        }
    }

    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.top: crescent.bottom
        anchors.topMargin: Math.min(root.height, root.width) * 0.055
        text: "LYD ARK"
        color: "#E9E1D5"
        font.family: "Noto Sans"
        font.pixelSize: Math.max(12, Math.min(root.width, root.height) * 0.018)
        font.letterSpacing: 5
        font.weight: Font.Medium
        opacity: 0.88
    }
}
