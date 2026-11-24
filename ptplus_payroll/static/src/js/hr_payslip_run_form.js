import {PayslipBatchFormController} from "@hr_payroll/views/payslip_run_form/hr_payslip_run_form";
import {markup} from "@odoo/owl";
import {patch} from "@web/core/utils/patch";
import {serializeDate} from "@web/core/l10n/dates";

patch(PayslipBatchFormController.prototype, {
    async selectEmployees() {
        const data = this.model.root.data;
        if (!data.l10n_pt_independent_slip) {
            return super.selectEmployees(...arguments);
        }
        // The pay run is not saved yet, so the server only knows the kind of
        // slip it is going to hold if it is sent along with the period.
        const employeeListAction = await this.orm.call(
            "hr.payslip.run",
            "action_payroll_hr_version_list_view_payrun",
            [
                [this.model.root.resId],
                serializeDate(data.date_start),
                serializeDate(data.date_end),
                data.structure_id?.id,
                data.company_id?.id,
                data.schedule_pay,
            ],
            {l10n_pt_independent_slip: data.l10n_pt_independent_slip}
        );
        return this.actionService.doAction({
            ...employeeListAction,
            help: markup(employeeListAction.help),
            context: {
                raw_record: data,
            },
        });
    },
});
