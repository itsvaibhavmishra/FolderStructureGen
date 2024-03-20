import os
import sys
import time
import shutil
from colorama import Fore, Style  # Import colorama for cross-platform ANSI color support

def generate_folder_structure():
    clear_terminal()
    print_centered("-=-=-=-=- Folder Structure Generator -=-=-=-=-", Fore.LIGHTCYAN_EX)
    print("\n")
    print_centered("by Vaibhaw Mishra", Fore.LIGHTYELLOW_EX)
    print("\n")
    print_centered("-=-=-=-=- https://github.com/itsvaibhavmishra -=-=-=-=-", Fore.LIGHTCYAN_EX)
    print("\n")

    folder_name = input("Enter name of the folder to generate structure: ")
    if not os.path.exists(folder_name):
        print(f"{Fore.LIGHTRED_EX}Folder not found.{Style.RESET_ALL}")
        return
    
    excluded_items_input = input("Enter folders or files to exclude (comma-separated): ")
    excluded_items = [item.strip() for item in excluded_items_input.split(",")]

    print(f"{Fore.LIGHTBLUE_EX}\nScript started...{Style.RESET_ALL}")
    output_file = f"{folder_name}_structure.md"  # Dynamically generate output filename

    start_time = time.time()

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("## Folder Structure Generator\n")
        f.write("### by [Vaibhaw Mishra](https://github.com/itsvaibhavmishra)\n\n")
        f.write("```\n")

        total_items = count_items(folder_name, excluded_items)
        processed_items = 0
        update_progress_bar(processed_items, total_items)

        f.write(f"{folder_name}/\n")
        processed_items = crawl_folder(folder_name, f, 1, processed_items, total_items, excluded_items)
        
        f.write("```")

    end_time = time.time()
    print(f"\n{Fore.LIGHTBLUE_EX}Script completed in {end_time - start_time:.2f} seconds.{Style.RESET_ALL}")


def count_items(folder_path, exclude_list=None):
    if exclude_list is None:
        exclude_list = []

    count = 0
    for item in os.listdir(folder_path):
        if item not in exclude_list:
            count += 1
            if os.path.isdir(os.path.join(folder_path, item)):
                count += count_items(os.path.join(folder_path, item), exclude_list)
    return count

def crawl_folder(folder_path, output_file, depth, processed_items, total_items, exclude_list=None):
    if exclude_list is None:
        exclude_list = []

    for item in os.listdir(folder_path):
        if item not in exclude_list:
            processed_items += 1
            update_progress_bar(processed_items, total_items)

            if os.path.isdir(os.path.join(folder_path, item)):
                output_file.write("│   " * (depth-1) + "├── " + item + "/\n")
                processed_items = crawl_folder(os.path.join(folder_path, item), output_file, depth + 1, processed_items, total_items, exclude_list)
            else:
                output_file.write("│   " * (depth-1) + "├── " + item + "\n")
    return processed_items

def update_progress_bar(current, total):
    progress = (current / total) * 100 if total != 0 else 100
    bar_length = shutil.get_terminal_size().columns - 10  # Adjust for padding and other elements
    progress_length = int(bar_length * (progress / 100))
    color = interpolate_color(progress)
    bar = color + '=' * progress_length + Style.RESET_ALL + ' ' * (bar_length - progress_length)
    sys.stdout.write('\r[' + bar + f'] {progress:.2f}%')
    sys.stdout.flush()

def interpolate_color(progress):
    # Define color range
    start_color = '#f4ca25'  # Start color: Yellow
    middle_color = '#f45905' # Middle color: Orange
    end_color = '#00FF7F'    # End color: Green

    # Determine color based on progress
    if progress <= 50:
        start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
        middle_rgb = tuple(int(middle_color[i:i+2], 16) for i in (1, 3, 5))
        interpolated_rgb = tuple(int(start + (middle - start) * (progress / 50)) for start, middle in zip(start_rgb, middle_rgb))
    else:
        middle_rgb = tuple(int(middle_color[i:i+2], 16) for i in (1, 3, 5))
        end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
        interpolated_rgb = tuple(int(middle + (end - middle) * ((progress - 50) / 50)) for middle, end in zip(middle_rgb, end_rgb))

    # Convert interpolated RGB to hex
    interpolated_hex = '#' + ''.join(f'{val:02X}' for val in interpolated_rgb)

    # Convert hex to ANSI color escape code
    return f"\033[38;2;{interpolated_rgb[0]};{interpolated_rgb[1]};{interpolated_rgb[2]}m"

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def print_centered(text, color=Fore.WHITE):
    terminal_width = shutil.get_terminal_size().columns
    padding = (terminal_width - len(text)) // 2
    print(f"{color}{' ' * padding}{text}{Style.RESET_ALL}")

# Example usage:
generate_folder_structure()
