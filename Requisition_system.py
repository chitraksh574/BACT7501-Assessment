# BACT7501 Assessment 2 - Purchase Requisition System
# Uses simple Python concepts: classes, methods, lists, loops and conditionals.

class Requisition:
    def __init__(self, requisition_id):
        # Store all details for a single purchase requisition
        self.requisition_id = requisition_id
        self.date = ""
        self.staff_id = ""
        self.staff_name = ""
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

    def staff_info(self):
        # Ask the user for staff details and check that inputs are not blank
        print("Enter staff information:")

        while True:
            date_input = input("Date (DD-MM-YYYY): ")
            if date_input == "":
                print("Date cannot be empty. Please try again.")
            else:
                self.date = date_input
                break

        while True:
            staff_id_input = input("Staff ID: ")
            if staff_id_input == "":
                print("Staff ID cannot be empty. Please try again.")
            else:
                self.staff_id = staff_id_input
                break

        while True:
            staff_name_input = input("Staff Name: ")
            if staff_name_input == "":
                print("Staff Name cannot be empty. Please try again.")
            else:
                self.staff_name = staff_name_input
                break

    def requisitions_details(self):
        # Ask the user to enter one or more purchase items and prices
        print("Enter requisition items:")

        while True:
            while True:
                item_name = input("Item name: ")
                if item_name == "":
                    print("Item name cannot be empty. Please try again.")
                else:
                    break

            while True:
                try:
                    item_price = float(input("Item price: $"))
                    if item_price <=0:
                        print("Price must be greater than 0. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Invalid price. Please enter a number.")

            # Save the item name and price as a small list inside self.items
            self.items.append([item_name, item_price])

            # Ask whether the user wants to add another item
            while True:
                another_item = input("Add another item? (yes/no): ").lower()
                if another_item == "yes" or another_item == "no":
                    break
                else:
                    print("Please enter yes or no.")

            if another_item == "no":
                break

        # Calculate the total cost of all entered items
        self.total = 0
        for item in self.items:
            self.total += item[1]

    def requisition_approval(self):
        # Automatically approve requisitions below $500; keep $500 or more Pending
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    def respond_requisition(self):
        # Allow a manager to approve, reject, or leave a pending requisition pending
        if self.status == "Pending":
            print("")
            print(f"Reviewing Requisition ID: {self.requisition_id}")
            print(f"Staff Name: {self.staff_name} | Total: ${self.total}")

            while True:
                decision = input("Manager decision (approve/reject/pending): ").lower()
                if decision == "approve":
                    self.status = "Approved"
                    self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
                    print("Requisition has been Approved.")
                    break
                elif decision == "reject":
                    self.status = "Not approved"
                    self.approval_reference = "Not available"
                    print("Requisition has been marked Not approved.")
                    break
                elif decision == "pending":
                    self.status = "Pending"
                    self.approval_reference = "Not available"
                    print("Requisition remains Pending.")
                    break
                else:
                    print("Invalid choice. Please enter approve, reject, or pending.")

    def display_requisition(self):
        # Print the full summary for this requisition
        print("")
        print("Requisition Summary")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print("Items:")
        for item in self.items:
            print(f"  - {item[0]}: ${item[1]}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference}")


class RequisitionSystem:
    def __init__(self):
        # Requisition IDs start at 10001 (10000 + 1 for the first requisition)
        self.requisition_counter = 10000
        self.requisitions = []

    def add_requisition(self):
        # Create a new requisition, collect inputs, apply rules, and display result
        self.requisition_counter += 1
        new_requisition = Requisition(self.requisition_counter)
        new_requisition.staff_info()
        new_requisition.requisitions_details()
        new_requisition.requisition_approval()
        new_requisition.display_requisition()
        self.requisitions.append(new_requisition)

    def review_pending_requisitions(self):
        # Check if there are any pending requisitions for manager review
        has_pending = False
        for req in self.requisitions:
            if req.status == "Pending":
                has_pending = True

        if has_pending:
            print("")
            while True:
                review_choice = input("Do you want to review pending requisitions as manager? (yes/no): ").lower()
                if review_choice == "yes" or review_choice == "no":
                    break
                else:
                    print("Please enter yes or no.")

            if review_choice == "yes":
                for req in self.requisitions:
                    if req.status == "Pending":
                        req.respond_requisition()

    def display_all_requisitions(self):
        # Display every requisition stored in the system
        print("")
        print("All Requisitions")
        if self.requisitions == []:
            print("No requisitions found.")
        else:
            for req in self.requisitions:
                req.display_requisition()

    def display_statistics(self):
        # Count total, approved, pending, and not approved requisitions
        total_count = 0
        approved_count = 0
        pending_count = 0
        not_approved_count = 0

        for req in self.requisitions:
            total_count += 1
            if req.status == "Approved":
                approved_count += 1
            elif req.status == "Pending":
                pending_count += 1
            else:
                not_approved_count += 1

        print("")
        print("Requisition Statistics")
        print(f"Total requisitions submitted: {total_count}")
        print(f"Total approved requisitions: {approved_count}")
        print(f"Total pending requisitions: {pending_count}")
        print(f"Total not approved requisitions: {not_approved_count}")

    def run(self):
        # Run the main program loop
        print("Purchase Requisition System")

        while True:
            print("")
            self.add_requisition()

            while True:
                another_req = input("Do you want to enter another requisition? (yes/no): ").lower()
                if another_req == "yes" or another_req == "no":
                    break
                else:
                    print("Please enter yes or no.")

            if another_req == "no":
                break

        self.review_pending_requisitions()
        self.display_all_requisitions()
        self.display_statistics()
        
        


# Start the Purchase Requisition System
if __name__ == "__main__":
    system = RequisitionSystem()
    system.run()
