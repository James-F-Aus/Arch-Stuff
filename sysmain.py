from sysmain_menu import *
from commands import *
import subprocess, os, sys

def run_cmd(cmd: list[str]):
    return subprocess.run(cmd, text=True)

def up_choice(x):
    try:
        os.system("clear")
        result = run_cmd(upgrade_commands[x])
        print(result.stdout)
    except subprocess.CalledProcessError as exc:
        # Why: ensures you see terminal error output instead of silent failures
        print("Command failed:", exc.stderr)

def main_choice(x):
    try:
        os.system("clear")
        result = run_cmd(maintenence_commands[x])
        print(result.stdout)
    except subprocess.CalledProcessError as exc:
        # Why: ensures you see terminal error output instead of silent failures
        print("Command failed:", exc.stderr)

def del_orphans_safe():
        
        #Safely handles the two-step removal of orphaned packages.
        #1. Gets the list of orphans.
        #2. Runs pacman to remove them.
        
    print("\n--- Starting safe removal of orphaned packages ---\n")
    try:
        # Step 1: Get the list of orphaned packages
        print("1/2: Checking for orphaned packages...")
        
        # We need the output of this command, so capture_output=True and check=False initially
        orphan_list_cmd = ["pacman", "-Qtdq"]
        result = subprocess.run(orphan_list_cmd, capture_output=True, text=True, check=False)
        
        # The list of packages is in stdout, split by newline
        orphaned_packages = result.stdout.split()

        if not orphaned_packages:
            print("No orphaned packages found. Nothing to remove.")
            return

        # Step 2: Remove the packages if found
        print(f"2/2: Found {len(orphaned_packages)} orphans. Removing...")
        
        # Build the final removal command
        removal_cmd = ["sudo", "pacman", "-Rns"] + orphaned_packages
        
        # Run the removal command, allowing interactive streaming
        subprocess.run(
            removal_cmd,
            check=True,
            capture_output=False, # Stream output for password prompt/confirmation
            text=True,
            stdin=sys.stdin,
        )
        print("\n--- Orphaned package removal complete ---\n")
    except subprocess.CalledProcessError as exc:
        # Check failed usually means a pacman error (e.g., failed dependency check)
        print(f"\n--- Removal Failed: Pacman error code {exc.returncode} ---")
        if exc.stderr:
            print("Pacman Error Details:", exc.stderr)
    except FileNotFoundError:
        print("\n--- Error: pacman command not found. ---")
    except Exception as e:
        print(f"\n--- An unexpected error occurred during orphan removal: {e} ---")


while True:
    os.system("clear")
    print(logo)
    print(intro)
    print(options)

    choice = input("Choose task:  ")

    if choice == "1":
        up_choice("aur_update")

    elif choice == "2":
        up_choice("sys_update")

    elif choice == "3":
        up_choice("check_logs")

    elif choice == "4":
        up_choice("fastfetch")

    elif choice == "5":
        main_choice("delete_cache_pkg")

    elif choice == "6":
        main_choice("del_aur_cache")

    elif choice == "7":
        del_orphans_safe()

    elif choice == "8":
        main_choice("clear_logs")
        
    elif choice == "9":
        main_choice("update_mirrors")

    elif choice == "10":
        main_choice("check_cache")
    
    elif choice == "11":
        main_choice("del_cache")        

    elif choice == "E" or choice == "e":
        os.system("clear")
        sys.exit()

    next = input("Press Any Key to Continue")