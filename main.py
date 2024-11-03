"""
citations: chatgpt, in class lessons
"""


from datetime import datetime, date

class Transaction:
    def __init__(self, date, amount, category, description):
        self.date = date  # datetime object
        self.amount = amount  # float
        self.category = category  # string
        self.description = description  # string

    def __str__(self):
        return (f"Date: {self.date.strftime('%Y-%m-%d')}, Amount: {self.amount}, "
                f"Category: {self.category}, Description: {self.description}")

    def __eq__(self, other):
        return (self.date == other.date and
                self.amount == other.amount and
                self.category == other.category and
                self.description == other.description)

"""
class CashTransaction(Transaction):
    def __init__(self, date, amount, description, category):
        super().__init__(date, amount, description)
        self.category = category

    def __str__(self):
        return (super().__str__() + f", Category: {self.category}, Method: Cash")

    def process_transaction(self):
        pass

    def __eq__(self, other):
        return (isinstance(other, CashTransaction) and
                super().__eq__(other) and
                self.category == other.category)

class ETransaction(Transaction):
    def __init__(self, date, amount, description, category, vendor):
        super().__init__(date, amount, description)
        self.category = category
        self.vendor = vendor

    def __str__(self):
        return (super().__str__() + f", Category: {self.category}, Vendor: {self.vendor}")

    def process_transaction(self):
        pass

    def __eq__(self, other):
        return (isinstance(other, ETransaction) and
                super().__eq__(other) and
                self.category == other.category and
                self.vendor == other.vendor)
"""

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None  # or raise exception

    def is_empty(self):
        return len(self.stack) == 0

class ListNode:
    def __init__(self, transaction):
        self.transaction = transaction
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_tail(self, transaction):
        new_node = ListNode(transaction)
        if not self.head:
            self.head = self.tail = new_node
        else:
            # Check for duplicate transaction
            curr = self.head
            while curr:
                if curr.transaction == transaction:
                    print("Duplicate transaction detected. Transaction not added.")
                    return False
                curr = curr.next
            self.tail.next = new_node
            self.tail = new_node
        return True

    def delete_node(self, transaction):
        prev = None
        curr = self.head
        while curr:
            if curr.transaction == transaction:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                if curr == self.tail:
                    self.tail = prev
                return True  # deleted
            prev = curr
            curr = curr.next
        return False  # not found

    def find(self, transaction):
        curr = self.head
        while curr:
            if curr.transaction == transaction:
                return curr.transaction
            curr = curr.next
        return None

class BSTNode:
    def __init__(self, transaction):
        self.transaction = transaction
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, key_func):
        self.root = None
        self.key_func = key_func  # function to extract key from transaction

    def insert(self, transaction):
        def _insert(node, transaction):
            if node is None:
                return BSTNode(transaction)
            elif self.key_func(transaction) < self.key_func(node.transaction):
                node.left = _insert(node.left, transaction)
            else:
                node.right = _insert(node.right, transaction)
            return node
        self.root = _insert(self.root, transaction)

    def delete(self, transaction):
        def _delete(node, transaction):
            if node is None:
                return None
            elif self.key_func(transaction) < self.key_func(node.transaction):
                node.left = _delete(node.left, transaction)
            elif self.key_func(transaction) > self.key_func(node.transaction):
                node.right = _delete(node.right, transaction)
            else:
                # Node found
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    # Node with two children
                    successor = self._min_value_node(node.right)
                    node.transaction = successor.transaction
                    node.right = _delete(node.right, successor.transaction)
            return node
        self.root = _delete(self.root, transaction)

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, key):
        def _search(node, key):
            if node is None:
                return []
            elif self.key_func(node.transaction) == key:
                # Collect all transactions with the same key
                return self._collect_equal(node, key)
            elif key < self.key_func(node.transaction):
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)

    def _collect_equal(self, node, key):
        # Collect transactions with keys equal to 'key' in subtree rooted at 'node'
        results = []
        if node is None:
            return results
        if self.key_func(node.transaction) == key:
            results.extend(self._collect_equal(node.left, key))
            results.append(node.transaction)
            results.extend(self._collect_equal(node.right, key))
        elif key < self.key_func(node.transaction):
            results.extend(self._collect_equal(node.left, key))
        else:
            results.extend(self._collect_equal(node.right, key))
        return results

    def transactions_in_order(self):
        results = []
        def _in_order(node):
            if node:
                _in_order(node.left)
                results.append(node.transaction)
                _in_order(node.right)
        _in_order(self.root)
        return results

def quicksort(transactions, key_func):
    if len(transactions) <= 1:
        return transactions
    else:
        pivot = transactions[0]
        less = [x for x in transactions[1:] if key_func(x) <= key_func(pivot)]
        greater = [x for x in transactions[1:] if key_func(x) > key_func(pivot)]
        return quicksort(less, key_func) + [pivot] + quicksort(greater, key_func)

