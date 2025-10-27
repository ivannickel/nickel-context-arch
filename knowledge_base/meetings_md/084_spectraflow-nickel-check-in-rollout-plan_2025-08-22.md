---
title: Spectraflow + Nickel | Check-In + Rollout Plan
date: '2025-08-22'
time: '15:03:56'
duration_sec: 2944.58
duration_min: 49.1
participants:
- Colton O'Farrell <colton@getnickel.com>
- Spectraflow East <jodie@spectraflow.com>
- Christian Sheerer <christian@getnickel.com>
- Accounts Payable East at Spectraflow <ap_east@spectraflow.com>
- Jodie Steen <null>
source: Circleback
meeting_number: 84
---

Jodie Steen: Know Hafeez is joining as well.
Colton O'Farrell: Oh, perfect.
Jodie Steen: Yeah.
Colton O'Farrell: How has your week been going since we last spoke?
Jodie Steen: Pretty good. And it's my daughter's birthday today, so.
Christian Sheerer: Oh, my gosh.
Colton O'Farrell: Happy birthday to your daughter. How old does she turn in?
Jodie Steen: 16 today.
Colton O'Farrell: Ooh, sweet 16.
Jodie Steen: That's a big one. Yeah. So I'm. I'm taking off this afternoon, and we're gonna go do.
Colton O'Farrell: What are Do you do a little spa day?
Jodie Steen: Yeah, doing the nails and she wants to go to Sephora.
Colton O'Farrell: Of course, classic.
Jodie Steen: Dinner, so yeah, all the things.
Colton O'Farrell: Oh, I love that. Are you guys doing any kind of family or friends party sort of thing this weekend too?
Jodie Steen: Yeah, well, I'm actually taking her and three of her best friends. Hi, Hafiz.
Accounts Payable East at Spectraflow: Hello.
Jodie Steen: Hello. My family lives in Bermuda, so we're taking them there.
Christian Sheerer: Oh, nice.
Accounts Payable East at Spectraflow: Yeah. how exciting.
Jodie Steen: That'Ll be the the big sweet 16 present I don't know if I told you that it's honor's birthday today she turned 16.
Accounts Payable East at Spectraflow: Oh wow.
Jodie Steen: Yeah.
Christian Sheerer: Hey hey how's it going everybody?
Jodie Steen: Hey good how are you doing well.
Christian Sheerer: Doing well staying busy.
Colton O'Farrell: It's Jodie's daughter's 16th birthday today. So we were just talking about the plans they have and then Hafiz joined as well. So I think we got everybody on the call.
Christian Sheerer: Do we have a sweet 16 going on?
Jodie Steen: Yes.
Colton O'Farrell: It sounds like too, they're going to Bermuda. She's taking her daughter and some of their best friends and spoiled. Spoiled.
Christian Sheerer: Spoiled. Absolutely. Hafiz, nice to meet you.
Colton O'Farrell: Let's see, you might be connecting to audio.
Jodie Steen: Can you hear us, Hippies?
Accounts Payable East at Spectraflow: Yeah, hello, yeah, it was a little bit issue, sorry.
Colton O'Farrell: No worries.
Christian Sheerer: Awesome. Okay, so I think we have a pretty good agenda sketched out. Let's go through it.
Accounts Payable East at Spectraflow: One by one.
Christian Sheerer: Did you guys get a chance to go through some AR transactions in between now and when we last chatted?
Jodie Steen: So we didn't, and the reason for that we realized is we need to have an invoice that's ready to charge via ACH or credit card, and we didn't have anything that we could run because we're like, oh, if we send a link or something like that, it could take them 30 days to pay that. so I spoke with Andrew and Derek to say, do either of you have something that we can use coming up that we can test this on? So they both have their eye out for something. We just didn't have anything at the moment.
Christian Sheerer: Okay, no worries. Yeah, and I think even in between now and the next time we check in, something simple, like if you guys run a fake one, like a dollar, that might be useful just to see how the flow works.
Jodie Steen: We talked about that too. Like maybe that would even be a good place to start. Because the other issue is like even people that we have on recurring payments, like that we automatically charge, we don't have visibility to their card details. It's just stored in there. So I don't even have like an auto one that would work.
Christian Sheerer: Yeah, yeah, yeah. And that's typical. And that's why I like the AP and the AR side is like pretty different, right? Like, you know, honestly, you don't even really need to collect AR, like customer information, but like having your vendor information is important, right? As I was talking to our support engineer, like earlier today in preparation for this, that's what he sort of wanted me to communicate. I was like, okay, what is like the extent of this flow in between an ERP that is not QuickBooks Online that we are not integrating with natively, but doing so in sort of like a more manual on our end fashion to sort of give our customers like the white glove treatment of not having to think about it. And he's like, yeah, on the AR side, right? There's like very little that we need to collect besides company name or customer name and their email, right? And what the payment is for and that's tied to a specific invoice on the AP side. Obviously, we keep those vendors with their account and routing number in some CSV that we can handle that transition into zero for you. And so I think transitioning into that bullet point of the agenda, that's sort of the route immediately that I think makes the most sense based on the conversations that I had with our engineers, which is via CSV import. And so what we would do is just give a template that would map well into sort of any ERP zero included and then We would ask for like we said then we would ask for a download from Xero of vendor and customer information that they have on file. So then us have to put that into that template and then push it into nickel for you in the first go around, if that makes sense.
Jodie Steen: Are you meaning For all client information or all existing invoices or all existing credit cards or what are you thinking in terms of exactly what information you would need?
Christian Sheerer: We wouldn't need even their banking information. We would just need client, how they're mapped into Xero as your client. Whether they're typically taking a recurring invoice or a regular one because when we go through, and I'll show you these for the first time, like when they go through, I see if I have a payment link ready to go. I should. I got a reminder. So I sent myself a reminder. Let's share my screen. So we don't need to like collect this upfront because every time they're going.
Jodie Steen: In.
Christian Sheerer: They go in, pay it out, pay it with their card, put their card details, or put their bank details. So we just want to make sure that we have customer information like their email, which it got sent to, and what customer they're for. So that we know, okay, in the first go around when we send them a recurring invoice through NICOL, we already have that customer data. In Nickel. Oh, that's the real.
Colton O'Farrell: Yeah, and more so with the CSV option, it's just since we don't have the native integration with Xero, this is more so just to make it as easy as possible on your end and for us as well, we can just set it up on a cadence. Was curious, were you guys able to get a CSV file downloaded from Xero?
Jodie Steen: Well, that's what I'm looking at is like, I don't even know how to do that. And Hafeez, I think that probably falls more in your territory than mine.
Accounts Payable East at Spectraflow: Can you hear me guys? Hello? Yeah, we can definitely export it. We can export all the information that we want from Xero.
Colton O'Farrell: Yeah, that would be ideal. We have other customers using Xero today, so the team knows the format. We just need to get that from you so that we can upload it into Nickel to make that as easy as possible for all your customers, all of your invoices to show up. And then I think we walked through it a little bit, but you're able to also reconcile if there's invoices that are pulled in, in that CSV file into nickel that have already been paid. You can go into nickel and just mark those ones as paid. But for all the rest, you would be sending those out through nickel so that we avoid that 1% fee with invoice Sherpa.
Jodie Steen: Yeah. So I'm gonna let Hafeez take over now and ask all of the questions because he's probably gonna be like the primary person dealing with all of this.
Accounts Payable East at Spectraflow: Thank you. Thank you, Jodie. All right, so first of all, I think we discussed about how we are going to upload the existing data from the invoices and all the customers from General. So how are we going to handle the regular process, the regular invoices?
Jodie Steen: Yeah.
Colton O'Farrell: You mean just in terms of sending those out to your customer to pay those?
Jodie Steen: Yeah.
Accounts Payable East at Spectraflow: For the payments.
Jodie Steen: Yeah. Yeah.
Colton O'Farrell: Christian, I'm happy to pull up demo if you wanted to walk through it.
Jodie Steen: Yeah.
Christian Sheerer: So we have. Let me pull this into a different, a different window. Okay, so when we do the first batch and we'll set just to close the loop on kind of like the first instance of these. So we'll send a format that's useful for us to pull into nickel for you, where then we'll just merge those CSVs from zero into this format so that we're mapping correctly. and we'll post that into Nickel in your account with your customers, right? And so then we go in, and-.
Colton O'Farrell: Oh, all right, also do you want to share your screen, Christian?
Christian Sheerer: Perfect. Thank you. And so then we have all the customers here. And so I can go in for Christian number two, for example, and I can create an invoice. I can do it on the customer level and say, I don't know, Whatever. For whatever the invoice amount is, set up another recurring one if it's every month or how often you guys are doing it, and then send them an invoice by a payment link. If I already have their payment method on file, fees, I can charge the payment method on file.
Accounts Payable East at Spectraflow: Thank you so much. That is going to be manual input.
Jodie Steen: Can we not import the invoices?
Colton O'Farrell: You can import the invoices if they're in that CSV file. He's just showing you how you could generate a customer invoice just on the customer level. But if we're importing that CSV from invoice Sherpa, we're gonna have all your customers, we're gonna have all your invoices. You would instead just go to the invoices tab and hit send payment. A request payment there.
Accounts Payable East at Spectraflow: Thank you. Let's say if we already imported some of the invoices here in Nickel and is there any kind of functionality that it can send the reminders maybe after 30 days and then do we have that?
Christian Sheerer: Yeah, I sent one here. This one's overdue, for example, is due yesterday. I can send a reminder.
Colton O'Farrell: You can also. Oh, sorry. Go ahead.
Accounts Payable East at Spectraflow: I'm sorry. I'm sorry. Can that work automatically? Like we can set up a process that it should pick up all the invoices which are going to be due. Maybe within 30 days, it should pick up when it once it is due and then it send an auto reminder reminder maybe on 45 days. Can that work automatically? I mean, is there any kind of functionality for this?
Jodie Steen: Yeah.
Christian Sheerer: Colton, can we send automatic reminders?
Colton O'Farrell: I know the engineering team has been building those out. One thing that they're trying to balance is just getting, you know, not annoying customers by sending too many kind of requests there. So right now, how it's set up is you would just hit the little kind of arrows there, or you could hit the multiple checkboxes and send multiple requests at one time.
Jodie Steen: Oh, you can send multiple at once. You can send the same email or.
Colton O'Farrell: So no, it's going to pull up individual boxes for each of those. So if you had a little message that you wanted to type in each one of those, you would be able to do the messages kind of in mass, but have them customized and personalized.
Accounts Payable East at Spectraflow: So these messages can be personalized for each customer, right?
Christian Sheerer: Of course.
Accounts Payable East at Spectraflow: Got that, thank you. And one more thing, this is what we discussed when we are going to import the invoices from zero to Nicole. Is there any possibility that, you know, sometime we can add a payment link on our invoices? Like instead of we import the invoice from Xero and we import into the nickel, instead of doing that manually, maybe we have kind of a payment link which we can attach on our invoices in Xero. So whenever we send the invoice from Xero, they should automatically get a payment link, click on payment link and they go directly to nickel for the payment. And like, you know, go Google as kind of merchant and stripe kind of, they normally offer this kind of payment link possibility. We can do that with this one.
Christian Sheerer: And so, so you could, you could link it to, so we have this, for example, like a payments portal.
Colton O'Farrell: You could be sharing Christian, by the way.
Accounts Payable East at Spectraflow: Okay.
Christian Sheerer: You could link it to your payments portal, which you could set up, right? And so this was, let's just assume it's, you know, the Spectraflow payments portal. And then you could link this to a zero invoice if there's an editable field in that invoice where you just drop that in and then they're paying out against that from here. Or you could go in, and have that invoice get created, this payment link, copy it and put it into the editable field itself for a one-to-one invoice.
Accounts Payable East at Spectraflow: Oh, okay.
Christian Sheerer: So a one-to-one payment link per invoice or the generic portal, which They would then, it would be opened up, so then you would have it. Yeah, whatever the invoice is titled on the invoice that's going out to them in their editable field will have this link to the nickel portal for Spectraflow, and then they type in the amount and the reason for the payment.
Accounts Payable East at Spectraflow: Okay, so that is everything they will see on that. this logo and D Grow Distribution Corporation.
Colton O'Farrell: They will completely customize. Yep, you can customize that all within settings.
Accounts Payable East at Spectraflow: Okay, and can we add any additional field here so they can see the invoice number and maybe they can see the exact amount of that invoice?
Colton O'Farrell: Yeah, that's a great question. Right now, the portal, I know there's a lot of work being done. So this was more so kind of Built as like a backup method for some of our customers. A lot of them will take it and embed it in their website just so they have a place where customers can come in and make an electronic payment. I know they're building out some kind of more functionality. Right now there isn't like the ability to add additional fields in there. This more so was to serve as a backup method, but we are seeing a lot of customers really like this feature. So we are building out some more functionality there. But what Christian was kind of showing you before is we can either send that individual secured payment link on that editable field within Xero where it would be tied to that specific invoice or you could have a like the mass kind of portal link. But more so I would recommend having that portal link possibly embedded in your website and then just do the one-to-one invoice level.
Christian Sheerer: Yeah, because then this is the most specific way the fees for, okay, this is, you know, for this particular invoice, it is this amount there. It's not editable, right? Like, it's like, this is what you're being charged.
Jodie Steen: Yeah.
Christian Sheerer: And, and at what frequency and what payment it is. Of course.
Jodie Steen: Coming back to the question of automated emails, I'm wondering if there's a possibility. Like, I completely understand the complexity and, and the challenge of having many different automated emails for many different States. But I'm wondering if there's maybe something in the roadmap that could be like simply that it sends the email as soon as the invoice is created. Because that's probably like the most routine thing. And as soon as it comes in to Nickel, like it has to be sent out to the client. Like there, there's probably, I would imagine for most customers, no scenario where you have an invoice coming in. to nickel where you wouldn't want to send it out to your client.
Colton O'Farrell: Yeah, that's a great call out, Jodie. And it's actually something we have built out today. However, it is just specific right now with QuickBooks Online. We are going to be having some more of the, like some more of that built out for other ERP systems, but when the APIs are made more available to our customers. So right now that is just a QuickBooks Online integration and it is a toggable field. So One kind of caveat with that as well is that works really well if you're just generating an invoice and you're ready to send it. There doesn't need to be like edits made to that, but if there's people that have to go in, make changes or adjustments there, if you have automation like that turned on, your customer would get an email each time there was like a modification made to that invoice. But that is a great call out and something we're absolutely looking for for more ERPs like Xero, or all the other ones that our customers are using as well.
Jodie Steen: Yeah, understood. Okay.
Christian Sheerer: And these sort of like stopgap manual stuff that we call white glove to take on as our responsibility to link up are stopgaps in between now and when we build either 2025 type agentic integration or an API, you know, more 2018 integration. That's my little heuristic for calling it different YAFEs, right? Like, you know, API, you know, sort of in the past, and their own security vulnerabilities with API, right? Where I think, like, we're trying to think of a way in which we can accomplish the same things as an API without having to link up directly and expose that security vulnerability. But in the meantime, it's like these CSV uploads are supposed to be.
Jodie Steen: Our.
Christian Sheerer: Version of a white glove service to make it foolproof. It's a little bit of manual work on our end that we want to adopt one because it helps us learn and two, because it makes it easy for people to use.
Jodie Steen: We would be able to do the CSV upload as often as we want.
Colton O'Farrell: For Can I, yeah, let's, it's helpful for us to understand more of the schedule or like numbers.
Christian Sheerer: You know, you said that there's, there's gonna be, yeah, there would need to be like a regular cadence for it.
Jodie Steen: I mean, we basically do it at least once a day. So we're, I mean, we're syncing with zero, with invoice Sherpa kind of all the time and it's like automatic. And to explain our workflow a little bit further, like, All of our invoices, I think I mentioned, originate in SIN 7. And so whenever we're in that process of like changing or quoting or redoing, it all lives in SIN 7 and it only comes over to zero when it's final, when it's like 100% done and it's ready to be sent. So. At that point, like the way that I might envision this working, and I don't know if it's possible with like within the framework is like at least once a day then at the end of the day, we would need to upload the current state of all of the invoices that need to be paid. So, you know, there might be two or three new ones from day one and maybe day two, there's nothing and day three that would be like Two new invoices, who knows, it could be your 10. But basically every day we would need to have a current snapshot of here are all of the invoices that need to be paid and we're sending out from Nickel the reminder or the initial like, hey, pay this invoice.
Colton O'Farrell: Yeah, is there a way that you're able to download that CSV from SIN7 on a cadence yourself or it sends you maybe an emailed CSV SMB report and then we could potentially like CC our support on there where they would just make sure that that's they receive it at a specific time every day. I guess what?
Jodie Steen: It would come from zero because that's sort of like our final like since seven is kind of like our everything in progress working and zeros are final. So yeah, we would we would probably send it from there. I mean, basically we're open to any idea. that allows us to not have to manually add in invoices every day and manually send them out.
Accounts Payable East at Spectraflow: Thank you so much, Jodie. And I think I would like to add something here. So let's say we are adding maybe four or five new invoices each day and maybe there is kind of change in any previous invoice which we have already uploaded, let's say any kind of text changes. So, and how we are, I mean, we are going to upload all the open invoices in nickel and that invoice already exists there. So how it, it will pick up that.
Colton O'Farrell: Can you walk us through a scenario where that, that invoice is going to need to be edited? Like, for what reason is Can you just talk a little bit more about some of the use cases there?
Accounts Payable East at Spectraflow: Yeah, maybe let's say we have one invoice and there was a tax charge to them, maybe 7% and later on we discovered that it should have been maybe 0% or maybe it should have been something additional to be charged on that invoice. We modified that invoice and it was a little bit change maybe from one invoice was $100 and then it amended to 110 and then we uploaded it again on the nickel. So we know one the invoice for 100 already exists there. So is it going to replace that one? Is it going to edit that one?
Christian Sheerer: And you're making those edits where? Sorry.
Accounts Payable East at Spectraflow: It is. Sorry.
Christian Sheerer: You're making those edits in since seven or in zero.
Accounts Payable East at Spectraflow: In zero. Okay, so these are very rare. Not normal. Yeah.
Jodie Steen: Or I can think about like applying a credit to an invoice or something like that. Yeah.
Christian Sheerer: And so we can edit invoices in nickel, but edit like a real-time edit flow from zero to nickel. I don't, I can't speak to the possibilities of that. Like I would say, I do know.
Colton O'Farrell: Nickel's not going to allow you to send two invoices that have the same exact name. So I imagine if you have an invoice that's let's just say it's $107 or something, there's that 7% fee. You guys realize that it was actually meant to be zero. If you're pulling in that from like a CSV file and it's named the same, it's likely going to pull them both in, but it's not going to send out like an invoice that's with the same name to the same customer. It would have to have a unique name. So in that case, I'm sorry.
Accounts Payable East at Spectraflow: No, no, go ahead. You mean the same invoice number, right?
Colton O'Farrell: Correct.
Christian Sheerer: Yeah, yeah. And so you can edit invoices in Nickel.
Colton O'Farrell: Yeah, that might be an easier solution.
Christian Sheerer: Like you can go into an invoice, edit it, and edit it here. And then on the back end, it gets reflected. When we push into zero. So that was 2,000 up to 2,700 or 2,000 down to 1,700. Save the changes.
Jodie Steen: All right.
Accounts Payable East at Spectraflow: Thank you. One last question. Sorry on this one. So yeah, so when let's say we have collected three invoices today. the customers paid us. So what is that time period we are going to get that money in our bank account? Normally, what is it?
Christian Sheerer: Yeah, it's two business day turnaround on ACH, one business day turnaround on credit card.
Accounts Payable East at Spectraflow: So let's say one customer paid us today. We are going to receive, let's say they paid us by ACH on Friday. We are going to receive it by Monday, maybe by Tuesday.
Colton O'Farrell: So it is, we're not processing payments on, on like weekends. So we still have like normal kind of bank bank hours and holidays impact that as well.
Accounts Payable East at Spectraflow: Yeah.
Christian Sheerer: So Tuesday roughly.
Accounts Payable East at Spectraflow: Tuesday.
Jodie Steen: Yeah.
Accounts Payable East at Spectraflow: And that is going, that is going to be a batch payments. I mean, maybe we processed, we received five payments on Friday. So those five invoices going to be deposited in our bank account by Tuesday, right?
Colton O'Farrell: We're not going to deposit them as batches. They're going to be deposited as their own individual units. So it should make very easy for you.
Jodie Steen: Yeah, that should make it so much easier. If I'm to understand you, the CSV importing, that would not be done by us. That's done on your side.
Colton O'Farrell: Yeah, just make sure that the field, like the fields are all mapped correctly and so you're not having like an error. It's a very simple process.
Christian Sheerer: The manual workflow on you guys is like just making sure in the first instance that we have the way that it gets exported from zero mapped to our nickel template, which we will send you.
Jodie Steen: So a few follow-up questions to that. So I think you had mentioned there was CSV and there was Another option. Yeah. What was the other option? And is that viable?
Christian Sheerer: We don't I think it's viable today. That is sort of like a 2025 type like a gentic workflow where we would that's something that we're having to build out, which would require a little bit more engineering like elbow grease that I think when I spoke to them, they were like the easiest way today, which It's still manual for us, but borderline automatic for y'all is via the CSV download upload, which we will handle. But that's a whole kind of can of worms on the, it's like, you know, it's just a little bit more elbow grease for us that I think the engineers were like pretty adamant with me on.
Colton O'Farrell: And we'll try to get the CSV breakdown. And we'll try to get some timeframes on that. That's more the agentic AI agents working to get that information from Nickel to Zero, have that reconciliation, or the other option is the 2018 type integration where we have an API that's delivering that information. So those are the two possible future states that we're looking at. But today, something that we can do is that CSV file download, a fee's knows, he'll be able to get that downloaded. sent over to our team. Our team will upload that for you and it will just be in the nickel account today. So that would be kind of the immediate solution.
Jodie Steen: And okay, so follow up to that is if we needed to do that every day, is that viable on your side that we're sending you a CSV every day?
Christian Sheerer: I think that's something that we have to. So what's this, what's the volume every day? You guys, people are sending you payments every day.
Jodie Steen: Yes, so we are generally getting, we have new invoices that come in every day, which that's what necessitates us being, like having to send out payment links every day. And we're also receiving payments every day. Now they're not like a ton, like Hafiz, you probably can speak better about the volume.
Accounts Payable East at Spectraflow: I mean, it cannot be on a daily basis. Sometimes we may receive maybe 5 to 10 payments in a day. Sometimes maybe there's no payment for that day. So that is on the payments, but there should be regular invoices. You know, we have customers. So a customer may be having 5 to 10 invoices. So he's being us regularly on a monthly basis. So payments may not be that often, but invoices can be on a regular maybe on a daily basis.
Colton O'Farrell: Can I, can I, I know we're kind of running up here on time as well, but can I ask, so for the accounts payable side now, you're just manually kind of going in there and creating those. Is there a scenario where you'd be able to get both the AR and AP over to us so that you can also, you know, resend out the invoices for your AR side, but then also we can get the AP in there and you can pay your bills via ACH or credit card, however you're doing that today. Is that like a solution? For you guys, that would make it easier than having to manually go in, create the bills, but also where there is more kind of of that volume that you'd be processing.
Accounts Payable East at Spectraflow: Yeah, I know for now we are doing it manually and there are not many, I think 10 to 13 vendors we are doing right now. But of course, if it is going to be an automatic, that is of.
Jodie Steen: Course, that would be better. The payables are more predictable because we do that like every Friday. And so every Friday there's maybe like, I'm going to say five to 10 different bills that need to go out. And of those, half of our vendors have still not signed up for ACH. So we might have, you know, I'm going to say two to five bills that have to go out. every Friday. So because that's like so much like a lot volume and like that's not onerous for us, but the invoices because there's usually 120 open at any one time and they come and go every day, that would be a lot harder for us to keep track of manually.
Accounts Payable East at Spectraflow: Right.
Colton O'Farrell: No, that makes perfect sense. Thanks for sharing that. Okay, cool.
Christian Sheerer: Yeah, I think there's a. I think there's still a little bit of ideation based on, like, the daily volume of four to five or whatever coming in that I'm gonna have to do with engineering to understand, like, if there's a Cadence that we might propose of doing it on a weekly basis rather than a daily thing, wherein you would still get stuff deposited, it would just be that reconciliation into zero. Christian Sheerer: happening at some other interval.
Jodie Steen: Yeah, that's not so much a problem. It's really just the important piece for us is getting the invoice into Nickel as soon as it's in zero. That's what affects our accounts receivable. Yeah, if we let's say we do it weekly and we have an invoice that was ready Friday at 5:00 PM and it's not going out until next Friday, we've lost seven days of, of course.
Colton O'Farrell: And we want to. Yeah, yeah, I would say maybe too, even if it's something where we do like by week or where it's twice a week, something on the front end early in the week and then later part of the week, just because they're, you know, that maybe we do a Tuesday to Friday thing just to make sure we're kind of having the best coverage for when those invoices come in and are sent or, you know, with the zero reconciliation.
Accounts Payable East at Spectraflow: Mm-.
Jodie Steen: Yeah.
Colton O'Farrell: But that's definitely something Christian and I will run by our engineering team. So we don't have a great answer there, but what I can tell you is that we do that with many customers today. So we don't see it being a problem. It's just more so the kind of cadence and also just, you know, having this be kind of the interim solution until we work on a more long-term.
Christian Sheerer: Kind of better fit.
Jodie Steen: And what are the clients that you're doing? this with already, like, tell me more about that. Like, what is the workflow for them?
Christian Sheerer: They're, they are batching up at a, like, more distributed cadence. Like, it's like weekly or a couple times within the month. Um, and they're processing like a lot of payments at once. And so they have it.
Accounts Payable East at Spectraflow: Yeah.
Jodie Steen: So are they, like they don't have an issue if it's like a week or two week lag?
Christian Sheerer: No, no.
Colton O'Farrell: It depends I guess on some of these customers have net like terms that, you know, increase.
Jodie Steen: I see.
Colton O'Farrell: Okay. It kind of depends more so the specific relationships they have with their customers. If there's some voices that they're not needing or expecting to be immediately paid for, those they will have like together into kind of a batch. and send that, but if there's any-- it makes sense.
Jodie Steen: I understand. Okay, so that's important. So I'm going to throw out a scenario and Hafiz, this is probably specific to us, but when we create an invoice that is finalized, we send that. Usually we send that from SIN 7. Okay, and then it goes to zero. So maybe it's like, maybe it's not as important if the client is on 30-day terms like you're suggesting and they have the invoice and the clock is ticking, that you're saying the payment link just wouldn't be available for a few days or a week. But in that case, they're not really going to be using that anyway. Is that the piece that you're running into?
Colton O'Farrell: Exactly.
Accounts Payable East at Spectraflow: Yep.
Jodie Steen: Yeah. Okay, yeah, so it's more for like, let's say clients that do not have terms that need to pay immediately. Or. The client, you know, in the rare case that's like, I'm gonna pay this a couple days after I get the invoice or something like that.
Colton O'Farrell: Exactly.
Christian Sheerer: I mean, and you could always just like shift the invoice creation process to happening through Nicholas, right? You create the invoice right away and then push it.
Colton O'Farrell: Because of the SIN 7.
Jodie Steen: Because of SIN 7, it would be, yeah, that wouldn't work. But I'm glad that you walked me through how other people are using it because I can see how maybe that. Like. We can talk about it internally about how many of our invoices would we actually need to have a payment link for immediately versus how many would be okay if it was a few days later? Yeah.
Accounts Payable East at Spectraflow: And I think for anyone who is not on Circleback, maybe we can add a general payment link. Exactly. So whenever they receive an invoice, they have at least a general payment link. So that can be a special.
Jodie Steen: That just wouldn't be attached to an invoice or like an invoice number or like come up as like you owe this, but rather they would just send.
Colton O'Farrell: It to accounts payable. It wouldn't be that one to one link. It would more be like the payment portal where it would say, I don't know, still list their amount. They could still pay you at any time with that link. They just want to be like this, like the specific invoice link tied to that invoice.
Jodie Steen: Yeah, understood.
Accounts Payable East at Spectraflow: Okay. And one more thing regarding the ACH, is there any kind of limit on ACH we can collect? okay. Yeah.
Colton O'Farrell: So for the nickel plus members, you can do up to a million dollars per ACH transaction, and that's unlimited. So you could do as many as many as just the, the one million dollars, like the per ACH kind of soft limit.
Accounts Payable East at Spectraflow: Okay. Okay.
Jodie Steen: Okay. Cool.
Colton O'Farrell: Are there any other, I know, appreciate you guys taking, you know, going over a little bit time here. Are there any outstanding questions? I know Christian and I have a couple follow up to do with the engineers and just learning a little bit. a little bit more about kind of ideal or use case or what's worked well for other customers. And now it sounds like you guys got to get that CSV file from Xero and then also kind of, you know, evaluate customers in terms of what you have set up for terms with them and if there's invoices that are going to be more critical versus those that are going to, you know, it'd be okay to take a few days before sending those out. What other aspects am I missing here?
Jodie Steen: I think for us, it's probably just like we need to go through and think through how this would fit in with our process, like, and what we, what things we have the flexibility to change and, and what things are like kind of hardwired that we just, we can't change. And probably Hafiz and I have to have an internal conversation about that. and then also to test it and which we want to do, we just have to find like invoice or like you said, we can make like a dummy one and just see how that works.
Christian Sheerer: So yeah, we'll do this. I will get the template that we typically send over for the ways that, you know, as CSV should come into Nickel. And then Just help from the CSV that you guys get from zero, just help merge those should be pretty simple to do. And then we can go from there in testing like an invoice getting sent out and then that link up and provided what comes out of that internal conversation about what can change and what can't, I think it probably warrants another conversation where after this test we then think through, okay, based on what can change, where can we meet Spectraflow where they're at, and like what, where can we, if it so happens not, right?
Jodie Steen: Yeah, I mean, I'm more inclined, like we have done a bunch of research and, you know, I understand Melio is like the one that integrates, but there's certain core functionality that you have that they don't have. So if there's a way for us to make this work, I'm inclined to do that. And we're already set up on the payable side. So I think the transition would be pretty easy. So I think from our side, it just hinges on the workflow of are we able to consistently get invoices in to the platform.
Christian Sheerer: From zero.
Jodie Steen: From zero and send them out, you know, and the real wish list would be send them out automatically when they hit. Yeah.
Christian Sheerer: Okay, I got you. No, no, that's, that's clear to focus in on that because there's a lot of stuff going around. Um, and it's pretty simple to get from nickel to zero.
Accounts Payable East at Spectraflow: Right.
Christian Sheerer: Like, it's kind of like, and that can happen on whatever cadence, but yeah. And I actually identified in an ideal state.
Colton O'Farrell: I think I, I mentioned this last time we spoke, but I actually got some more confirmation from our CTO that we'll actually be building out a direct connection with zero in the future.
Jodie Steen: Oh, great.
Colton O'Farrell: I didn't think we would be just because zero purchased Melio and you mentioned them. We actually got some more insight that they changed some of their pricing. So they already have the same issue that you're dealing with with invoice Sherpa, where they're charging 1% for ACH fees. But they also changed some more of their pricing. Our CEO is actually going to be putting out a new blog article about their pricing updates. So that's maybe something to just keep in mind there. But we will have a integration with Xero. It's just in the meantime, the CSV is just that kind of Band-Aid solution to make it simple on your end.
Jodie Steen: Yeah, well that's good to know because that also moves the needle a little bit that it's like, okay, if it's, you know, something that we have to live with for a period of time.
Colton O'Farrell: Exactly.
Jodie Steen: And then there's a better integration that's coming that, you know, that could make sense.
Colton O'Farrell: And we're happy to get more timeline specific on that. I know QuickBooks kind of desktop is the main one that's going to be launching very soon just because there's a pretty big need there. But I know zero is right behind that.
Accounts Payable East at Spectraflow: So.
Jodie Steen: Right. Okay. Hafiz, did you have any other questions before we?
Accounts Payable East at Spectraflow: Yeah, yeah, yeah. Just a few minutes. So, sorry, I forgot to answer the question is, let's say when once we received a payment, is there any possibility to issue a partial refund or a full refund? within platform?
Colton O'Farrell: Yes. So I know this came up for another customer the other day, and let me just pull up what the specific.
Christian Sheerer: Sorry, one second.
Colton O'Farrell: So for in regards, this is about partial refunds.
Accounts Payable East at Spectraflow: Partial or full for refunds. And are there any fees associated with the refunds.
Colton O'Farrell: So how it were, it depends if it's with a card. So I know the card network charges like an interchange fee. So a card fee does apply. It's typically paid for by the customer, but if it's being like a partial or full refund, then there's a card fee that would apply and is typically put back would be put on yourself. In the case of a refund, the card fee won't be applied twice. It will just be transferred from the customer to you. But if you're refunding the customer fully, you can tell the customer that the card was already charged and then you can refund them minus any kind of charge fee that you would have incurred. And if there are cutoff times that apply to those charges when they're submitted for settlement, it looks like there's like a specific cutoff times for that. So if you are able to catch it quickly, Typically, you can avoid that altogether. It's usually a pretty short window, like an hour. But in the case that you are charged by the credit card interchange kind of network, you could do the partial refund and just subtract any kind of card fee that you acquired. But there wouldn't be like any kind of fees associated beyond the credit card fee if that's what they were using.
Accounts Payable East at Spectraflow: Got it. One last thing, sorry. and let's say we have a CH information, or maybe we have a credit card information for one particular customer. And instead of they are processing the payment, we want to process. Let's say the invoice is due. We can do that, right?
Colton O'Farrell: Yeah.
Jodie Steen: Yeah.
Christian Sheerer: You just have to send them authorization form through us because we're going to be pulling the payment, and so they just have to redo authorization so that.
Colton O'Farrell: When you're setting up customer, you can automatically just send them a form to fill out where you can set criteria, either like a specific dollar amount. You can also have like timeline expiration or just there's no expiration there. And then as long as it fits within the parameters that have been outlined and agreed to, you just be able to automatically pull from their account.
Accounts Payable East at Spectraflow: Got that. So can we also process payments manually? Like let's say they have any outstanding balance from the past period and this confirmed us that we are put to charge. So it's just possibility that we can process it manually from the platform.
Colton O'Farrell: Yeah, when you're saying process it manually, are you saying so if they give you that card authorization, you would automatically be able to charge the card on file and they would get a receipt. It's saying that this, you know, payment has went through. Yes, absolutely.
Jodie Steen: There's times when our clients just give us a card over the phone and they want us to key it in. So are we able to do that?
Accounts Payable East at Spectraflow: Yes.
Colton O'Farrell: So we have a.
Accounts Payable East at Spectraflow: I'm going to.
Colton O'Farrell: Share my screen really quick to.
Christian Sheerer: Let'S.
Colton O'Farrell: See, we have this form. I can also send you a template of as well that you can send to your customers. and if they want to, they can also only put in for the card number because we're trying to obviously keep this secure, just put in the last four digits. That also works fine. If they give you a card over the phone, there is a section within Nickel where you can automatically go in and enter the card information. So that when you're sending out the or when you're adding the customer, we can either send them a form to fill out the information or if you have it, you can go ahead and enter it yourself. if something like this would be helpful, we're happy to send that as well.
Jodie Steen: Yeah. Or maybe we just send them Hafeez, like the portal and say, if you want to pay.
Colton O'Farrell: So that is an actual payment.
Jodie Steen: Here. Here's the link.
Accounts Payable East at Spectraflow: Pay, you know, that makes.
Jodie Steen: Sense.
Accounts Payable East at Spectraflow: Okay.
Christian Sheerer: So, yeah, let. Let's let us follow up on those. So I think. homework on both sides sort of clear. If we run some tests, that might be good. We will send over that CSV template that will help us bring stuff into nickel in the first instance and then give the full breakdown on this pulling invoices from zero on a recurring basis. Where do we need to meet you guys where you're at? And then the final thing is just give a full breakdown so you guys have it in your back pocket on those three options that we just talked about in terms of authorization, whether it's via the payment portal, via the setup authorization or that credit card authorization form that Colton issued.
Jodie Steen: Okay, yeah, that sounds great.
Accounts Payable East at Spectraflow: Okay.
Christian Sheerer: Should we get back together next week?
Jodie Steen: I am probably out of town.
Christian Sheerer: Oh, yeah, yeah, yeah.
Colton O'Farrell: Out of the country, so I'm going.
Jodie Steen: To be out of town. But maybe like after Labor Day. Okay. Yeah, the second I'm in the office and the rest of the week I'm with clients. Yeah, the second could be a good time.
Colton O'Farrell: Yeah, let's touch base on the second. I think that's a great idea.
Christian Sheerer: Does the same time work usually? Like 11 a.m.?
Jodie Steen: That's good for me.
Christian Sheerer: Awesome. I'll just send out the invite to everybody right now and then we'll get to work on our homework items.
Jodie Steen: Okay. All right.
Colton O'Farrell: Thank you so much.
Accounts Payable East at Spectraflow: Thank you.
Colton O'Farrell: Have a great rest of your time. And Jodie, I hope your daughter has a great birthday.
Accounts Payable East at Spectraflow: Thank you.
Colton O'Farrell: Thanks so much. Bye.
Accounts Payable East at Spectraflow: Bye.

---

**Recording:** https://storage.googleapis.com/saved-meeting-recording.prod.circleback.ai/meeting_3464269.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=circleback-ai%40appspot.gserviceaccount.com%2F20251022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251022T153200Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=93e0637a8ee82a8d1f08d53c7363fe78f0b86dbbc3170bbe3b82366992e43ed60b0106f2922e2146a25cf505d358c99c3cf2d329d94aaf736e666a3b0b4ffed128cb8d67624ea79dc89435c749944fffbcc81cb1726301a6aa22bc658f0b2754a87bace29f45fba43f266bd4e8fa18165b82a6bcaa39fd08a46074cb6ef99298e2e8637db986c76f22abfa34ad2abeaf55fa130d1462780fe1339505f5830c39843e18b3ad724e3873a2fe9513f51dd366ca6a566212ea3bb178fd0fee97991a47c3244f17ee99d99a73f55d486e78ee1fd5b5a075e55b5d7599866fd2d6c4af368a3a8973e9412eaf4bf5ed051661b32b7df4db7288b441d65b5311395234c8
