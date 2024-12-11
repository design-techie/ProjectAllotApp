// Copyright (c) 2024, vprojects and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Project", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Project", {
    refresh: function(frm) {
        // Only add the button if the project has been saved 
        if (!frm.is_new()) {
            frm.add_custom_button(__('Create Task'), function() {
                frappe.new_doc("Project Task", {
                    proj_id: frm.doc.ID // Automatically link the new task to the current project
                });
            }, __('Actions'));
        }
    }
});