def mergesort(transactions, key_func):
    if len(transactions) <= 1:
        return transactions
    mid = len(transactions) // 2
    left = mergesort(transactions[:mid], key_func)
    right = mergesort(transactions[mid:], key_func)
    return merge(left, right, key_func)

def merge(left, right, key_func):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class ExpenseTracker:
    VALID_CATEGORIES = ['Food', 'Rent', 'Utilities', 'Entertainment', 'Transportation', 'Other']

    def __init__(self):
        self.transactions = LinkedList()
        self.transaction_tree_by_date = BinarySearchTree(key_func=lambda t: t.date)
        self.transaction_tree_by_amount = BinarySearchTree(key_func=lambda t: t.amount)
        self.undo_stack = Stack()

    def add_transaction(self, transaction):
        if self.transactions.add_tail(transaction):
            self.transaction_tree_by_date.insert(transaction)
            self.transaction_tree_by_amount.insert(transaction)
            self.undo_stack.push(('add', transaction))
            print("Transaction added.")

    def delete_transaction(self, transaction):
        if self.transactions.delete_node(transaction):
            self.transaction_tree_by_date.delete(transaction)
            self.transaction_tree_by_amount.delete(transaction)
            self.undo_stack.push(('delete', transaction))
            print("Transaction deleted.")
        else:
            print("Transaction not found.")

    def edit_transaction(self, old_transaction, new_transaction):
        if self.transactions.delete_node(old_transaction):
            self.transactions.add_tail(new_transaction)
            self.transaction_tree_by_date.delete(old_transaction)
            self.transaction_tree_by_date.insert(new_transaction)
            self.transaction_tree_by_amount.delete(old_transaction)
            self.transaction_tree_by_amount.insert(new_transaction)
            self.undo_stack.push(('edit', old_transaction, new_transaction))
            print("Transaction edited.")
        else:
            print("Transaction not found.")

    def view_transactions(self):
        if not self.transactions.head:
            print("No transactions to display.")
            return
        curr = self.transactions.head
        while curr:
            print(curr.transaction)
            curr = curr.next

    def sort_transactions_by_date_quicksort(self):
        # Collect transactions into list
        transactions = []
        curr = self.transactions.head
        while curr:
            transactions.append(curr.transaction)
            curr = curr.next
        if not transactions:
            print("No transactions to sort.")
            return
        # Sort using quicksort
        transactions = quicksort(transactions, key_func=lambda t: t.date)
        for t in transactions:
            print(t)

    def sort_transactions_by_category_mergesort(self):
        # Collect transactions into list
        transactions = []
        curr = self.transactions.head
        while curr:
            transactions.append(curr.transaction)
            curr = curr.next
        if not transactions:
            print("No transactions to sort.")
            return
        # Sort using mergesort
        transactions = mergesort(transactions, key_func=lambda t: t.category)
        for t in transactions:
            print(t)

    def search_transactions_by_category(self, category):
        # Input validation: check if the category is valid
        if category not in self.VALID_CATEGORIES:
            print("Invalid category. Please choose from the valid categories.")
            return
        curr = self.transactions.head
        results = []
        while curr:
            if curr.transaction.category == category:
                results.append(curr.transaction)
            curr = curr.next
        if not results:
            print("No transactions found in that category.")
            return
        for t in results:
            print(t)

    def search_transactions_by_date(self, date):
        transactions = self.transaction_tree_by_date.search(date)
        if transactions:
            for t in transactions:
                print(t)
        else:
            print("No transactions found on that date.")

    def search_transactions_by_amount(self, amount):
        transactions = self.transaction_tree_by_amount.search(amount)
        if transactions:
            for t in transactions:
                print(t)
        else:
            print("No transactions found with that amount.")

    def undo(self):
        if self.undo_stack.is_empty():
            print("Nothing to undo.")
            return
        action = self.undo_stack.pop()
        if action[0] == 'add':
            transaction = action[1]
            self.transactions.delete_node(transaction)
            self.transaction_tree_by_date.delete(transaction)
            self.transaction_tree_by_amount.delete(transaction)
            print("Undo add transaction.")
        elif action[0] == 'delete':
            transaction = action[1]
            self.transactions.add_tail(transaction)
            self.transaction_tree_by_date.insert(transaction)
            self.transaction_tree_by_amount.insert(transaction)
            print("Undo delete transaction.")
        elif action[0] == 'edit':
            old_transaction = action[1]
            new_transaction = action[2]
            self.transactions.delete_node(new_transaction)
            self.transactions.add_tail(old_transaction)
            self.transaction_tree_by_date.delete(new_transaction)
            self.transaction_tree_by_date.insert(old_transaction)
            self.transaction_tree_by_amount.delete(new_transaction)
            self.transaction_tree_by_amount.insert(old_transaction)
            print("Undo edit transaction.")

    def total_spending(self, time_frame):
        # time_frame can be 'day', 'month', or 'year'
        curr = self.transactions.head
        totals = {}
        while curr:
            transaction = curr.transaction
            if time_frame == 'day':
                key = transaction.date.date()
            elif time_frame == 'month':
                key = transaction.date.strftime('%Y-%m')
            elif time_frame == 'year':
                key = transaction.date.strftime('%Y')
            else:
                print("Invalid time frame.")
                return
            totals[key] = totals.get(key, 0) + transaction.amount
            curr = curr.next
        if not totals:
            print("No transactions to calculate.")
            return
        # Sort the totals by date
        sorted_totals = sorted(totals.items())
        for key, total in sorted_totals:
            print(f"{time_frame.capitalize()}: {key}, Total Spending: {total}")

    def calculate_budget_allocation(self):
        # Prompt user for monthly paycheck
        print("\nCalculate Budget Allocation:")
        paycheck = prompt_for_positive_amount("Enter your monthly paycheck: ")
        if paycheck is None:
            print("Operation cancelled.")
            return
        print("\nWould you like to use the recommended allocation percentages (50% Needs, 30% Wants, 20% Savings)?")
        use_recommended = input("Enter 'y' for yes or 'n' for no: ").strip().lower()
        while use_recommended not in ['y', 'n']:
            print("Invalid input. Please enter 'y' or 'n'.")
            use_recommended = input("Enter 'y' for yes or 'n' for no: ").strip().lower()
        if use_recommended == 'y':
            allocations = {
                'Needs': 50,
                'Wants': 30,
                'Savings': 20
            }
        else:
            # Allow user to input custom percentages
            allocations = {}
            total_percentage = 0
            print("\nEnter the percentage allocation for each category. Total must be 100%.")
            while True:
                allocations.clear()
                total_percentage = 0
                for category in ['Needs', 'Wants', 'Savings']:
                    percentage = prompt_for_percentage(f"Enter percentage for {category}: ")
                    if percentage is None:
                        print("Operation cancelled.")
                        return
                    allocations[category] = percentage
                    total_percentage += percentage
                if total_percentage != 100:
                    print(f"Total percentage allocations must add up to 100%. Currently at {total_percentage}%. Please try again.")
                else:
                    break
        # Map the allocations to the expense categories
        # Needs: Rent, Utilities, Transportation
        # Wants: Food, Entertainment
        # Savings: Other
        needs_categories = ['Rent', 'Utilities', 'Transportation']
        wants_categories = ['Food', 'Entertainment']
        savings_categories = ['Other']
        print("\nBased on your inputs, your budget allocation is:")
        for category_group, categories in [('Needs', needs_categories), ('Wants', wants_categories), ('Savings', savings_categories)]:
            allocation_amount = (allocations[category_group] / 100) * paycheck
            print(f"{category_group} ({allocations[category_group]}%): ${allocation_amount:.2f}")
            print("  Categories:", ', '.join(categories))
        print("\nRemember to adjust your spending according to these allocations to meet your financial goals.")

