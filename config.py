from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

super = "mod4"
terminal = guess_terminal()

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
        [super, "control", "shift"],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    #
    # Toggle floating on the focused window
    #
    Key(
        [super, "control", "shift"],
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
]

groups = [
    Group(
        "1",
        label="",
    ),
    Group(
        "2",
        label="",
        layout="max",
        exclusive=True,
        matches=[Match(wm_class="firefox")],
    ),
    Group(
        "3",
        label="",
        layout="max",
        exclusive=True,
        matches=[Match(wm_class="music")],
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
    layout.Max(),
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
]

widget_defaults = dict(
    font="sans",
    fontsize=10,
    padding=2,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(highlight_method="text"),
                widget.Spacer(),
                widget.Prompt(),
                widget.Clock(format="%A %d/%m/%Y %I:%M:%S %p"),
            ],
            16,
            margin=1,
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
