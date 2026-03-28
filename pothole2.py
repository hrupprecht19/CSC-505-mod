"""
PHTRS Use Case Diagram Summary Script
Pothole Tracking and Repair System
"""

class Actor:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.use_cases = []
    
    def add_use_case(self, use_case):
        self.use_cases.append(use_case)
    
    def __str__(self):
        return f"{self.name}: {self.description}"

class UseCase:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.relationships = []
    
    def add_relationship(self, relationship_type, target_use_case):
        self.relationships.append((relationship_type, target_use_case))
    
    def __str__(self):
        return f"  - {self.name}: {self.description}"

def main():
    print("=" * 70)
    print("PHTRS - Pothole Tracking and Repair System")
    print("Use Case Diagram Summary")
    print("=" * 70)
    print()
    
    # Define Actors
    citizen = Actor("Citizen", "General public who reports potholes and submits damage claims")
    admin = Actor("Public Works Admin", "Administrative staff managing the system and coordinating repairs")
    crew = Actor("Repair Crew", "Field workers performing pothole repairs and logging work details")
    
    actors = [citizen, admin, crew]
    
    # Define Use Cases
    use_cases = {
        # Citizen use cases
        "Report Pothole": UseCase("Report Pothole", "Submit a new pothole location and details"),
        "Submit Damage Claim": UseCase("Submit Damage Claim", "File a claim for vehicle damage caused by potholes"),
        "View Pothole Status": UseCase("View Pothole Status", "Check the repair status of reported potholes"),
        "View Claim Status": UseCase("View Claim Status", "Track the status of submitted damage claims"),
        
        # Admin use cases
        "View Reported Potholes": UseCase("View Reported Potholes", "Review all pothole reports in the system"),
        "Assign Repair Crew": UseCase("Assign Repair Crew", "Designate crew members to repair specific potholes"),
        "Update Work Order": UseCase("Update Work Order", "Modify work order details and status"),
        "Generate Reports": UseCase("Generate Reports", "Create summary and analytics reports"),
        "Manage Damage Claims": UseCase("Manage Damage Claims", "Process and respond to citizen damage claims"),
        
        # Crew use cases
        "Update Repair Status": UseCase("Update Repair Status", "Report progress on pothole repairs"),
        "Log Hours": UseCase("Log Hours", "Record time spent on repair work"),
        "Enter Material Usage": UseCase("Enter Material Usage", "Document materials used in repairs"),
    }
    
    # Assign use cases to actors
    citizen.add_use_case(use_cases["Report Pothole"])
    citizen.add_use_case(use_cases["Submit Damage Claim"])
    citizen.add_use_case(use_cases["View Pothole Status"])
    citizen.add_use_case(use_cases["View Claim Status"])
    
    admin.add_use_case(use_cases["View Reported Potholes"])
    admin.add_use_case(use_cases["Assign Repair Crew"])
    admin.add_use_case(use_cases["Update Work Order"])
    admin.add_use_case(use_cases["Generate Reports"])
    admin.add_use_case(use_cases["Manage Damage Claims"])
    
    crew.add_use_case(use_cases["Update Repair Status"])
    crew.add_use_case(use_cases["Log Hours"])
    crew.add_use_case(use_cases["Enter Material Usage"])
    
    # Define relationships
    use_cases["Assign Repair Crew"].add_relationship("include", "Update Work Order")
    use_cases["Update Repair Status"].add_relationship("include", "Update Work Order")
    use_cases["Log Hours"].add_relationship("include", "Update Work Order")
    use_cases["Enter Material Usage"].add_relationship("include", "Update Work Order")
    
    # Print Actors and their Use Cases
    print("ACTORS AND THEIR USE CASES")
    print("-" * 70)
    for actor in actors:
        print(f"\n{actor}")
        print(f"Number of use cases: {len(actor.use_cases)}")
        for use_case in actor.use_cases:
            print(use_case)
    
    print("\n" + "=" * 70)
    print("USE CASE RELATIONSHIPS")
    print("-" * 70)
    print("\nThe following use cases have <<include>> relationships:\n")
    
    for uc_name, uc in use_cases.items():
        if uc.relationships:
            for rel_type, target in uc.relationships:
                print(f"  • '{uc_name}' <<{rel_type}>> '{target}'")
    
    # Generate Summary
    print("\n" + "=" * 70)
    print("DIAGRAM STRUCTURE SUMMARY")
    print("-" * 70)
    print(f"""
The PHTRS use case diagram models a Pothole Tracking and Repair System with
three main actors and {len(use_cases)} use cases.

ACTORS ({len(actors)} total):
  • Citizen: Interacts with {len(citizen.use_cases)} use cases for reporting and tracking
  • Public Works Admin: Manages {len(admin.use_cases)} use cases for coordination and oversight
  • Repair Crew: Performs {len(crew.use_cases)} use cases for field operations

KEY PATTERNS:
  • Citizens focus on reporting issues and monitoring status
  • Admins coordinate between citizens and repair crews
  • The 'Update Work Order' use case serves as a central integration point,
    included by 4 different use cases (Assign Repair Crew, Update Repair Status,
    Log Hours, and Enter Material Usage)
  
WORKFLOW:
  1. Citizens report potholes and can track their status
  2. Admins review reports and assign repair crews
  3. Crews update repair progress, log hours, and record materials
  4. All crew activities and admin assignments update the central work order
  5. Citizens can also submit and track damage claims processed by admins

This system facilitates efficient pothole management from initial report through
repair completion and damage claim resolution.
""")
    print("=" * 70)

if __name__ == "__main__":
    main()