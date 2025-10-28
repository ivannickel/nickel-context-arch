# Funnel Stages and Definitions

Area: 🤑 Revenue
Owner: Ray Fu
Status: Outdated
Status 2: Draft
Type: Reference
Version: 1.0

## Sales Funnel Lifecycle and Definitions

| Stages | Description | Entry Criteria | Qualification Level at end of stage |
| --- | --- | --- | --- |
| Aware | You’re aware of Nickel, but we don’t have your contact info yet | - Marketing only | - Marketing only |
| Cold | We got your contact information and have identified you as a potential customer through various prospecting efforts | - Outbound only |  |
| Warm Lead | We have your information and have some indicator that you’re familiar with Nickel | - Subscribed to our blog, followed us on LinkedIn, etc.
- Used Nickel to pay or receive payments | You meet our basic firmographic qualifications, but we do not know if you’re [Green, Yellow or Red ICP](ICP%20Summary%20&%20Use%20Cases%207085d388732a44caaa41db763f531999.md)  |
| MQL | You’ve responded positively to Nickel | - You responded positively to either our outbound or inbound efforts
- Ex. responded to email, downloaded a white paper, signed up for a demo, etc. | You meet our basic firmographic qualifications, but we do not know if you’re [Green, Yellow or Red ICP](ICP%20Summary%20&%20Use%20Cases%207085d388732a44caaa41db763f531999.md)  |
| SQL | You’re aware of the problem and Nickel’s value proposition resonates | - You’ve agreed to a discovery call and we have it scheduled on the calendar | You meet our basic firmographic qualifications, but we do not know if you’re [Green, Yellow or Red ICP](ICP%20Summary%20&%20Use%20Cases%207085d388732a44caaa41db763f531999.md)  |
| Opportunity | You have demonstrated a clear intent to evaluate and consider a solution. We’re actively pursuing a deal and the deal is tracked in our Deal Pipeline | - You’ve attended a discovery call
- We’ve confirmed that you’re ICP you have real intentions to evaluate and purchase a solution | We know if you’re [Green, Yellow or Red ICP](ICP%20Summary%20&%20Use%20Cases%207085d388732a44caaa41db763f531999.md) and which solutions are most suitable for your business |
| Customer | You’ve signed up and are actively using Nickel | - You’ve registered on Nickel and handle more than 3 transactions a month on our platform | Same |
| Evangelist | You’ve met our LIR and are suitable for upsell or referrals | - You handle more than 50% of receivables on Nickel and are an avid user | Same |

## Deal Pipeline Definitions

| Deal Pipeline | Description | Entry Criteria | Win % |
| --- | --- | --- | --- |
| Demo Scheduled | You’ve agreed to a personalized Demo | - Demo scheduled | 25% |
| Demo Attended | You attended a personalized Demo and have provided information we needed to evaluate the opportunity | - Demo Attended
- We know the size of the opportunity, timeline, ACV, decision steps. | 50% |
| Trial Invitation Sent | We sent you a registration link | - Received registration link | 75% |
| Trial Started | You’ve registered and are evaluating our product | - Registered for Nickel | 80% |
| Review & Q&A
(Optional) | Your evaluation has ended, but you need more information before you will convert | - Trial ended | 80% |
| Deal Won | You signed up for a subscription | - Converted | N/A |
| Deal Lost | You decided to use another service | - Did not convert | N/A |
| Deal Abandoned | You decided not to move forward because of timing, budget and other consideration. But you’re also not adopting another service | - Did not convert | N/A |

---

**Notes and brainstorm**

Aware - we don’t have your information yet, you might have interacted with us somehow. This information lives in GA4 / trackers

Lead - we have your contact information and have identified you through different efforts: prospecting, trade shows, saw you pay one of our customers, etc.

Entry: no requirements

Exit: positive response

Edge cases:

- Fuck off: stay lead, flag with do not contact and can continue to target with marketing

Engaged Lead / MQL

You responded positively to us:

- If outbound: replied to the email to learn more
- If inbound: submitted a form, downloaded a paper, etc.
- At this point, we do not know if you’re a good fit for Nickel and additional discovery is required

Entry: positive engagement (replied) and aware that they have a problem

Exit criteria: agrees to a discovery call (clear intent to consider)

Edge cases:

- Don’t show up to discovery call: flag with follow up and can auto send them a lower commitment request like reschedule link, personalized demo video, etc.
    - You can further tag them with Busy/Reschedule and No Response to know how to interact with them in the future
    - These guys are good for long term nurturing campaigns with product updates, relevant case studies, or even new offers. This keeps you top-of-mind without being too aggressive.

Sales Qualified Lead

- Entry criteria
    - Aware that there’s a problem and there’s clear intent to consider a solution - usually by agreeing to a discovery call
    - Becomes an active SQL (meaning we’re actively pursuing)
- Exit criteria:
    - Had a conversation with Nickel sales team and has demonstrated problem/product alignment (confirmed that they’re ICP). know the size of the opportunity and what it takes to move the deal forward
    - One of the following outcomes: moves to opportunity, nurture (not a good time) or unqualified
- Edge cases
    - we do the discovery call and realize they're not a good fit. I know we change the lead status to unqualified, but do we keep the lifecycle stage to SQL or does it go back to a "Lead": move them back to MQL with unqualified status. They’re no longer being actively pursued by sales and may not be a good fit for our product right now, but keep them in your database for future nurturing.
    - we do the discovery call and realize its a good fit but its not the right time. Do I keep the lead in a SQL stage: keep them in SQL but change lead status to “bad timing”
    - SQLs can have different substatuses depending on the outcome. You can be an SQL but we’re not actively pursuing at the moment

Opportunity

- This is when the lead formally becomes part of our sales pipeline. There is a genuine opportunity for revenue and conversion. And only leads who have a genuine chance of closing as a customer will enter our opportunity pipeline, this prevents the sales team from wasting time on unqualified or uninterested leads
- When we scale, this is also the handoff between BDR and Account Execs
- Subprocess
    - Demo Scheduled: confirm, reminder, prepare/customize
    - Demo Attended: debrief, timing/pricing, address follow ups and questions
    - Trial Invitation Sent: Send, Confirm that they’ve received the link and are aware of trial specifics, reminder
    - Trial Started: Monitor usage, CS support, schedule a mid-trial check in, drip marketing resources like FAQs and guides
    - Post Trial Review: trial ended, answer any remainder questions, negotiate if needed
    - Closed Won / Lost / abandoned

Demo

Demo follow ups - leads who’ve completed a demo but haven’t signed up yet

Customer

Evangelist: Happy customers who are actively recommending your product (if you track advocacy); or customers who have > 50% usage

---

Hubspot

**Lifecycle Stage:** Describes a contact's relationship with your company

**Lead Status:** Describes sales activities during the qualification process

**Deal Stage:** Represent steps in  your companies sales process

Unqualified MQL vs. Unqualified Lead

DO NOT CONTACT lead status

NO SHOW / Follow Up status

Lead Object replaces Lead Status in Hubspot

- Designed specifically for Sales while the other pipeline is more for marketing (i guess?)
- What is the relationship between Lead and Lifecycle Stage - you get to define this
    - Option 1 - Do we want to create a lead when a contact hits a certain lifecycle stage?
    -