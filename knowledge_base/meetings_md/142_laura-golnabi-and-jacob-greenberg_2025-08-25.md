---
title: Laura Golnabi and Jacob Greenberg
date: '2025-08-25'
time: '14:00:26'
duration_sec: 1004.89
duration_min: 16.7
participants:
- Jacob Greenberg <jacob@getnickel.com>
- null <laura.golnabi@uvims.com>
- Saeed golnabi <golnabi@optonline.net>
- Mohammadreza <null>
source: Circleback
meeting_number: 142
# === STRATEGIC CLASSIFICATION (Transcript Classifier Agent v1.0) ===
call_type: discovery
deal_stage: discovery
customer_segment: unknown
has_pain_points: true
has_objections: true
has_competitive_intel: false
has_use_case: true
has_pricing_discussion: true
has_integration_needs: true
primary_industry: professional_services
transaction_volume: unknown
ar_vs_ap: both
processed: false
dimensional_extracted: false
extraction_priority: high
---

Saeed golnabi: Good.
Mohammadreza: Morning, guys. Good morning.
Saeed golnabi: How are you?
Jacob Greenberg: Good.
Saeed golnabi: So.
Jacob Greenberg: So who do we have here today? I see.
Saeed golnabi: Actually, this is, this is Saeed Golnabi, you have an appointment with Laura, but she's my daughter, so I'm calling on behalf for, for the emerging Monterey area school. So if you need my password, username, whatever, I'm, I'm logged, we are logged in right now. So I have a couple of questions. Probably this, this call is going to be quick. One, one is, I'm basically, I'm basically developing this. this solution for them so that their software, their user, their parents, they can make the payments through our programs. So, so far, our first question is, let's say, do you guys have any callback at the end so that if it is successful, does it route it to our site or something like that or not? Is it something you guys can do after they basically go through the putting the information and submit and make the payment.
Jacob Greenberg: Okay, I am not sure I understand the question. So just let's back up for one second. You guys work with a Montessori school, correct?
Saeed golnabi: Correct, yes.
Jacob Greenberg: And then the you're using nickel for accounts receivable or for accounts payable?
Saeed golnabi: For accounts payable. So the parents log in and they want to make the monthly, monthly tuition they have to pay every month. So the parents log in, they want to make a payment either through ACH or credit card, both.
Jacob Greenberg: Okay. Okay.
Saeed golnabi: Great. Yep.
Jacob Greenberg: So did you guys already created an account on Nickel?
Saeed golnabi: Oh, yeah, yeah, we have it.
Mohammadreza: Yes.
Jacob Greenberg: Okay.
Saeed golnabi: You already have the account and we have already already made some, if you look at it, you will see a lot of like $1 payments and $10 payment. That's what we are testing with our software so that we can basically, before we go live, you are basically testing it.
Mohammadreza: Okay. Our issue is a technical issue. Okay. We have currently an account on Nickel payment and we want to use this account for all system to learning a payment system. Okay. Message, message, message, message.
Saeed golnabi: So you can share it here. So our question is how?
Mohammadreza: We need to integrate Nickel get, Nickel payment system with all system that parents can pay with this gateway and return to our system again.
Saeed golnabi: For.
Mohammadreza: Now, my issue is the retaining the system after the payment.
Saeed golnabi: How can we come back to our payment after the parents made the payment? Somehow route it back to our system, to our page.
Jacob Greenberg: After they make a payment, you want the page that they're on, on the payment page, to send back to the Montessori school website.
Saeed golnabi: Correct, yes.
Mohammadreza: Yes.
Jacob Greenberg: You want the information to send back to the website or you want them just you wanted to reload the website?
Saeed golnabi: I guess the information and the message that it was done successfully, whatever the message is, if they get an error or whatever it is, something that we can we know they made the payment.
Mohammadreza: Or... Let me share my experience with you. to show you what we need.
Saeed golnabi: By the way, one thing, we made the payment the other day, 423. Can you cancel that payment? We couldn't cancel it because it said it is not, it is in process. So if you can just cancel that for us.
Jacob Greenberg: I could ask my development team, but you should be able to cancel it on your own.
Saeed golnabi: We tried it, but it says since it's not You can either return, like get refund, we cannot because it's not like done yet and it's not in, it's like in process. So, when it's in process we try to cancel it, say you cannot do that.
Jacob Greenberg: And this is a payment that you sent or received?
Saeed golnabi: We sent like, and we receive a.
Mohammadreza: Payment, sounds like, received yeah.
Jacob Greenberg: All right, I will find out.
Saeed golnabi: We can show you, he is going to show you that we did some testing like $1, $10. There was one, one for 123. I just would like to cancel that.
Jacob Greenberg: Okay.
Saeed golnabi: So.
Jacob Greenberg: You were sharing your screen.
Mohammadreza: You can show me again.
Jacob Greenberg: I mean, yeah.
Saeed golnabi: So go ahead.
Mohammadreza: Yeah, okay, sure.
Saeed golnabi: You will stop sharing, so share your screen again.
Mohammadreza: Can you see that?
Jacob Greenberg: Yes.
Mohammadreza: Okay, but no, we pass the amount and the order reference with the parameters. Okay, this URL will need the All clients as parents, we redirect this gateway by our system. We want, when we need to pay, when we pay successfully.
Saeed golnabi: Call back.
Mohammadreza: They said, can you give me your loading number?
Saeed golnabi: Yes. 0-2-1-2-7-2-6-5-5.
Mohammadreza: 0-2-1-2-7-2-7-2-6-.
Saeed golnabi: No no no no 0-2-1-2-7-2-6-5-5.
Mohammadreza: And your account number?
Saeed golnabi: 383.
Mohammadreza: J83. 424-424-766.
Saeed golnabi: First of all, on this page, how can we pass some information like address to here also? Address? Yeah, we already have the to, on the page where you enter the bank information, the bank address information. Because we have it in our system, so when they click on make a payment, we would like to populate this the same as we do the first, the first 2, the amount and the description we can pass it with parameter. I guess my question is can we pass parameter also to the address or to fill out the address also?
Mohammadreza: Just information. Just name, city name.
Jacob Greenberg: Yes, when you send an individual invoice through the accounts receivable tool.
Saeed golnabi: They will.
Jacob Greenberg: Have their information auto populated. But this payment link is a generic payment portal. It's not for a specific invoice. So it won't know who's using it. Does that make sense? Like it won't recognize you, me, we.
Mohammadreza: Need to know that. we have to use an order way to loading to the payment page.
Saeed golnabi: So what is the best, what is your, what is the alternative? What is the best practice to do it from your system?
Jacob Greenberg: I'll show you typically what people will do, okay? Give me one second. I'm going to get my screen pulled up.
Mohammadreza: Okay?
Saeed golnabi: Yeah.
Jacob Greenberg: Can you see my screen?
Mohammadreza: Yes.
Jacob Greenberg: So this would be recurring invoices and this would be for all the families.
Saeed golnabi: So.
Jacob Greenberg: You create a recurring invoice, say Saeed test. He set it for recurring. every month and on the first or the 25th of every month.
Mohammadreza: Okay.
Jacob Greenberg: It's a bill. How often do they pay the bill?
Saeed golnabi: Monthly.
Mohammadreza: Can we do that? Real system, real API. Can we do that?
Jacob Greenberg: And then once you click create, what you do is you do charge payment method on file or secure payment. so if you have the information already, you could just charge it automatically every month. They don't have to go in and pay, but you could come in and you can send the link and it will look like this. It will say Montessori School. This will have your logo.
Saeed golnabi: So, by the way, do you mind if. Can you record this so that. I don't know. I guess if you can or not, it doesn't matter, really. Yeah. Are you okay?
Mohammadreza: Yes, it's okay. We need to integrate your system with all system. It's mean we need to create these invoices with our system. Can we do API API?
Jacob Greenberg: So we don't do APIs, but we can build out a webhook.
Saeed golnabi: Webhook, okay. Yeah.
Mohammadreza: Okay. And how we can redirect the customer after the payment to our system?
Jacob Greenberg: Say that one more time.
Saeed golnabi: So how can we redirect the, after they make the payment, how can we redirect it back to our site? With the message saying that it was successful or whatever the message is.
Jacob Greenberg: I'll find out, I'll find out if that's possible. I don't know if we can do that right now.
Saeed golnabi: Okay. Yeah.
Jacob Greenberg: You just want one.
Mohammadreza: Can we talk with the technical person to fix this issue?
Jacob Greenberg: You can email support@getnickel.com and they'll respond to you, but I'll message them as well right now.
Saeed golnabi: Oh, good. You. I think if you know that we talk to, it's whether you are our contact, like point of contact, it's fine.
Mohammadreza: It's really more, more official. Okay.
Jacob Greenberg: Yeah, I'll loop in since I don't, you know, this seems like a technical thing and I don't have any ability to do that for you guys. I'm going to loop in the technical team, okay?
Saeed golnabi: Actually, let me tell you another thing. I have a, my company is like your secure portal. In fact, I have my own software company and I recommend that Nikhil company to this emerging Montessori school. She's my daughter anyway, so. But yesterday I received a message that because I wanted to start using it for my company. And then once it's, I'm happy with it, just do all this integration there basically because I have about 70 clients like Monteserrate School. So I was planning to basically give them like a solution if it is simple because I I mean the software that they use is my software company. So I was going to give them one and then all of a sudden I received an email yesterday that sorry we cannot we are going to close your account. I don't understand all I did was did a couple of testing so can you look into that for me also?
Jacob Greenberg: What was the account?
Saeed golnabi: It's your secure portal.com your secure portal.com.
Jacob Greenberg: Okay cool I will look into it.
Saeed golnabi: For you and I had I had a call with Christian today, but it was exactly at the same time I had to reschedule it. So if you can look into that, as I said, that's my own software company that I have a product that I have about 70 clients that they use my software. So I just wanted to also give them a solution for payment. So I'm sure this is something good for you guys, so.
Jacob Greenberg: Okay, great. I will message the team and I'll have them get back to you guys today.
Saeed golnabi: All right. So let me see. Mr. So tell me, do you get your. Did you get your answer or not? I. Think the. hello.
Mohammadreza: Okay.
Saeed golnabi: Yeah.
Mohammadreza: Okay. I understand. I. We need. We have to communicate with test to call team. We are supported by getnik.com to fix this issue for us. Okay. Thank you, Jacob.
Jacob Greenberg: All right. Thank you, guys.
Saeed golnabi: So. So we'll just wait for your email or what do we. What's the next?
Jacob Greenberg: Yeah, I'm gonna send an email to the. to the development team. So support.
Saeed golnabi: And send us on this email, the one that you, you sent us the link to. This is a good, good email to send it to me. So.
Jacob Greenberg: Okay, great. Pretty good.
Mohammadreza: Yep.
Jacob Greenberg: Thank you so much.
Saeed golnabi: Thank you.
Jacob Greenberg: Also, thank you.
Saeed golnabi: Also the other one. Also the, for your secure portal, please let me know what's going on so that they can basically, I can use it. I wanna. I wanna start using it to build my clients. So basically, so that my clients, they can go on and make their payment with credit card or with ACX. So.
Jacob Greenberg: Okay, sounds right.
Saeed golnabi: Thank you. Okay. One more question. The. The rate that you guys have, is this something that you can confirm with me? Because my daughter asked me to. To ask you specifically.
Jacob Greenberg: For what?
Saeed golnabi: For the, the rates. The credit card for the ACH.
Jacob Greenberg: Yeah, it's free ACH and 2.99 credit card. But you could put the credit card on your customers.
Saeed golnabi: Exactly. So, and for the ACH is free, right?
Jacob Greenberg: Correct.
Saeed golnabi: Okay. And is there a, she also asked me to ask you, is there a limit, minimum, hundred dollar, ten dollar or, or, or, or. I mean, of course nobody pays $10. She just wanted to know what's the minimum, the maximum that you can do through the ACH?
Jacob Greenberg: There's no minimum and the maximum on the free program of Nickel is $25,000 and the maximum on the paid version of Nickel is unlimited.
Saeed golnabi: And the paid version, how much, what is the difference between paid version and the free version?
Jacob Greenberg: The paid version is $35 a month.
Saeed golnabi: Okay.
Jacob Greenberg: And you can send transactions of any sizes. So above twenty five thousand dollars.
Saeed golnabi: Okay.
Jacob Greenberg: And it has a one day quicker settlement time for ACH.
Saeed golnabi: Uh huh. Probably she should. So this is 35 flat per month. That's it.
Mohammadreza: Yep.
Saeed golnabi: For the credit card is the same. It doesn't matter, right?
Jacob Greenberg: Yep.
Saeed golnabi: Okay. If you can also shoot me what you just told me, because this. What you tell me, it's not very clear everywhere. It says that with. But if you can also shoot me an email, tell me about the rate that you just told me so that I can forward it to her.
Jacob Greenberg: Okay, sounds good.
Saeed golnabi: Very good. Thank you.
Mohammadreza: All right. Thank you. Thank you.

---

**Recording:** https://storage.googleapis.com/saved-meeting-recording.prod.circleback.ai/meeting_3488072.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=circleback-ai%40appspot.gserviceaccount.com%2F20251022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251022T195535Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=7389c5778ca0c5cb79f18f9a15896156e711cd51d847a4d21d2f6be07271f392a42f80f9f5af3a1778f99e14f613f65d584a2d72fb0cd79fb11e5f41b2696e44b3d1ea05c6c4f957a13892bbbee7e8c88409eac32eda60daafe98838a6545f52471d66cbce2242225605c0f1835c212c08a2ab56ff1cf5ee3da05f57b0c11049919442390f60fcf475b328325f921f11761e716680e1c3525995f1b75bc898bff0c2fcd4fec1f8f38932df3f990b025fbfdf702433989c43cf3dde9a2c0b46c141ef3c7b0b43eaa0f99d7c887e0eab3c87c716c3cf3030b72a7b7ac6d345d01aca4b5bb79c259bcc5ee4e756c5710875da524c690789b540bbd4486b99576f72
