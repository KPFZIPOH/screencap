# Title: Enhanced Screenshot Capture Script
# Description: Captures a screenshot and saves it with a timestamped filename
# Author: KPFZIPOH
# Created: June 6, 2025
# Requirements: pyautogui, datetime, os

import pyautogui
import datetime
import os
from pathlib import Path

def capture_screenshot(save_dir="C:/temp"):
    """
    Captures a screenshot and saves it to the specified directory with a timestamped filename.
    
    Args:
        save_dir (str): Directory path where the screenshot will be saved
        
    Returns:
        str: Path to the saved screenshot file or None if failed
    """
    try:
        # Ensure the save directory exists, create it if it doesn't
        os.makedirs(save_dir, exist_ok=True)
        
        # Generate timestamp for filename in format YYYY_MM_DD_HH_MM_SS
        timestamp = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        
        # Construct full file path with timestamp
        filepath = os.path.join(save_dir, f"screencap_{timestamp}.png")
        
        # Configure pyautogui settings
        pyautogui.FAILSAFE = True  # Move mouse to upper-left corner to abort
        pyautogui.PAUSE = 0.5     # Add small pause after each pyautogui call
        
        # Capture screenshot
        screenshot = pyautogui.screenshot()
        
        # Save screenshot as PNG
        screenshot.save(filepath)
        
        # Verify file was created
        if Path(filepath).exists():
            print(f"Screenshot saved successfully to: {filepath}")
            return filepath
        else:
            print("Error: Screenshot file was not created")
            return None
            
    except Exception as e:
        # Handle any errors during screenshot capture or saving
        print(f"Error capturing screenshot: {str(e)}")
        return None

def main():
    """
    Main function to execute the screenshot capture.
    """
    # Define default save directory
    default_save_dir = "C:/temp"
    
    # Call screenshot capture function
    result = capture_screenshot(default_save_dir)
    
    # Check if screenshot was successful
    if result:
        print("Screenshot capture completed successfully")
    else:
        print("Screenshot capture failed")

if __name__ == "__main__":
    # Execute main function when script is run directly
    main()
