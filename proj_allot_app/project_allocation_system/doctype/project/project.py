# Copyright (c) 2024, vprojects and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from frappe import _


class Project(Document):
    def validate(self):
        # Fetch financial year start and end dates from Project Allocation Setting
        settings = frappe.get_single("Project Allocation Setting")
        f_start_date = getdate(settings.f_start_date)
        f_end_date = getdate(settings.f_end_date)

        # Validate that the project's start date is within the financial year
        if not (f_start_date <= getdate(self.proj_start) <= f_end_date):
            frappe.throw(_("Project Start Date must be within the financial year range: {0} to {1}").format(f_start_date, f_end_date))

        # Validate that the project's end date is after the start date
        if getdate(self.proj_end) < getdate(self.proj_start):
            frappe.throw(_("Project End Date cannot be before the Start Date"))


