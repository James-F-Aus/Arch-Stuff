import os

upgrade_commands = {
    "fastfetch": ["fastfetch"],
    "sys_update": ["sudo", "pacman", "-Syu"],
    "aur_update": ["yay", "-Syu"],
    "check_logs": ["sudo", "journalctl", "-p", "3", "-xb"],
}
maintenence_commands = {
    "delete_cache_pkg": ["sudo", "pacman", "-Sc"],
    "del_aur_cache": ["yay", "-Sc"],
    "del_orphans": ["sudo", "pacman", "-Rns", "$(pacman -Qtdq)"],
    "clear_logs": ["sudo", "journalctl", "--vacuum-time=2weeks"],
    "update_mirrors": ["sudo", "reflector", "--country", "AU", "-a", "6", "--sort rate", "--save", "/etc/pacman.d/mirrorlist"],
    "check_cache": ["sudo", "-du", "-sh", "~/.cache/"],
    "del_cache": ["rm", "-rf", os.path.expanduser("~/.cache/*")],

}
