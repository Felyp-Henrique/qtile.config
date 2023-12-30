import os
import time
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

super = "mod4"
terminal = guess_terminal()


@hook.subscribe.startup_once
def hook_start_picom():
    """
    Start the picom process
    """
    try:
        rc = os.path.expanduser("~/.config/qtile/qtilerc")
        time.sleep(2)
        qtile.cmd_spawn(rc)
    except:
        pass


keys = [
    #
    # Move window focus to any other
    #
    Key(
        [super],
        "space",
        lazy.layout.next(),
        desc="Move window focus to other window",
    ),
    #
    # Toggle fullscreen on the focused window
    #
    Key(
        [super, "control"],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    #
    # Toggle floating on the focused window
    #
    Key(
        [super, "control"],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    #
    # Reload the config
    #
    Key(
        [super, "control"],
        "r",
        lazy.reload_config(),
        desc="Reload the config",
    ),
    #
    # Shutdown Qtile
    #
    Key(
        [super, "control"],
        "q",
        lazy.shutdown(),
        desc="Shutdown Qtile",
    ),
    #
    # Spawn a command using a prompt widget
    #
    Key(
        [super],
        "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget",
    ),
    #
    # Spawn WezTerm
    #
    Key(
        [super],
        "Return",
        lazy.spawn("/usr/bin/wezterm"),
        desc="Spawn WezTerm",
    ),
    #
    # Toggle between layouts
    #
    Key(
        [super],
        "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts",
    ),
    #
    # Volume UP
    #
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ),
    #
    # Volume DOWN
    #
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ),
]

groups = [
    Group(
        "1",
        label="",
        layout="max",
    ),
    Group(
        "2",
        label="",
        layout="max",
    ),
    Group(
        "3",
        label="",
        layout="max",
        exclusive=True,
        matches=[Match(wm_class="firefox")],
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [super],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Max(
        margin=3,
    ),
    layout.Columns(
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=1,
        margin=3,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=8,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        wallpaper="~/.config/qtile/wallpaper.jpg",
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.GroupBox(
                    highlight_method="text",
                    active="#2e3440",
                    inactive="#2e3440",
                    foreground="#2e3440",
                    block_highlight_text_color="#4c566a",
                    this_current_screen_border="#4c566a",
                    disable_drag=True,
                ),
                widget.Spacer(),
                widget.Prompt(),
                widget.Clock(
                    format="%d/%m/%Y %I:%M:%S",
                    foreground="#2e3440",
                ),
            ],
            20,
            margin=3,
            background=["#00000000"],
        ),
    ),
]

#
# Drag floating layouts.
#
mouse = [
    #
    # Move focused float window
    #
    Drag(
        [super],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    #
    # Change focused float window's size
    #
    Drag(
        [super],
        "Button3",
        lazy.window.set_size_floating(),
        start=lazy.window.get_size(),
    ),
    #
    # Bring to front
    #
    Click(
        [super],
        "Button2",
        lazy.window.bring_to_front(),
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
