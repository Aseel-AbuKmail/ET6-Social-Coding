# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 3: Access Visualization
Objective
Develop a visual representation of the company's access control system to identify patterns, overlaps, and security risks.
Scenario
The company’s security team is struggling to interpret raw access data. They need a clear way to see:
Employees who have access to financial records, technical documents, or both.
Employees with no access, who may need onboarding.
Any overlap that could indicate excessive privileges or security risks.
Instead of listing raw data, your task is to create a structured representation that makes these relationships intuitive and easy to understand.
Your Task
Using the provided employee access data, design a way to illustrate:
Who belongs where? Group employees based on their level of access.
Where is the overlap? Show employees who have access to both financial and technical records.
Who is left out? Identify employees without access.
Are there risks? Indicate employees who might be exposed to unnecessary data.
Your output should visually highlight these relationships without explicitly listing them in a simple table or list. Think beyond just printing data—use a format that helps detect patterns at a glance.
"""

#finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
#tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
#Employee_IDs = {"E0435","E1021","E3098","E7642","E8873","E6590","E9812","E4520","E9999","E0001",}
#Admin = {"E0001"}

# Who belongs where? Group employees based on their level of access.
#access_to_any_data = finance_access | tech_access | Admin
#print("Employees with access to at least one type of data:", access_to_any_data)

# Where is the overlap? Show employees who have access to both financial and technical records.
#access_to_both_data = finance_access & tech_access
#print("Employees with access to both financial and technical data:", access_to_both_data)

# Who is left out? Identify employees without access.
#lack_access = Employee_IDs - access_to_any_data
#print("Employees with lack access (but exist in the system):", lack_access)

# Are there risks? Indicate employees who might be exposed to unnecessary data.

import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles


def visualize_access_control(financial_access, technical_access, employee_ids, admin):
    both_access = financial_access & technical_access
    only_financial = financial_access - both_access
    only_technical = technical_access - both_access
    no_access = employee_ids - (financial_access | technical_access | admin)

    plt.figure(figsize=(6, 6))
    venn = venn2([financial_access, technical_access], ("Financial Records", "Technical Records"))
    venn2_circles([financial_access, technical_access])

    if venn.get_label_by_id("10"):
        venn.get_label_by_id("10").set_text("\n".join(only_financial))
    if venn.get_label_by_id("01"):
        venn.get_label_by_id("01").set_text("\n".join(only_technical))
    if venn.get_label_by_id("11"):
        venn.get_label_by_id("11").set_text("\n".join(both_access))

    plt.title("Employee Access Control Visualization")
    plt.show()

    print("Employees without access:", no_access)
    print("Admin employees:", admin)


# Employee access data
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Employee_IDs = {"E0435","E1021","E3098","E7642","E8873","E6590","E9812","E4520","E9999","E0001",}
Admin = {"E0001"}

visualize_access_control(finance_access, tech_access, Employee_IDs, Admin)

