import InternalDashboard from '../dashboard.vue'
import Search from '../search.vue'
import OrgAccessTable from '../organisations/access_dashboard.vue'
import OrgAccess from '../organisations/access.vue'
import Organisation from '../organisations/manage.vue'
import UserDashTable from '../users/dashboard.vue'
import User from '../users/manage.vue'
import Application from '../applications/application.vue'
import CompleteAssessment from '../applications/complete_assessment.vue'
import LicenceDashTable from '../licences/dashboard.vue'
import CallEmailDashTable from '../call_email/call_email_dashboard.vue'
import CallEmail from '../call_email/call_email.vue'
import ReturnDashTable from '../returns/dashboard.vue'
import Returns from '../returns/return.vue'
import InspectionDashTable from '../inspection/inspection_dashboard.vue'
import LegalCaseDashTable from '../legal_case/legal_case_dashboard.vue'
import LegalCase from '../legal_case/legal_case.vue'
import Inspection from '../inspection/inspection.vue'
import ArtifactDashTable from '../artifact/artifact_dashboard.vue'
import Artifact from '../artifact/artifact.vue'
import SanctionOutcomeDashTable from '../sanction_outcome/sanction_outcome_dashboard.vue'
import SanctionOutcome from '../sanction_outcome/sanction_outcome.vue'
import OffenceDashTable from '../offence/offence_dashboard.vue'
import Offence from '../offence/offence.vue'
import DashboardSwitcher from '../dashboard_switcher.vue'
import Reports from '@/components/reports/reports.vue'

export default
{
    path: '/internal',
    component:
    {
        render(c)
        {
            return c('router-view')
        }
    },
    children: [
        /*
        {
            path: '/',
            component: InternalDashboard,
            name: 'internal-dash'
        },
        */
        {
            path: '/',
            component: DashboardSwitcher,
            name: 'internal-dash'
        },

        {
            path: 'licences',
            component: LicenceDashTable,
            name:"internal-licences-dash"
        },
        {
            path: 'inspection',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: InspectionDashTable,
                    name:"internal-inspection-dash"
                },
                {
                    path: ':inspection_id',
                    component: Inspection,
                    name:"view-inspection"
                },
            ]
        },
        {
            path: 'legal_case',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: LegalCaseDashTable,
                    name:"internal-legal-case-dash"
                },
                {
                    path: ':legal_case_id',
                    component: LegalCase,
                    name:"view-legal-case"
                },
            ]
        },
        {
            path: 'object',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: ArtifactDashTable,
                    name:"internal-artifact-dash"
                },
                {
                    path: ':artifact_id',
                    component: Artifact,
                    name: "view-artifact"
                },
            ]
        },

        {
            path: 'offence',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: OffenceDashTable,
                    name:"internal-offence-dash"
                },
                {
                    path: ':offence_id',
                    component: Offence,
                    name:"view-offence"
                },
            ]
        },
        {
            path:'reports',
            name:'reports',
            component:Reports
        },
        {
            path: 'sanction_outcome',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: SanctionOutcomeDashTable,
                    name:"internal-sanction-outcome-dash"
                },
                {
                    path: ':sanction_outcome_id',
                    component: SanctionOutcome,
                    name:"view-sanction-outcome"
                },
            ]
        },
        {
            path: 'call_email',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: CallEmailDashTable,
                    name:"internal-call-email-dash"
                },
                {
                    path: ':call_email_id',
                    component: CallEmail,
                    name:"view-call-email"
                },
            ]
        },
        {
            path: 'returns',
            component: ReturnDashTable,
            name:"internal-returns-dash"
        },
        {
            path: 'search',
            component: Search,
            name:"internal-search"
        },
        {
            path: 'return/:return_id',
            component: Returns
        },
        {
            path: 'users',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: '/',
                    component: UserDashTable,
                    name:"internal-users-dash"
                },
                {
                    path: ':user_id',
                    component: User,
                    name:"internal-user-detail"
                },
            ]
        },
        {
            path: 'organisations',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            children: [
                {
                    path: 'access',
                    component: OrgAccessTable,
                    name:"org-access-dash"
                },
                {
                    path: 'access/:access_id',
                    component: OrgAccess,
                    name:"org-access"
                },
                {
                    path: ':org_id',
                    component: Organisation,
                    name:"internal-org-detail"
                },
 
            ]
        },
        {
            path: 'application',
            component: {
                render(c)
                {
                    return c('router-view')
                }
            },
            
            children: [
                {
                    path: ':application_id',
                    component: {
                        render(c)
                        {
                            return c('router-view')
                        }
                    },
                    children: [
                        {
                            path: '/',
                            component: Application,
                            name:"internal-application"
                        },
                        
                    ]
                },
                {
                    path: 'assessment/:application_id',
                    component: CompleteAssessment,
                    name:"complete-assessment"
                },
 
            ]
        },
        /*{
            path: 'application',
            component: Application,
            name:"new_application"
        }*/
    ]
}