def prompt_for_date(prompt):
    while True:
        date_str = input(prompt)
        if not date_str.strip():
            print("Input cannot be empty. Please enter a date.")
            continue
        try:
            transaction_date = datetime.strptime(date_str, '%Y-%m-%d')
            if transaction_date.date() > date.today():
                print("Date cannot be in the future.")
                continue
            return transaction_date
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

def prompt_for_amount(prompt):
    while True:
        amount_str = input(prompt)
        if not amount_str.strip():
            print("Input cannot be empty. Please enter an amount.")
            continue
        try:
            amount = float(amount_str)
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")

def prompt_for_positive_amount(prompt):
    while True:
        amount_str = input(prompt)
        if not amount_str.strip():
            print("Input cannot be empty. Please enter an amount.")
            continue
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")

def prompt_for_percentage(prompt):
    while True:
        percentage_str = input(prompt)
        if not percentage_str.strip():
            print("Input cannot be empty. Please enter a percentage.")
            continue
        try:
            percentage = float(percentage_str)
            if percentage < 0 or percentage > 100:
                print("Please enter a percentage between 0 and 100.")
                continue
            return percentage
        except ValueError:
            print("Invalid input. Please enter a number.")

def prompt_for_category(prompt, valid_categories):
    while True:
        # Display the available categories to the user
        print(f"Available categories: {', '.join(valid_categories)}")
        category = input(prompt)
        if not category.strip():
            print("Input cannot be empty. Please enter a category.")
            continue
        if category in valid_categories:
            return category
        else:
            print("Invalid category. Please choose from the available categories.")

