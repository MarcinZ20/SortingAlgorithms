from re import M
import tkinter as tk
from tkinter.font import Font
import specs


def createRoot() -> tk.Tk:

    root = tk.Tk(screenName="Main screen")
    root.geometry("1200x600")
    root.title("Sorting Algorithms Visualiser")

    return root


def welcomeScreen(root: tk.Tk) -> tk.Frame:

    fr_welcome_screen = tk.Frame(
        root, background=specs.colors["background_color"])
    fr_welcome_screen.pack(fill=tk.BOTH, expand=True)

    # Components
    label_title = tk.Label(fr_welcome_screen, text="Sorting Algorithms Visualiser",
                           fg=specs.colors["purple"], background=specs.colors["background_color"], pady=40, font=Font(fr_welcome_screen, specs.fonts["title_font"]))

    label_footer = tk.Label(
        root, text="Created and Developed\nby Marcin Zub", fg=specs.colors["dark_sea"], padx=10, pady=10, bg=specs.colors["background_color"], font=Font(fr_welcome_screen, specs.fonts["footer_font"]))

    button_start = tk.Button(fr_welcome_screen, text="START", width=30, pady=20,
                             bg=specs.colors["light_yellow"], fg=specs.colors["purple"], border=2, font=Font(fr_welcome_screen, specs.fonts["button_font"]))

    button_start.configure(activebackground=specs.colors["peach"],
                           activeforeground=specs.colors["purple"])

    label_title.pack(side="top", fill=tk.X)
    button_start.pack(anchor="center")
    label_footer.pack(side="bottom", fill=tk.X)

    return fr_welcome_screen
