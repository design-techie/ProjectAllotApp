# Copyright (c) 2024, vprojects and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import getdate
from frappe import _

class ProjectTask(Document):
    def validate(self):
        # Fetch the associated project document to get its start and end dates
        project = frappe.get_doc("Project", self.proj_id)
        
        # Validate that the task's start date is after or equal to the project's start date
        if getdate(self.task_sdate) < getdate(project.proj_start):
            frappe.throw(_("Task Start Date must be on or after the Project's Start Date"))

        # Validate that the task's end date is on or before the project's end date
        if getdate(self.task_edate) > getdate(project.proj_end):
            frappe.throw(_("Task End Date must be on or before the Project's End Date"))

