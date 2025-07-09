#!/usr/bin/env python3
"""
Contact Manager - Messy Code Needing Refactoring
================================================

This contact manager works but the code is a mess!
Everything is in one giant function with no separation of concerns.

Practice Challenge: Use the "Refactoring" prompt pattern to clean this up
"""

import json
import os
from datetime import datetime

def contact_manager():
    """One giant function that does EVERYTHING - needs refactoring!"""
    
    # Hardcoded filename - should be configurable
    contacts_file = "contacts.json"
    
    # Load contacts - no error handling!
    if os.path.exists(contacts_file):
        with open(contacts_file, 'r') as f:
            contacts = json.load(f)
    else:
        contacts = []
    
    print("Contact Manager - Messy Version")
    print("Commands: add, list, search, delete, save, quit")
    
    while True:
        command = input("\nEnter command: ").strip().lower()
        
        if command == "quit":
            # Save before quitting - should be automatic
            with open(contacts_file, 'w') as f:
                json.dump(contacts, f, indent=2)
            break
            
        elif command == "add":
            # Adding contact logic - way too much in one place
            print("Adding new contact:")
            name = input("Name: ").strip()
            
            # Basic validation - but inconsistent
            if not name:
                print("Name cannot be empty")
                continue
                
            phone = input("Phone: ").strip()
            email = input("Email: ").strip()
            address = input("Address: ").strip()
            
            # More validation that should be in a separate function
            if email and "@" not in email:
                print("Invalid email format")
                continue
            
            # Check for duplicates - inefficient search
            duplicate = False
            for contact in contacts:
                if contact['name'].lower() == name.lower():
                    print("Contact already exists!")
                    duplicate = True
                    break
            
            if not duplicate:
                # Creating contact object - should be a class
                new_contact = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'address': address,
                    'created': datetime.now().isoformat(),
                    'updated': datetime.now().isoformat()
                }
                contacts.append(new_contact)
                print(f"Added {name} to contacts")
                
        elif command == "list":
            # List contacts - formatting should be separate
            if not contacts:
                print("No contacts found")
            else:
                print(f"\nFound {len(contacts)} contacts:")
                print("-" * 50)
                for i, contact in enumerate(contacts, 1):
                    print(f"{i}. {contact['name']}")
                    if contact['phone']:
                        print(f"   Phone: {contact['phone']}")
                    if contact['email']:
                        print(f"   Email: {contact['email']}")
                    if contact['address']:
                        print(f"   Address: {contact['address']}")
                    print(f"   Created: {contact['created'][:10]}")
                    print()
                    
        elif command == "search":
            # Search logic - should be its own function
            search_term = input("Search for: ").strip().lower()
            if not search_term:
                print("Search term cannot be empty")
                continue
                
            found = []
            for contact in contacts:
                # Inefficient search through all fields
                if (search_term in contact['name'].lower() or 
                    search_term in contact['phone'].lower() or 
                    search_term in contact['email'].lower() or 
                    search_term in contact['address'].lower()):
                    found.append(contact)
            
            if found:
                print(f"\nFound {len(found)} matching contacts:")
                print("-" * 40)
                for contact in found:
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print()
            else:
                print("No matching contacts found")
                
        elif command == "delete":
            # Delete logic - no confirmation, poor UX
            name_to_delete = input("Enter name to delete: ").strip()
            if not name_to_delete:
                print("Name cannot be empty")
                continue
                
            # Linear search again - inefficient
            deleted = False
            for i, contact in enumerate(contacts):
                if contact['name'].lower() == name_to_delete.lower():
                    contacts.pop(i)
                    print(f"Deleted {contact['name']}")
                    deleted = True
                    break
                    
            if not deleted:
                print("Contact not found")
                
        elif command == "save":
            # Manual save - should be automatic
            try:
                with open(contacts_file, 'w') as f:
                    json.dump(contacts, f, indent=2)
                print("Contacts saved")
            except Exception as e:
                print(f"Error saving contacts: {e}")
                
        else:
            print("Unknown command")

def main():
    """Main function - should handle setup and cleanup"""
    try:
        contact_manager()
    except KeyboardInterrupt:
        print("\nGoodbye!")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 