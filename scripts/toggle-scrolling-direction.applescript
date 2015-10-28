tell application "System Preferences"
    set current pane to pane "com.apple.preference.mouse"
end tell

tell application "System Events"
    tell process "System Preferences"
        click checkbox 1 of window 1
    end tell
end tell

quit application "System Preferences"
