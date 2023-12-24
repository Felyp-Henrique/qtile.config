from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Key, Group, Match, Mouse, Screen
from libqtile.layout.base import Layout
from libqtile.lazy import lazy

super = "mod4"


def get_keys() -> list[Key]:
    """
    Returns the keys configurations.
    """
    return [
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


def get_mouse() -> list[Mouse]:
    """
    Returns the mouse configuration.
    """
    return []


def get_groups() -> list[Group]:
    """
    Returns the groups configurations.

    Groups:

    - general:
      Here, all tasks is do.
    - music:
      Here, YouTube Music is opened.
    - health:
      Here, the htop command is opened.
    """
    return [Group(group_name) for group_name in "general music health".split()]


def get_layouts() -> list[Layout]:
    """
    Returns the layouts configurations.
    """
    return []


def get_screens() -> list[Screen]:
    """
    Returns the screens configurations.
    """
    return []


#
# Do Qtile configurations
#
keys = get_keys()
layouts = get_layouts()
groups = get_groups()
sreens = get_screens()
widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
wl_input_rules = None
wmname = "LG3D"

#
# Do keys replications between groups
#
for index, group in zip(range(1, len(groups) + 1), groups):
    keys.extend(
        [
            Key(
                [super],
                str(index),
                lazy.groups[group.name].toscreen(),
                desc=f"Switch to group { group.name }",
            ),
        ]
    )
