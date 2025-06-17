"""
CP1404/CP5632 Practical
Kivy_layout

function main
    create kivydemo instance
    run the app

class kivydemo (inherits from app)
    property: status_text ← "hello. click the buttons :)"

    function __init__
        call superclass initializer
        set counter ← 0
        set names ← ["lindsay", "osmond", "paul"]

    function build
        set app title to "hello world!"
        load interface from 'kivy_layout.kv'
        for each name in names:
            create button with text = name
            bind button press to function handle_name_button
            add button to names_box in layout
        return root widget

    function handle_name_button(instance)
        print "hello" and instance.text

    function handle_press(amount)
        add amount to counter
        update status_text to "the count is: {counter}"
"""
