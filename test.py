"""
Pothole Tracking and Repair System (PHTRS)
Interactive Python Application
"""

from datetime import datetime
from typing import Dict, List


class Pothole:
    """Represents a pothole report in the system."""
    next_id = 1
    
    def __init__(self, street_address, size, location, district, citizen_name="Anonymous"):
        self.id = f"POT-{Pothole.next_id:05d}"
        Pothole.next_id += 1
        self.citizen_name = citizen_name
        self.street_address = street_address
        self.size = size
        self.location = location
        self.district = district
        self.priority = self._calculate_priority()
        self.status = "Reported"
        self.reported_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.work_order = None
        
    def _calculate_priority(self):
        """Calculate repair priority based on size (1-10 scale)."""
        if self.size >= 9:
            return "CRITICAL"
        elif self.size >= 7:
            return "HIGH"
        elif self.size >= 5:
            return "MEDIUM"
        elif self.size >= 3:
            return "LOW"
        else:
            return "MINOR"
    
    def __str__(self):
        return (f"ID: {self.id} | Reported by: {self.citizen_name} | Address: {self.street_address} | "
                f"Size: {self.size}/10 | Priority: {self.priority} | Status: {self.status}")


class WorkOrder:
    """Represents a work order for pothole repair."""
    next_crew_id = 1
    
    def __init__(self, pothole_id):
        self.pothole_id = pothole_id
        self.crew_id = f"{WorkOrder.next_crew_id:05d}"
        WorkOrder.next_crew_id += 1
        self.crew_size = 0
        self.equipment = []
        self.hours = 0.0
        self.filler_material = 0.0  # in cubic yards
        self.status = "Not Started"
        self.cost = 0.0
        
    def calculate_cost(self):
        """Calculate total repair cost based on labor, equipment, and materials."""
        labor_cost = self.hours * self.crew_size * 45.00  # $45/hour per person
        equipment_cost = len(self.equipment) * self.hours * 75.00  # $75/hour per equipment
        material_cost = self.filler_material * 120.00  # $120 per cubic yard
        self.cost = labor_cost + equipment_cost + material_cost
        return self.cost
    
    def __str__(self):
        return (f"Crew ID: {self.crew_id} | Pothole: {self.pothole_id} | "
                f"Crew Size: {self.crew_size} | Hours: {self.hours} | "
                f"Status: {self.status} | Cost: ${self.cost:.2f}")


class PHTRS:
    """Main Pothole Tracking and Repair System."""
    
    def __init__(self):
        self.potholes: Dict[str, Pothole] = {}
        self.work_orders: Dict[str, WorkOrder] = {}
        
        # District mapping (simplified)
        self.district_map = {
            "Main": "District 1",
            "Oak": "District 2",
            "Elm": "District 2",
            "Maple": "District 3",
            "Pine": "District 3",
            "Cedar": "District 4",
            "Washington": "District 1",
            "Lincoln": "District 4"
        }
    
    def determine_district(self, street_address):
        """Determine district from street address."""
        for street_name, district in self.district_map.items():
            if street_name.lower() in street_address.lower():
                return district
        return "District 5"  # Default district
    
    def add_pothole(self, street_address, size, location, citizen_name="Anonymous"):
        """Add a new pothole report."""
        district = self.determine_district(street_address)
        pothole = Pothole(street_address, size, location, district, citizen_name)
        self.potholes[pothole.id] = pothole
        return pothole
    
    def add_work_order(self, pothole_id):
        """Create a work order for a pothole."""
        if pothole_id in self.potholes:
            work_order = WorkOrder(pothole_id)
            self.work_orders[pothole_id] = work_order
            self.potholes[pothole_id].work_order = work_order
            self.potholes[pothole_id].status = "Assigned to Crew"
            return work_order
        return None


def citizen_menu(system):
    """Handle citizen interactions."""
    while True:
        print("\nCITIZEN PORTAL")
        print("1. Report a Pothole")
        print("2. Check Status of My Reports")
        print("3. Return to Main Menu")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            report_pothole(system)
        elif choice == "2":
            check_pothole_status(system)
        elif choice == "3":
            break
        else:
            print("Invalid option. Please try again.")


