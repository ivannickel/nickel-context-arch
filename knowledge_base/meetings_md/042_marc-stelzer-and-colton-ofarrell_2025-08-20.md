---
title: Marc Stelzer and Colton O'Farrell
date: '2025-08-20'
time: '19:00:18'
duration_sec: 1503.71
duration_min: 25.1
participants:
- Ivan LaBianca <ivan@getnickel.com>
- Claudio Wilson <claudio@getnickel.com>
- Najeer Ahmed <najeer@getnickel.com>
- Colton O'Farrell <colton@getnickel.com>
- Marc <marcs@renewal.com>
- keith <keith@renewal.com>
source: Circleback
meeting_number: 42
extraction_priority: medium
extraction_priority: medium
extraction_priority: medium
# === STRATEGIC CLASSIFICATION (Transcript Classifier Agent v1.0) ===
call_type: review
deal_stage: active
customer_segment: whale
has_pain_points: true
has_objections: false
has_competitive_intel: false
has_use_case: true
has_pricing_discussion: true
has_integration_needs: true
primary_industry: construction
transaction_volume: above_threshold
ar_vs_ap: both
processed: false
dimensional_extracted: false
extraction_priority: medium
---

Colton O'Farrell: But I'm moving. Oh, dude, I got issues.
keith: All those shelves right there are normally covered with what I'm seeing with figures. I see company stationary in that cabinet. Oh, I'm.
Marc: I'm God. How do you blur? How do you blur?
keith: Alexa, blur my. Elon. Elon, blur my background. That's awesome. Well, hey, I'm.
Colton O'Farrell: I'm appreciating all the. The Star Wars memorabilia I see there, too. So big Star Wars fan.
Marc: Stop it, Colton.
keith: I liked you Tons before you said of that. it is not even behind you would be even more impressed. We'll do another Zoom call just so you can look at my office when I remodel.
Najeer Ahmed: Yeah.
Colton O'Farrell: Awesome.
keith: So I got a Death Star poking out of the wall up there. See it?
Marc: Oh yeah.
keith: That's the Death Star, yeah.
Colton O'Farrell: That's super cool. Yeah.
Marc: So are we gonna, should we share your screen, Keith? Is that probably the best way to do this?
keith: If I can even figure out how to do that. I mean, I'll do it then.
Marc: Right, Colton, is that the best way to end?
Colton O'Farrell: Yeah, that'd be the best way. And then Marc, just on your side.
Marc: We have Najeer, one of our head engineers. I saw Najeer, thanks, brother, because you've helped me a little bit. I appreciate it.
keith: I appreciate it. Let me share my screen.
Marc: I hope that crane doesn't fall down behind you. That's scary.
Colton O'Farrell: Yeah.
Marc: You guys see everything? Yep. Perfect. No Pornhub or anything. Okay, here we go.
Colton O'Farrell: No. So.
Marc: You know, Colton, to start with, I think at a higher level, you might have heard, I don't know if it was Najeer that helped me or I forgot the other gentleman's name, but we stopped having it sync back the invoices as paid to QuickBooks because we already have Salesforce telling things that are paid. And because Keith and Rod and some other people in my company need to watch that from a production management standpoint of when things get paid. And because they don't really have visibility in QuickBooks, they need to do it from the Salesforce side. So you guys did some custom coding to shut that off. I can't tell you how badass I think that is for how reasonable this costs. So I just want to start by saying that.
Colton O'Farrell: Much appreciated.
Marc: Thank you. Yeah, I love the fact that you guys bring the invoices in and I think you do too, but I think one of the main things I know Keith is going to talk about today in construction, people will often order us, order from us on a contract. That's called an invoice. Let's say it's $20,000. Then along the way, they're like, Hey, I want another window, another $1,000. I want change it to black windows.
Colton O'Farrell: That's five.
keith: Permit. Permits almost on every job.
Marc: Whatever. And then, oh, reduce two windows. I've decided not to do this. So there's multiple invoices or credits, and the problem is sending them five invoices and asking them to pay is weird. So what we're fine with doing a workaround is doing manual and not really because we can't send unless there's a way and I mean, I'm bringing this up that we could sum up, but I don't think you have that. But you know, Ray said, Hey, we'd love to know what you think about, you know, maybe there's a roll up if that sounds smart or makes sense to you from a programming standpoint that we could, you know, click like roll this, this, this and this are all the same client into one invoice or one payment request. Maybe that's a future thing I would.
Colton O'Farrell: Actually Najeer, if you want to take that one.
Najeer Ahmed: Yeah, it's actually definitely something we've been thinking about. It's probably something that we want to do soon. And it would work exactly as you're saying, right? Like the same customer has 10 invoices with you, they can pay them all.
Marc: It was like a statement. Yeah, pay off the statement amount.
Najeer Ahmed: Right, exactly.
Colton O'Farrell: Right.
Najeer Ahmed: That is something we're thinking about. And I think that would solve the issue for you guys, right?
Marc: In that regard, I mean, as long as it was something like, let's say these were all the same client, David, Carol, and then there's different invoices for little different amounts, and we could do something like click, click, and then find the invoice.
keith: Can I add something to that?
Colton O'Farrell: Yeah.
keith: So it would have to be, it would, if for that to work, it would have to enable me or whoever the user to be able to click some of them, but not all of them, because for instance, We have window jobs that also have siding jobs. And when the windows are done, we're holding out our hand to get paid for that phase. But you know what I mean? So as long as we have the ability to actually like, oh, there's four of them, but I only want them to pay three of them.
Marc: Yeah, I would imagine if it's click, I don't think that would be.
Najeer Ahmed: Yeah, but yeah, that's important point. That's interesting. And that's definitely not an angle we've thought about where you want to withhold certain invoices, right, from payments. to certain customers.
keith: I guess in that scenario, maybe it isn't as big of an issue because we use different POs for the siding versus the windows. So like if this guy had Carol had a window or siding job, you know, it'd have a W or an S after it. So those are kind of technically different POs, but they're all for the same client account. you know what I mean?
Marc: So maybe, yeah, it depends how you guys group them. If you group them by client name, then that would be problematic for us. If it was completely choosable by us, that'd be the best way that you don't pre-group them, that we could assemble different ones, even if we did it by mistake across different clients, but want to email it to, that's up to us. If we have that full flexibility to grab different invoices and, and merge them into one, invoice we're looking to get paid up that I think, right, Keith, you'd love that.
keith: Yeah, even if it, if, even if it won't, if the functionality only works for the ones that are not combo jobs and I have to do the manual invoice for the combo only jobs, that will still narrow down the amount of those I have to do. And it would just to have that ability for the ones that it works for would be great.
Marc: Yeah, we're five minutes in, we don't have, and that's a future thing. So I think giving you guys something. visibility as to what we'd love to see and I'm sure your users would love to see and you know, people would make adoption easier would be great, but we have to talk about now because a couple things. So, Keith, you're gonna probably take over, but I yesterday made this little play around dollar 10 thing just to see what you were. I was trying to tech support Keith to see if I could figure something out because he couldn't find a way to do something and I'll let you take over Keith, but I built this and then I said, oh, I can't delete it. He goes, yeah, that's on my list to talk to these guys about.
Colton O'Farrell: Do you want to try, can you just click into, so over by where it says 435-235. So, okay, and interesting. Typically there should be a delete button next to that.
Najeer Ahmed: Yeah, so this is something that we also want to do right now, the way to delete an invoice. And the reason you can't delete it is because you're synced up to QuickBooks. We kind of had this philosophy of like, okay, let's not delete things from people's QuickBooks accounts.
Marc: Yeah, I think our answer was going to be the thing.
Najeer Ahmed: And so, you know, we'll let them delete it from their QuickBooks, like on the QuickBooks website. But we can actually, I think we're finding more people asking for this. So we could probably pretty easily give you that delete button and it would delete it from QuickBooks as well.
Marc: By the way, please actually delete this one.
Najeer Ahmed: This was a test.
Marc: So 455 after we're done, if you don't mind going in and grabbing that and Sure. just deleting it. Definitely.
Najeer Ahmed: I can give that a shot.
Marc: So it's another future thing that it sounds like, you know, on a lot of these things, like in Salesforce, it's vote ups. You are hearing vote ups for maybe merging invoices in some way, and you're hearing vote ups about being able to manually delete. And the thing, you know, with us, we're not having you send them back to QuickBooks. So that whole concept is obviously unimportant to us that we're breaking that links and that syncing. We just want to be able to lead it. Honestly, we're seeing and maybe you're freaked out by this, but it's probably good feedback. I love the idea of the syncing back and forth. And I really love you bringing them over because it pre-fills things down. But I think Keith and I are most excited about just this as a payment platform. As crazy as it, I don't know, maybe you're going, that's wow. I don't care why you like us, but we like this ACH. I like your reasonable 2.9% fee on the Credit card, I like your reasonable $420 a year thing. But we're seeing these little things that are just problematic and we're trying to work around. For sure. For sure.
Najeer Ahmed: I mean, we really appreciate people like you that are willing to come onto calls with us and give us feedback and work with us actually to make the product even better. So we appreciate that for sure.
Marc: So Keith, I think this is where you should take over on the bigger scarier issue we're having. one yesterday that kind of, and any others?
Colton O'Farrell: Yeah.
keith: So I think the bigger one is when I'm creating- Tell me what you.
Marc: Want me to click into. Maybe you'll have to do it on your side and I'll- well.
keith: We want to create a new invoice.
Marc: Okay.
keith: And this is up at the top.
Colton O'Farrell: So invoice, right side, new invoice.
Marc: Yep. That's what we did yesterday.
Najeer Ahmed: That's right.
Marc: Let me move my screen thing. Okay.
keith: And then we want to use Javeri's PO, so it's JHA-250106-S. Got it. So see how it automatically has QuickBooks sync enabled?
Colton O'Farrell: Yeah.
keith: We don't want that. And if I miss that, then it's pushing this new invoice to QuickBooks. But When you try to create this invoice with that button off, like unclick the button, Marc.
Marc: Got it.
keith: Yeah, turn it off. And then just put whatever dollar amount, I guess. It doesn't really matter because this is going to be another sort of phantom. And I think.
Marc: Invoice number, just anything.
keith: Yeah, I don't think that really matters.
Marc: Right, we don't care about that.
keith: And down at the bottom, it should say Create.
Marc: This one worked.
Najeer Ahmed: Yeah, so let me interrupt here. I noticed, so we had seen the errors coming in from your account yesterday. I went in and fixed the issue. So now you should be able to make those.
keith: So the fill to create QuickBooks invoice business validation error, that was what was popping up before. Okay. Is there any way to remove the.
Colton O'Farrell: The sync button, is that what we're talking about?
keith: Or remove it would be grand, but you mean at least make it so that the default is disabled. Because if I'm moving quickly, you know, I might miss that.
Najeer Ahmed: So do you guys actually not want any thing to come back to QuickBooks? Is that like your preferred?
Marc: Yeah, because I think, Keith, tell me if I'm wrong here, but I think because Salesforce, we have a sync. with a company called SyncQ that brings everything in from Salesforce. Yeah. To us, all, everything is done in Salesforce and it pushes to bill.com, it pushes to QuickBooks, it pushes to other things. It is the one place that we, if we have multiple clocks with all these different, forget what you call these type of programs that sync together. They're called, there's an acronym, right? ISP, ASPs, whatever it is. You know, we've obviously done all these things that But we, you know, the one thing that lives in the center, the one thing that is the hub for everything that may sink in and out is Salesforce. And Nickel now is one of our, looking like to be one of our, you know, big things that we're gonna use a lot. But because of functionality between Salesforce and QuickBooks, we can't use your, we want, we love bringing over invoices because again, it plants the seed from which we can use to maybe create an invoice in some cases. Other times we have to do it manually. But we never, I don't think we want anything ever going back into QuickBooks. Anything. Got it. Okay.
Najeer Ahmed: So I think that should be a pretty easy change for you guys as well. Basically what I'll do is I'll make a setting where you can like disable by default the sync for certain things. And that sounds like that'll take care of that.
Colton O'Farrell: Yeah.
Marc: We would see it. And by the way, here's another one you got to get rid of since I can't delete it for the dollar. I won't take this.
Colton O'Farrell: Well, actually, well, is that one not gonna, Najeer, is that one not gonna allow to delete because the customer is pulled from QuickBooks?
Marc: Let's take a look.
Colton O'Farrell: Oh, because it's manual, it may be able to, right?
keith: So you can delete. Yeah.
Marc: Oh, you're right. There it is. So it actually has a delete button. Okay. Okay. So, oh, that's interesting. So anything pulled over we can't delete because of the priority of you didn't want this So thing, JHA but anything we manually Javari, do, okay, let's start this that's again.
Colton O'Farrell: Good to know.
Marc: So Yep. just knowing Yeah. what it sounds like you're going to do, you're going to have this pre-grade out for us like that.
keith: Yeah, that should be the default.
Marc: That'd be awesome. Yeah.
Colton O'Farrell: Yeah.
Marc: And that kind of makes sense since you're not sinking payments. Yeah, we don't want this either.
Najeer Ahmed: Yeah, yeah, you're right. I mean, we really want to ideally have this whole, like, you can pick and choose exactly what you want to send.
Marc: Yeah.
Najeer Ahmed: We're just not there yet.
Marc: Yeah, I get it. And I also know the more you complicate, it makes it really great, but it also makes integrate, you know, it's a bigger program to learn. Like just, you know, your thing is so easy, for example, compared to somebody.
Najeer Ahmed: Starting in Salesforce, they're like, oh my God.
Marc: There's a billion things. But once you master it, it's amazing. So, Keith, I don't have anything else.
keith: But I know you have the QR. You have any program other yet, topics? right? No, There's no, no so QR there.
Marc: Is no code recommendation. system for this.
Colton O'Farrell: Yeah, so if you click at that payment portal button right on the screen, the purple one. I'm sorry, I'm stupid.
Marc: No, you're good.
Colton O'Farrell: So it's rate versus invoices. Start accepting payments by creating that purple payments portal link. Oh, God, sorry. Yeah, so if you take, if you copy this link and then go to QR.io, you can paste that link in there and it will generate Where a you QR code.
keith: Just, yes, that's right.
Marc: I couldn't replicate this.
keith: Yeah, so you have to use a different program basically to pull it into it.
Marc: So once we get it, we're done.
Colton O'Farrell: Yep. So you just go to QR.io, that top one, paste that link right into, I believe it's in the middle of the, oh, let's see. Unless they did an update. Let me see if this is a new web page. Yeah, I'll put it in the chat here.
Marc: This one.
keith: Oh, yeah, I see it.
Colton O'Farrell: So if you paste that into.
keith: Right.
Marc: Yep.
Colton O'Farrell: That box right there.
Marc: There it is. So that's. That's. And we download it.
Colton O'Farrell: Yep.
Marc: I'll set it to Keith. And then this is the one we can give it to our installers.
Colton O'Farrell: This one? Yeah. And this one does have. It looks like with this account, there was, like, a free trial so that. they, you would just have to make sure they're not deactivated. You might have to have some kind of plan with, with these guys for having the active QR code. But what this will do is your, your guys can have it on their phone. Customer can scan it. They can pay you for free or with their bank via ACH for no fees, or if they want to pay via credit card, they can do that. There's a 2.99, but this would allow them to make payments on site.
Marc: All right, I'll look around and see if there's any other free This, ones.
keith: The And QR if not, thing you is know, not like I massively might be one.
Colton O'Farrell: Important Perfect. to me.
keith: It's snazzy, it's cool, it's kind of, you know, new age, you know.
Colton O'Farrell: Well, dude, we could put it at.
Marc: The bottom of our, a lot of.
Colton O'Farrell: People print it off too. You can always print that off and.
Marc: That would work as well. Because that might, you know, somebody's showing them a phone, that might freak them out if one of the guys says, hey, you pay right here and they're like, and I know it ultimately will go to the American Home Renewal But thing with we our could landing put it on page, the completion with our picture. document and that might make people feel better. But we'll figure that out. It is snazzy.
keith: So question, in that scenario, if I print a QR code on Friday and give it to my guys for their job they're doing next week, and then next week the invoice amount changes and they scan that code, is it going to pull into the newest?
Colton O'Farrell: So this, the code there would just be like the payment portal. So when it gets tied to a direct invoice.
Marc: Okay.
Colton O'Farrell: Okay.
Marc: Yeah, it does, it's not a locked in amount specific to that invoice and amount. It's just, here's how you pay us. So it needs to be entered.
Colton O'Farrell: Yeah.
Marc: It is.
Colton O'Farrell: Najeer, do you want to add anything to the kind of payment portal or the QR code? Yeah.
Najeer Ahmed: I do want to flag one thing for you guys. So if a customer has multiple open invoices right now today, They can see a list of those invoices on any of their active links. So if you wanted to go and take a look at one of your payment links, you might be able to see what I'm talking about. Or I could show you an example as well. So yeah, if you just go to nickel. And let's take a look at DEY 2412. You can get either of those. Copy paste the link.
Marc: What do you want me to do from here?
keith: Copy that link.
Najeer Ahmed: Oh, you can just click on it. Sorry.
keith: Got it.
Colton O'Farrell: Nice.
Najeer Ahmed: And then just paste that into your browser.
Marc: Oh, that's interesting.
Najeer Ahmed: So yeah, in the bottom left, they'll be able to see just it's kind of not so good.
keith: He's going to have a lot because this is a great example. This was the one where I typed 400,000 instead of 100,000 and then it won't let me edit that number. So I had to start over. I couldn't just go into the invoice before I sent it. and edit the amount and just fix it. I had to create a new one. And then he was like, oh, I need two separate ones for 50 each. So he has tons of invoices that are not applicable.
Najeer Ahmed: Then you can delete it. Yeah, I see. Yeah, I'm going to get that delete function for you by today or tomorrow, and I'll let you know when that's available.
Marc: That's crazy that on a program like this, you can just give us custom functionality. I really, I can't tell you how much I applaud this. I'm shocked by it.
keith: And I wrote to Ray of like.
Marc: That, but I'll maybe have to write to Ray again. I really think that's just.
keith: Let's tone it down a little bit, Mark, because next year it's going to be 400. No, no, no. There's going to be tariffs, you know, next thing you know, it's 425 a year.
Najeer Ahmed: I mean, come on. Yeah, yeah, we got a good team. I appreciate that.
Marc: Where are you located, Najeer?
Najeer Ahmed: I'm in Nickel headquarters, which is in Brooklyn, New York.
keith: Nice.
Colton O'Farrell: Yeah, next week I'll be heading to Brooklyn to join the team. I'm just based in Chicago myself.
keith: Oh, right.
Marc: I think you told me that last time. Dude, I'm Sheepshead Bay, dude, Avenue X.
keith: Nice.
Najeer Ahmed: Nice.
Marc: Sheepshead Bay, Brooklyn.
keith: Right on.
Marc: What else you got? Anything else?
keith: I'm from Jersey. I'm way classier than you, New York guys.
Colton O'Farrell: I was just curious, have you, I'm curious on the feedback. I know you guys have done some transactions. What have you guys been hearing kind of from customers? They find this pretty slick. They, are they, what's any, I wouldn't know anything.
Marc: You got the guy that's really spearheading everything in Keith. Yeah.
Colton O'Farrell: Curious what your customers have been saying.
keith: Customers like it. I mean, it, I, this is something that I used to be asked for, you know, periodically, not, not all the time, but people would ask when we're When we're closing out the job, finishing up, and I'm talking to them about how did it go? You know, and they'll say, some people will literally say, yeah, just send me the electronic payment. Like they sort of, some people expect that.
Colton O'Farrell: Yeah, definitely.
keith: You know, usually probably in the Bay Area. Techy people. Yeah, they're sort of used to paying that way. And so sometimes I'm like, now you're gonna hand us a check, you know, and they're not put off by it or whatever. It's just, but yeah, so I think, customers appreciate it. I appreciate it because it makes, there's facets of my job that it makes a lot easier, meaning if people are mailing me checks, I have to implement a system to, you know, six days from now when I invoice them, like, where's the check? And then easily half the time it's like, oh, I left it on the counter. I didn't put a stamp on it. I forgot.
Marc: Now you're giving him too much value and they're going to change my price next year.
keith: 420 21 a year.
Marc: Yeah.
keith: So that, you know, that's great. That makes it, it's easier to get paid and, and it, you know, it, it makes it pretty seamless in, in that regard. Some people still want to hand us a check, you know, but it's definitely saving me some time. And I, you know, I already have enough things.
Marc: The more we have Natalie away from depositing and checks and all that stuff, the better.
keith: Yeah, for sure, because Michael in case. me minimum wage. So, I mean, I, you know, I only have so many hours in the day I can chase people around for Mark's money.
Colton O'Farrell: Right.
Marc: I got a question. I almost last asked it last time, but at 420 a year, 2-9 on Visa, which a lot of stuff is not Visa. How the hell are you guys making money? What's, what's your, how are you money? Yeah. No, that's not anything on the ach's.
Colton O'Farrell: Yeah, that's a great question. So, I mean, I think we, we maybe touched on this a little bit in one of our Last conversations, but so Nickel started in 2022. There was a lot of companies that were providing like free ACH, there was bill.com, there was Melio, QuickBooks Online. And then overnight, basically one of them changed where they decided that this was a like revenue stream for them that they could make money. They had a lot of customers that were paying nothing. And overnight they started paying hundreds or thousands of dollars a month, pissed off a lot of people. Nickel had already existed and just decided that this was a really good opportunity for us to really establish the brand and credibility with these customers who were burned by some of our competitors. And we found out that it's kind of the network effect. And once you have you provide a service that helps a lot of companies that, you know, they weren't getting elsewhere, they're going to be raving about you, they're going to be posting reviews, they're going to be posting in Reddit. And then with all this like AI, large language models using all of that data, Like we find Nickel is typically one of the top three recommended when customers are looking for an ACH solution now because we've provided such a great service. And even if our customers aren't paying us, like they're on the free plan, maybe they're more of a small, mom and posh style shop, there's a good chance that one out of five of their invoices from their customers will at least be paid for with a credit card. So even if they're not making us any money, likely their customers are, and we're already a profitable company. We have over 10,000 customers who are using us for AR, AP or both. And yeah, it's just we're getting a ton of referrals and that kind of network effect. So we're really happy with the progress and growing like crazy right now.
Marc: So how does Keith and I invest?
Colton O'Farrell: Yeah, unfortunately, I'm not the right guy for that, but Ray definitely would be up your alley as somebody to speak to about that.
Marc: So yeah.
keith: I got a hunt. I'll put 100 on it right now.
Colton O'Farrell: Yeah. Yeah.
Marc: I'm not the main user. I've seen some things we figured out workarounds or Najeer, you and your team have actually, you know, coded workarounds. It sounds like you're going to do for us now. Yep. Absolutely. I think you got some good stuff down the line that's going to maybe help us and others. The last time.
Colton O'Farrell: Yeah.
Marc: Keith, you got anything else or does it sound like we're pretty good for now?
keith: I think we hit the two real main issues.
Marc: Okay.
keith: Yeah, I'm just looking at my list. I don't have anything else that we haven't already talked about.
Marc: Yay. Cool.
Colton O'Farrell: Anything else pops up, definitely let us know. But Najeer and his team will make those changes for you that should be either today or tomorrow for some of the, the smaller changes and equipping that delete button. If anything else comes up, though, feel free to let us know and we're happy to handle that as it comes up. But really appreciate the partnership here and the product feedback. We love working with you guys and we hope to yeah. Be the. The AR and AP solution used for many years in the future. So really appreciate the partnership here. Thanks, guys.
Marc: I feel it, and I appreciate it as well. Take care.
Colton O'Farrell: Yeah.
Najeer Ahmed: Well, it's good to meet you guys.
keith: Good to see you, guys.
Colton O'Farrell: Bye. Bye-bye.

---

**Recording:** https://storage.googleapis.com/saved-meeting-recording.prod.circleback.ai/meeting_3420889.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=circleback-ai%40appspot.gserviceaccount.com%2F20251022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251022T012429Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=a1f78a4a21500d69ea970fdab23bfd74db14ff21ae0096216a13190b51917fb84d7e9c9e9eec1d839dc9aca56f4304cf3a1705641125abb0e5dc5b048241bc329d1178259a0ef02ba4315783c318da23595f5e2bf743e9ffd2ced330feab895081ab9453a7c4b7d5aeab9bd17cc5d4e50351221e5770a435ca677083919d100e4c020a806e6f92977ca1ef93bbfad676b35e32768322cdc73c5d379a46911c45cc3ae97847e20e71f9ea9a6ad7f5950ab75e2485750bffbc90698fb4ee1249d1611265c4952c5daa29a84dee053c2c1f5ec2342b7ca05f963f3e4e523a5f4892942bf62c8341754092d6df254cd2134fca1616bc73b55c724e52f248edbdbe45
