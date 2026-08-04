# animations.py
# Provides simple animation utilities used by the Tkinter interface

# Animations are intentionally lightweight to keep the application responsive
# while improving the overall user experience

from collections.abc import Callable

from tkinter import (
    Button,
    Widget,
)

from ui.theme import (
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    WIN_HIGHLIGHT_COLOR,
    ANIMATION_DELAY,
    WIN_FLASH_COUNT,
)


class AnimationManager:
    # Provides reusable animation helpers

    @staticmethod
    def add_hover_effect(
        button: Button,
    ) -> None:
        # Adds a hover effect to a Tkinter button

        def on_enter(
            event,
        ) -> None:

            button.configure(
                background=BUTTON_HOVER_COLOR,
            )

        def on_leave(
            event,
        ) -> None:

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
        flashes: int = WIN_FLASH_COUNT,
        delay: int = ANIMATION_DELAY,
    ) -> None:
        # Flashes the winning buttons

        if not buttons:
            return

        original_colors = [
            button.cget("background")
            for button in buttons
        ]

        def flash(
            count: int,
        ) -> None:

            if count >= flashes:

                for button, color in zip(
                    buttons,
                    original_colors,
                ):

                    button.configure(
                        background=color,
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
                lambda: flash(
                    count + 1,
                ),
            )

        flash(0)

    @staticmethod
    def animate_button_press(
        button: Button,
    ) -> None:
        # Briefly changes the button color when it is pressed

        original_color = button.cget(
            "background",
        )

        button.configure(
            background=BUTTON_HOVER_COLOR,
        )

        button.after(
            ANIMATION_DELAY * 4,
            lambda: button.configure(
                background=original_color,
            ),
        )

    @staticmethod
    def delay(
        widget: Widget,
        milliseconds: int,
        callback: Callable[[], None],
    ) -> None:
        # Executes a callback after a specified delay

        widget.after(
            milliseconds,
            callback,
        )


__all__ = [
    "AnimationManager",
] 

