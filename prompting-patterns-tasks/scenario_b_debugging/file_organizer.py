#!/usr/bin/env python3
"""
File Organizer - Has a Bug to Fix
==================================

This script organizes files by extension into folders.
There's a bug that causes it to fail on some file types.

Practice challenge: Use the "Debugging" prompt pattern to fix the issue
"""

import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, source_dir):
        self.source_dir = Path(source_dir)
        self.organized_count = 0
        
        # File type mappings - this has the bug!
        self.file_categories = {
            'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
            'videos': ['.mp4', '.avi', '.mov', '.wmv'],
            'music': ['.mp3', '.wav', '.aac', '.flac'],
            'archives': ['.zip', '.rar', '.7z', '.tar']
            # Missing 'other' category - this causes the bug!
        }
    
    def get_file_category(self, file_path):
        """Get category for a file based on its extension"""
        extension = file_path.suffix.lower()
        
        for category, extensions in self.file_categories.items():
            if extension in extensions:
                return category
        
        # BUG: This should return 'other' but returns None
        # causing issues when files don't match known extensions
        return None
    
    def create_category_folders(self):
        """Create folders for each category"""
        for category in self.file_categories.keys():
            category_path = self.source_dir / category
            category_path.mkdir(exist_ok=True)
    
    def organize_files(self):
        """Organize files into category folders"""
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Source directory not found: {self.source_dir}")
        
        self.create_category_folders()
        
        # Get all files in source directory
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        
        for file_path in files:
            try:
                category = self.get_file_category(file_path)
                
                # BUG: This will fail when category is None
                destination_folder = self.source_dir / category
                destination_path = destination_folder / file_path.name
                
                # Move the file
                shutil.move(str(file_path), str(destination_path))
                self.organized_count += 1
                print(f"Moved {file_path.name} to {category}/")
                
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")
                continue
        
        print(f"\nOrganized {self.organized_count} files")

def create_test_files(test_dir):
    """Create test files to organize"""
    test_path = Path(test_dir)
    test_path.mkdir(exist_ok=True)
    
    # Create test files
    test_files = [
        'photo.jpg',
        'document.pdf', 
        'music.mp3',
        'video.mp4',
        'archive.zip',
        'script.py',      # This will cause the bug!
        'config.ini',     # This will also cause the bug!
        'readme.md'       # And this one too!
    ]
    
    for filename in test_files:
        file_path = test_path / filename
        file_path.write_text(f"Test content for {filename}")
    
    print(f"Created test files in {test_dir}")

def main():
    test_directory = "test_files"
    
    print("File Organizer - Testing Version")
    print("=" * 40)
    
    # Create test files
    create_test_files(test_directory)
    
    # Try to organize them (this will trigger the bug)
    organizer = FileOrganizer(test_directory)
    
    print(f"\nOrganizing files in {test_directory}...")
    organizer.organize_files()

if __name__ == "__main__":
    main() 