def report_pothole(system):
    """Allow citizen to report a pothole."""
    print("\n" + "-"*80)
    print("REPORT A POTHOLE")
    print("-"*80)
    
    # Get citizen name
    citizen_name = input("Your full name: ").strip()
    if not citizen_name:
        print("Name cannot be empty.")
        return
    
    # Get street address
    street_address = input("Enter street address: ").strip()
    if not street_address:
        print("Address cannot be empty.")
        return
    
    # Get pothole size
    while True:
        try:
            size = int(input("\nEnter pothole size (1-10): ").strip())
            if 1 <= size <= 10:
                break
            else:
                print("Size must be between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Get location
    print("\nPothole Location Options:")
    print("1. Middle of road")
    print("2. Curb")
    print("3. Lane divider")
    print("4. Shoulder")
    print("5. Intersection")
    
    while True:
        try:
            loc_choice = int(input("Select location (1-5): ").strip())
            if 1 <= loc_choice <= 5:
                location_map = {
                    1: "Middle of road",
                    2: "Curb",
                    3: "Lane divider",
                    4: "Shoulder",
                    5: "Intersection"
                }
                location = location_map[loc_choice]
                break
            else:
                print("Please select 1-5.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Create pothole report
    pothole = system.add_pothole(street_address, size, location, citizen_name)
    
    print(f"\nPothole reported successfully. Tracking Number: {pothole.id}")
    print(f"Priority: {pothole.priority}, Status: {pothole.status}")
    
    input("\nPress Enter to continue...")


def check_pothole_status(system):
    """Allow citizen to check status of their reports."""
    print("\n" + "-"*80)
    print("CHECK POTHOLE STATUS")
    print("-"*80)
    
    tracking_number = input("Enter pothole tracking number (e.g., POT-00001): ").strip().upper()
    
    if tracking_number in system.potholes:
        pothole = system.potholes[tracking_number]
        print(f"Status: {pothole.status}, Priority: {pothole.priority}")
        
        if pothole.work_order:
            print(f"Work Order: {pothole.work_order.crew_id}, Status: {pothole.work_order.status}")
        else:
            print("No work order assigned yet.")
        
        input("\nPress Enter to continue...")
    else:
        print(f"No pothole found with tracking number: {tracking_number}")
        input("\nPress Enter to continue...")


def submit_damage_claim(system):
    """Allow citizen to submit a damage claim."""
    print("\n" + "-"*80)
    print("SUBMIT DAMAGE CLAIM")
    print("-"*80)
    
    name = input("Your full name: ").strip()
    address = input("Your address: ").strip()
    phone = input("Your phone number: ").strip()
    
    print("\nType of Damage:")
    print("1. Tire")
    print("2. Alignment")
    print("3. Body/Paint")
    print("4. Suspension")
    print("5. Rim/Wheel")
    print("6. Other")
    
    while True:
        try:
            damage_choice = int(input("Select damage type (1-6): ").strip())
            if 1 <= damage_choice <= 6:
                damage_map = {
                    1: "Tire",
                    2: "Alignment",
                    3: "Body/Paint",
                    4: "Suspension",
                    5: "Rim/Wheel",
                    6: "Other"
                }
                damage_type = damage_map[damage_choice]
                break
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            amount = float(input("Estimated damage amount ($): ").strip())
            if amount >= 0:
                break
            else:
                print("Amount must be positive.")
        except ValueError:
            print("Please enter a valid dollar amount.")
    
    claim = system.add_damage_claim(name, address, phone, damage_type, amount)
    
    print("\n" + "="*80)
    print("DAMAGE CLAIM SUBMITTED SUCCESSFULLY")
    print("="*80)
    print(f"Claim ID: {claim.claim_id}")
    print(f"Status: {claim.status}")
    print(f"Filed: {claim.filed_date}")
def repair_crew_menu(system):
    """Handle repair crew interactions."""
    while True:
        print("\nREPAIR CREW PORTAL")
        print("1. View and Update Work Orders")
        print("2. Return to Main Menu")
        
        choice = input("\nSelect an option (1-2): ").strip()
        
        if choice == "1":
            view_and_update_work_orders(system)
        elif choice == "2":
            break
        else:
            print("Invalid option. Please try again.")


def view_and_update_work_orders(system):
    """Display all work orders and allow selecting one to update."""
    print("\n" + "="*80)
    print("WORK ORDERS")
    print("="*80)
    
    if not system.work_orders:
        print("\nNo work orders currently assigned.")
        print("\nNote: Admins must assign work orders to potholes first.")
        return
    else:
        print("\nAvailable Work Orders:")
        for i, (pothole_id, work_order) in enumerate(system.work_orders.items(), 1):
            pothole = system.potholes[pothole_id]
            print(f"{i}. Pothole ID: {pothole_id} | Address: {pothole.street_address} | Status: {work_order.status}")
        
        while True:
            try:
                choice = int(input(f"\nSelect work order to update (1-{len(system.work_orders)}), or 0 to return: ").strip())
                if choice == 0:
                    break
                elif 1 <= choice <= len(system.work_orders):
                    selected_id = list(system.work_orders.keys())[choice - 1]
                    update_work_order(system, selected_id)
                    break
                else:
                    print("Invalid choice.")
            except ValueError:
                print("Please enter a valid number.")


def update_work_order(system, pothole_id):
    """Allow repair crew to update work order details."""
    print("\n" + "-"*80)
    print("UPDATE WORK ORDER")
    print("-"*80)
    
    work_order = system.work_orders[pothole_id]
    pothole = system.potholes[pothole_id]
    
    print(f"\nUpdating work order for: {pothole_id}")
    print(f"Current Crew ID: {work_order.crew_id}")
    
    # Update crew size
    while True:
        try:
            crew_size = int(input("\nNumber of people on crew: ").strip())
            if crew_size > 0:
                work_order.crew_size = crew_size
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Update equipment
    print("\nEquipment assigned (enter one at a time, type 'done' when finished):")
    work_order.equipment = []
    while True:
        equipment = input("Equipment name (or 'done'): ").strip()
        if equipment.lower() == 'done':
            break
        if equipment:
            work_order.equipment.append(equipment)
    
    # Update hours
    while True:
        try:
            hours = float(input("\nHours applied to repair: ").strip())
            if hours >= 0:
                work_order.hours = hours
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Update status
    print("\nWork Status:")
    print("1. Work in Progress")
    print("2. Repaired")
    print("3. Not Repaired")
    
    while True:
        try:
            status_choice = int(input("Select status (1-3): ").strip())
            if 1 <= status_choice <= 3:
                status_map = {
                    1: "Work in Progress",
                    2: "Repaired",
                    3: "Not Repaired"
                }
                work_order.status = status_map[status_choice]
                pothole.status = status_map[status_choice]
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Update filler material
    while True:
        try:
            filler = float(input("\nAmount of filler material used (cubic yards): ").strip())
            if filler >= 0:
                work_order.filler_material = filler
                break
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate cost
    work_order.calculate_cost()
    
    print(f"Work order updated for {pothole_id}. Status: {work_order.status}, Cost: ${work_order.cost:.2f}")


def admin_menu(system):
    """Handle admin interactions."""
    while True:
        print("\n" + "="*80)
        print("ADMINISTRATOR PORTAL")
        print("="*80)
        print("1. View All Reported Potholes")
        print("2. Assign Work Crew to Pothole")
        print("3. Generate Summary Report")
        print("4. Return to Main Menu")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == "1":
            view_all_potholes(system)
        elif choice == "2":
            assign_work_crew(system)
        elif choice == "3":
            generate_summary_report(system)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.")


def view_all_potholes(system):
    """Display all reported potholes."""
    print("\n" + "="*80)
    print("ALL REPORTED POTHOLES")
    print("="*80)
    
    if not system.potholes:
        print("\nNo potholes currently reported.")
    else:
        # Group by priority
        priority_groups = {"CRITICAL": [], "HIGH": [], "MEDIUM": [], "LOW": [], "MINOR": []}
        
        for pothole in system.potholes.values():
            priority_groups[pothole.priority].append(pothole)
        
        for priority in ["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"]:
            if priority_groups[priority]:
                print(f"\n{priority} PRIORITY:")
                print("-" * 80)
                for pothole in priority_groups[priority]:
                    print(pothole)
    
    print("="*80)


def assign_work_crew(system):
    """Assign a work crew to a pothole."""
    print("\n" + "-"*80)
    print("ASSIGN WORK CREW")
    print("-"*80)
    
    pothole_id = input("Enter pothole ID to assign crew (e.g., POT-00001): ").strip().upper()
    
    if pothole_id not in system.potholes:
        print(f"\nNo pothole found with ID: {pothole_id}")
        return
    
    if pothole_id in system.work_orders:
        print(f"\nWork order already exists for this pothole (Crew ID: {system.work_orders[pothole_id].crew_id})")
        return
    
    pothole = system.potholes[pothole_id]
    work_order = system.add_work_order(pothole_id)
    
    print(f"Work crew assigned to {pothole_id}. Crew ID: {work_order.crew_id}")


def generate_summary_report(system):
    """Generate system summary report."""
    print(f"\nSummary - Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    
    # Pothole statistics
    total_potholes = len(system.potholes)
    priority_counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0, "MINOR": 0}
    status_counts = {}
    
    for pothole in system.potholes.values():
        priority_counts[pothole.priority] += 1
        status_counts[pothole.status] = status_counts.get(pothole.status, 0) + 1
    
    print(f"Total Potholes: {total_potholes}")
    print("By Priority:", end=" ")
    for priority, count in priority_counts.items():
        if count > 0:
            print(f"{priority}: {count}", end=" ")
    print()
    
    print("By Status:", end=" ")
    for status, count in status_counts.items():
        print(f"{status}: {count}", end=" ")
    print()
    
    # Work order statistics
    total_work_orders = len(system.work_orders)
    total_cost = sum(wo.calculate_cost() for wo in system.work_orders.values())
    total_hours = sum(wo.hours for wo in system.work_orders.values())
    
    print(f"Total Work Orders: {total_work_orders}, Hours: {total_hours:.2f}, Cost: ${total_cost:.2f}")


def main():
    """Main function to run the PHTRS system."""
    system = PHTRS()
    
    print("\nWelcome to PHTRS - Pothole Tracking and Repair System")
    
    while True:
        print("\nMAIN MENU")
        print("1. Citizen Portal")
        print("2. Repair Crew Portal")
        print("3. Administrator Portal")
        print("4. Exit System")
        
        choice = input("\nSelect your role (1-4): ").strip()
        
        if choice == "1":
            citizen_menu(system)
        elif choice == "2":
            repair_crew_menu(system)
        elif choice == "3":
            admin_menu(system)
        elif choice == "4":
            print("\nThank you for using PHTRS. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()