def prompt_for_description(prompt):
    while True:
        description = input(prompt)
        if not description.strip():
            print("Description cannot be empty. Please enter a description.")
        else:
            return description.strip()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add transaction")
        print("2. Delete transaction")
        print("3. Edit transaction")
        print("4. View transactions")
        print("5. Sort transactions by date (QuickSort)")
        print("6. Sort transactions by category (MergeSort)")
        print("7. Search transactions by category")
        print("8. Search transactions by date")
        print("9. Search transactions by amount")
        print("10. Undo")
        print("11. View total spending")
        print("12. Calculate budget allocation")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == '1':
            transaction_date = prompt_for_date("Enter date (YYYY-MM-DD): ")
            amount = prompt_for_positive_amount("Enter amount: ")
            category = prompt_for_category("Enter category: ", ExpenseTracker.VALID_CATEGORIES)
            description = prompt_for_description("Enter description: ")
            transaction = Transaction(transaction_date, amount, category, description)
            tracker.add_transaction(transaction)

        elif choice == '2':
            if not tracker.transactions.head:
                print("No transactions to delete.")
                continue
            transaction_date = prompt_for_date("Enter date of transaction to delete (YYYY-MM-DD): ")
            amount = prompt_for_positive_amount("Enter amount of transaction to delete: ")
            category = prompt_for_category("Enter category of transaction to delete: ", ExpenseTracker.VALID_CATEGORIES)
            description = prompt_for_description("Enter description of transaction to delete: ")
            transaction_to_delete = Transaction(transaction_date, amount, category, description)
            tracker.delete_transaction(transaction_to_delete)

        elif choice == '3':
            if not tracker.transactions.head:
                print("No transactions to edit.")
                continue
            while True:
                print("Enter details of the transaction to edit:")
                old_transaction_date = prompt_for_date("Enter date (YYYY-MM-DD): ")
                old_amount = prompt_for_positive_amount("Enter amount: ")
                old_category = prompt_for_category("Enter category: ", ExpenseTracker.VALID_CATEGORIES)
                old_description = prompt_for_description("Enter description: ")
                old_transaction = Transaction(old_transaction_date, old_amount, old_category, old_description)

                # Check if the transaction exists
                found_transaction = tracker.transactions.find(old_transaction)
                if found_transaction:
                    # Proceed to get new details
                    print("Enter new details for the transaction:")
                    new_transaction_date = prompt_for_date("Enter new date (YYYY-MM-DD): ")
                    new_amount = prompt_for_positive_amount("Enter new amount: ")
                    new_category = prompt_for_category("Enter new category: ", ExpenseTracker.VALID_CATEGORIES)
                    new_description = prompt_for_description("Enter new description: ")
                    new_transaction = Transaction(new_transaction_date, new_amount, new_category, new_description)
                    tracker.edit_transaction(old_transaction, new_transaction)
                    break
                else:
                    print("Transaction not found with the provided details.")
                    retry = input("Would you like to try again? (y/n): ").strip().lower()
                    while retry not in ['y', 'n']:
                        print("Invalid input. Please enter 'y' or 'n'.")
                        retry = input("Would you like to try again? (y/n): ").strip().lower()
                    if retry != 'y':
                        break

        elif choice == '4':
            tracker.view_transactions()

        elif choice == '5':
            tracker.sort_transactions_by_date_quicksort()

        elif choice == '6':
            tracker.sort_transactions_by_category_mergesort()

        elif choice == '7':
            if not tracker.transactions.head:
                print("No transactions to search.")
                continue
            category = prompt_for_category("Enter category to search: ", ExpenseTracker.VALID_CATEGORIES)
            tracker.search_transactions_by_category(category)

        elif choice == '8':
            if not tracker.transactions.head:
                print("No transactions to search.")
                continue
            search_date = prompt_for_date("Enter date to search (YYYY-MM-DD): ")
            tracker.search_transactions_by_date(search_date)

        elif choice == '9':
            if not tracker.transactions.head:
                print("No transactions to search.")
                continue
            search_amount = prompt_for_positive_amount("Enter amount to search: ")
            tracker.search_transactions_by_amount(search_amount)

        elif choice == '10':
            tracker.undo()

        elif choice == '11':
            if not tracker.transactions.head:
                print("No transactions to calculate.")
                continue
            while True:
                print("Choose time frame to view total spending:")
                print("1. Day")
                print("2. Month")
                print("3. Year")
                time_frame_choice = input("Enter your choice: ").strip()
                if time_frame_choice == '1':
                    tracker.total_spending('day')
                    break
                elif time_frame_choice == '2':
                    tracker.total_spending('month')
                    break
                elif time_frame_choice == '3':
                    tracker.total_spending('year')
                    break
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")

        elif choice == '12':
            tracker.calculate_budget_allocation()

        elif choice == '0':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

