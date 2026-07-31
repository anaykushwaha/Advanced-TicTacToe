# animations.py 
# Provides simple animation utilities used by the Tkinter interface 

# Animations are intentionally lightweight to keep the application responsive 
# while improving the overall user experience 

from tkinter import Button

from ui.theme import (
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    WIN_HIGHLIGHT_COLOR,
)


class AnimationManager: 
    # Provides reusable animation helpers 

    @staticmethod
    def add_hover_effect(button, Button) -> None: 
        # Adds a hover effect to a Tkinter button 
        
        def on_enter(event):

            button.configure(
                background=BUTTON_HOVER_COLOR,
            )

        def on_leave(event):

            button.configure(
                background=BUTTON_COLOR,
            )

        button.bind(
            "<Enter>",
            on_enter,
        )

        button.bind(
            "<Leave>",
            on_leave,
        )

    @staticmethod
    def flash_winning_cells(
        buttons: list[Button],
        flashes: int = 6,
        delay: int = 180,
    ) -> None: 
        # Flashes the winning buttons 

        def flash(
            count: int,
        ) -> None:

            if count >= flashes:

                for button in buttons:

                    button.configure(
                        background=BUTTON_COLOR,
                    )

                return

            color = (
                WIN_HIGHLIGHT_COLOR
                if count % 2 == 0
                else BUTTON_COLOR
            )

            for button in buttons:

                button.configure(
                    background=color,
                )

            buttons[0].after(
                delay,
                lambda: flash(count + 1),
            )

        flash(0)

    @staticmethod
    def animate_button_press(button: Button) -> None: 
        # Briefly changes the button color when it is pressed 

        button.configure(
            background=BUTTON_HOVER_COLOR,
        )

        button.after(
            100,
            lambda: button.configure(
                background=BUTTON_COLOR,
            ),
        )

    @staticmethod
    def delay(widget, milliseconds: int, callback) -> None: 
        # Executes a callback after a specified delay 
        widget.after(
            milliseconds,
            callback,
        )


__all__ = [
    "AnimationManager",
] 

