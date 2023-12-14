staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}
if managers < staff:
    print("All managers are staff members")
if managers.issubset(staff):
    print("All managers are staff members (using issubset())")
if managers <= staff:
    print("All managers are staff members (proper subset)")
if managers.issubset(staff) and managers != staff:
    print("All managers are staff members (using issubset() with inequality)")
if staff > managers:
    print("All managers are staff members")
if staff.issuperset(managers):
    print("All managers are staff members (using issuperset())")
if staff >= managers:
    print("All managers are staff members (proper superset)")
if staff.issuperset(managers) and staff != managers:
    print("All managers are staff members (using issuperset() with inequality)")