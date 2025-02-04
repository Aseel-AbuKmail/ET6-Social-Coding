# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""
# Muhannad Asaf, Muhammet Isik, Al_Hassen Sabeeh, Aseel AbuKmail, Maria Roufail

# Employee_IDs= str(input("Enter employee IDs (formatted as E####)"))

finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Employee_IDs = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590","E9812", "E4520","E9999", "E0001"}
Admin = {"E0001"}
  
# Who has access to at least one type of data?

access_to_any_data = finance_access | tech_access | Admin
print("Employees with access to at least one type of data:", access_to_any_data)

# Who has access to both financial and technical data?

access_to_both_data = finance_access & tech_access
print("Employees with access to both financial and technical data:", access_to_both_data)

# Who has exclusive access to only one type of data?
access_to_only_type_of_data = access_to_any_data  - access_to_both_data
print("Employees with access to only one type of data:", access_to_only_type_of_data)

# Which employees currently lack access (but exist in the system)?
lack_access = Employee_IDs - access_to_any_data
print("Employees with lack access (but exist in the system):", lack_access)


# Are there unnecessary overlaps in access that could pose a security risk?


# What changes would you recommend to enhance security and minimize excessive access?
