---
title: Jagadish Sudarsanam and Christian Sheerer
date: '2025-08-11'
time: '14:30:24'
duration_sec: 1345.02
duration_min: 22.4
participants:
- Christian Sheerer <christian@getnickel.com>
- Jagadish Sudarsanam <sjagis@gmail.com>
- Participant 1 <null>
- Participant 2 <null>
- Participant 3 <null>
source: Circleback
meeting_number: 60
---

Participant 1: To turn on the video?
Christian Sheerer: Okay, I'll put mine off then too. Okay. Yeah, I guess let me know how you found us and what you think NIKO would be useful for.
Participant 1: Yes, so here's the thing, I'm building a website to, so okay, here's the thing, I deal with real estate transactions, like buying and selling the seller finance lands, So I've been working with both sides, people who have a land, they do seller financing, and then the buyers who make a monthly payment, let's say $500 a month or something like that. So we go through setting up the payments and collecting the money every month from the buyers. So I'm planning to put together a website where we get the information from the buyer, like their name, address, and their banking information and whatever it is needed to take the money from their account and pay the money to the seller on periodical basis. So it could be like a weekly or a monthly or whatever is the agreed terms between the buyer and seller. So I'm looking for the companies that provide the ACH transfer. So I've been looking at a couple of things like Stripe and GoCard, GoNoCard or whatever, right? Okay, so those kind of sites and I came across a Nickel as part of Google search and I found you have better the fees and pricing. So I want to learn about your process and what you need from me to allow me to set up this ACH transfers and if there is any banking regulation that I need to follow because when I'm going to take money from somebody's account, you know what it takes or is it everything you manage and I just send a request for money. So how does this work with the nickel?
Participant 2: Yeah.
Christian Sheerer: How much are you doing in volume today?
Participant 1: On a monthly basis? So, yeah, I'm just building out at this time. I would say probably about 500,000 transactions a month.
Christian Sheerer: 500,000 transactions a month. And what is the transaction for typically? It's land.
Participant 1: Yeah, typically for land purchases, mostly for the real estate transactions. Let's say like you want to buy a property, which usually are low value. Let's say a property is worth about $5,000. So you want to buy it on cash, but you don't have the $5,000. What you do is you basically have a contract with the seller saying, I will pay you $500 every month for one year. They have some agreed upon interest terms and things like that. But the buyer will agree like, you know, I will pay $500 a month at the end of one year. Once I'm done with the payment, you transfer the deed to me. So this is the model. So what we need is- Where are.
Christian Sheerer: These transactions usually taking place? Like geographically, like what land is $5,000?
Participant 1: Only you will see.
Christian Sheerer: They're probably buying like a tiny amount of land, it sounds like.
Participant 1: Yeah, it could be like, you know, if you go to like a place like a Nevada, for $5,000, you can buy like 10 acres of land. You may not buy like, you know, 10 square foot in Manhattan. So it depends on where you are buying, you know. So this is how the model works. So the buyer looks for some kind of investment. So if they find a property, like, you know, whatever is the price, like it could be 5,000, it could be 50,000, it's between the buyer and seller. Once they agreed on the contract terms, you know, they go and set up the payment stuff. So, and then every month or whatever is the period. So we submit a request to pull the money from the buyer's account and transfer the money to the seller's account.
Christian Sheerer: Yeah, and so is your hope to have Nickel be sort of API'd into your platform where they can do it through your platform? Okay, so we won't do that.
Participant 1: Yeah, here's what we do, I want from your side. So the buyer has like, you know, like obviously they should have a bank account in USA. They should be like a legal resident or a citizen of USA. We check all those things, make sure like, you know, there is not somebody doing like money laundering and all those things. So we check those things and we set up the account. So I want to know who will keep the banking information. Is it I need to keep it or Nickel will keep it?
Christian Sheerer: No, we will, and that's why we don't set up APIs for our product just yet, right? Because we are sort of on the liability side of the payment. And so we don't actually work with software vendors who are baking Nickel into their platform. We would rather have people just use the Nickel platform itself because we have to be able to make sure we know on both sides where the, because of our compliance infrastructure, we have to know who the buyer and seller is on both side, both sides and, and, and they have to be operating through the nickel platform. So we wouldn't set it up in the way that sort of you're describing, wherein you would be like an independent service provider and we would be API'd into your platform. That would, that would be something that we would not do.
Participant 1: I see.
Participant 2: Okay.
Participant 1: So, you know, there are platforms that, you know, they do the payment processing, like, you know, you keep the buyer banking information and everything, but we need to have the transaction information. For example, like, let's say there is a one-year turn, you know, the agreement between the buyer and seller. We want to know the buyer has initiated a payment every month and that information is what we keep in our website so that we track like every month the payment is made and at the end of the month we submit the contract closure so that way the seller can make the deed transfer. You know what I'm saying? So if that is the case, like you want the buyer to create an account on Nickel platform and initiate the ACH transfer like a bill pay?
Participant 2: Yeah.
Participant 1: Okay, so how do I get that transaction information?
Christian Sheerer: Yeah, we wouldn't provide like all the full, this is why I think it's just probably not a good fit for the model because we want at least one member of the transaction side, right? Whether it's buyer or seller to have a nickel account.
Participant 1: Okay, let's pretend that I ask the buyer to set up the nickel account because that's where the money is coming from.
Christian Sheerer: Yeah, you could also set up an account for them as like a parent account and then have them authorize the transaction when the transaction is ready to go through.
Participant 2: Oh, okay.
Participant 1: Yeah, that's. That sounds good, too. Like, you know, so I can build a, like, what do you call, like, umbrella account, and then, like, I can create, like, if I have 100 buyers, I will set up their information and request them to, you know, authorize or provide their banking information, and nickel would approve it or whatever you do, the background check. So once Nickel approves it, so they can set up like a periodical transaction with Nickel and the money comes. So the thing is like we are not a bank to hold the money, you know.
Participant 2: Yeah.
Participant 1: So if I'm going to hold the money, I'm subject to a lot of other banking regulations. Okay. So what we are doing is we are only keeping track of the transactions that go from buyer to seller. That's all we do. We are only facilitating the process and also we are keeping track of the money that went from buyer to seller. And at the end of all the transactions are all complete, we kind of like, you know, close the deal between the buyer and seller.
Participant 3: Yeah.
Participant 1: So when so given that situation, so you want me to set up like umbrella account for the company, submit a request to add this buyer to your, you know, like the nickel. So do they need to create a separate account for each of them or they come under?
Christian Sheerer: No, you can create a separate account for them on your own.
Participant 2: Okay.
Participant 1: So and then the banking information to do the ACH. So do I need to fill that information or the buyer will do it?
Christian Sheerer: No, you can fill it out if you're representing under your umbrella, the seller, and then the buyer will fill in their account routing. You can fill it out if you have their account and routing number.
Participant 2: Okay.
Christian Sheerer: Or you can send them a request, right? Like send them an invoice and then they can pay it with their own information filling it in.
Participant 1: Okay, so do you use like a Plaid or some other service provider that to connect the bank account?
Christian Sheerer: Yeah, something like that, yeah.
Participant 2: Okay.
Participant 1: So you are already like, you know, because I'm this is my first time with the Nickel, so you are already approved to take the banking details of a common man, right?
Christian Sheerer: Yeah, we move money all the time.
Participant 2: Okay, okay, good.
Participant 1: So how does the pricing works? Like is it per transactions or a subscription? Like every month I pay like, I don't know, maybe $50-$100, I don't know. Or like is it based on the volume? So how does the pricing work?
Christian Sheerer: Yeah, the pricing is $35 a month.
Participant 1: For.
Christian Sheerer: The tier that you're going to need. ACH is free and there's a 2.9% fee on credit card transactions.
Participant 1: Okay, 2.9. So you have the Visa, MasterCard, American Express, and all that.
Christian Sheerer: Yeah, any credit card, yeah.
Participant 1: Okay, so 2.9% on credit card and ACH is free. Is there any limit on the number of ACH transactions? per day or per month or something like that?
Christian Sheerer: No, if it is a, I mean, you're right around the number that that makes sense. I would say if you said that you were going to do 30,000 a month, then we might have to have.
Participant 1: A conversation, but I'm talking about 500 to 1000 at this time.
Christian Sheerer: Yep, I know.
Participant 2: So, yeah, okay.
Participant 1: So, ACH is free and is there any cost to the Buyer like, like you may be charging only 25 35 a month to me.
Christian Sheerer: Do you know if there's somebody is not on the platform then then no it just the seller can pass on the credit card transaction fee if they.
Participant 2: Choose oh I see okay so only.
Participant 1: If they use credit card then there is a 2.9% is it 2.9% negotiable or Is it like a thousand?
Christian Sheerer: No, that's going to be our fee. It's the buyer and the seller can pass on that 2.9% or a fraction.
Participant 2: Of it.
Christian Sheerer: To the seller can pass that on to the buyer should they want. But no, we're going to be at 2.9%.
Participant 1: I see. Sometimes some providers, if you do like a thousand transactions or 10,000 transactions, sometimes they give Maybe like for 2.5, 2.3, something like that. You don't have it. It's always static 2.9.
Christian Sheerer: Yeah, I mean, we're willing if you become a customer that's like moving an exorbitant amount of money, we're willing to assess it. But yeah, we have a lot of customers that are quite large.
Participant 3: Right?
Participant 2: So, okay. Okay.
Participant 1: So 2.9 is like the base rate and then if the volume goes higher and higher, you have like some, I.
Christian Sheerer: Would say it would need to be significantly high.
Participant 2: Yeah.
Participant 1: Oh, I see.
Participant 2: Okay.
Participant 1: What else I need to do? Like, okay, so we are talking about the buyer side so far. So we collect the money from the buyer and then now you need to move it to the seller.
Participant 2: Right?
Participant 1: So there could be like 100 sellers and maybe 200 buyers or whatever, right? So now you take the money. So when you move the money to the seller, so that's also free.
Christian Sheerer: Move the money to the seller. Yeah, if it's an ACH, correct.
Participant 2: Right, right.
Participant 1: We right now, like I'm thinking 99% of our transactions are ACH, you know, so it's, it's not like a one-time thing, so. you know, these people set up for like sometimes like three years, five years payment, things like that, you know, they don't want to put through credit card and, you know, literally three percentage charge on it.
Participant 3: Right.
Participant 1: So when you take the money from the buyer, there is no ACH charge. When you put the, you know, money back to the seller, there is no ACH charge. So the 35 dollars is the Monthly service fee as a mediator, I'm paying to you. Correct.
Participant 2: Okay.
Participant 1: So is there any other cost involved in this?
Participant 2: No. Okay.
Participant 1: So that's good. What is the turnaround time? Like let's say you take a month.
Christian Sheerer: You can set it up today, I think. Oh, you mean in terms of a payment?
Participant 1: Yeah, yeah, I have not started the accounting side yet. So you take the money from me today, let's say I'm the buyer.
Christian Sheerer: So I understand it's about a two day turnaround time.
Participant 2: Okay.
Christian Sheerer: One to two days on ACH.
Participant 2: Okay, good.
Participant 1: So what is the thing that you okay, now we are talking about the setting of the account and what kind of information you need from me.
Participant 2: Okay.
Participant 1: So basically like as I said, we are only like a platform to connect the buyer and seller and keep track of the transactions so that the money is whatever the, if there are like 100 payments the buyer has to make. So we track all the 100 payments, make sure the seller is paid on time and if there is any defaults or something that happens, we kind of like mediate and fix things. So what are the things you need from me as a company?
Christian Sheerer: Yeah, you can just get set up. you would need bank account information from the people who to make a transaction.
Participant 2: Okay.
Christian Sheerer: That's pretty much it. And then you can get set up and try your first transaction today. It sounds like there aren't transactions that are ready to be made though, are there?
Participant 1: Yeah, no, this will take like, you know, I need to get all these platforms set up and ready. So that's going to take probably a month. So I have to get all these sellers you know, give the transaction information and load it. Same thing. I need to inform the buyers to set it up. So this is going to be, you know, like a month time, you know. So I want all these details so that do you is there because there is some money transfers going on and I'm not physically going to hold any money in the process. So is there anything that I need to be compliant?
Christian Sheerer: I don't understand the question.
Participant 2: Okay.
Participant 1: The question is, I'm sorry, is there.
Christian Sheerer: Anything you need to do to be compliant?
Participant 1: Well, yeah.
Participant 2: Right.
Participant 1: That's exactly my question is like, so I'm as a website provider, I'm just maintaining the information of the transaction. I'm not going to hold the bank information of the buyer. or the seller. I just, you know, maintain the transaction information. So whenever, like, you know, you pull the money out of a buyer, I have a transaction. When you post the transaction to the seller, I have a transaction. I maintain this information alone. I don't maintain the money. I don't maintain their banking information. So I don't know whether you did something like this setup before.
Christian Sheerer: Yeah, we have many accountants who are not the owners of the business who run umbrella accounts for their clients. And so this is a similar situation. And so you would just need to Make sure that you're safely handling their bank account information should they give you their bank account information. But you can also Give them authorization access to authorized payments.
Participant 2: Okay. Okay.
Participant 1: That sounds good.
Christian Sheerer: Yeah, we have I will tell you a lot of compliance checks on our end, right? We have to go through the same process, make sure there's no money laundering going on all the things that money movement processors have to do.
Participant 2: So.
Christian Sheerer: So we will also have an eye on it.
Participant 1: Yeah, definitely.
Christian Sheerer: Yes.
Participant 1: Yeah. So is there anything I need to do like a background check on a buyer or seller or it is something beyond scope?
Participant 2: To be on your scope. Okay. Good. Okay.
Participant 1: So you keep track of where the money is coming, where it is going and if you flag somebody is like moving from outside the country, It's up to you to maintain that kind of complaints, right? Okay, sounds good. Yeah, this is pretty much what I wanted. So is there any like a number or something, if I have a question or something I want to reach out to you?
Christian Sheerer: I'll send you an email, it's support@getnickel.com.
Participant 2: Oh, okay.
Participant 1: So it's like a one common place.
Participant 2: Okay.
Participant 1: So one more question. Is it possible right now? I want to allow people do money transfer only within the country, within USA. And if somebody is trying to move from outside the country, is it possible to either, like, hold the transactions or, like, you know, I don't know.
Christian Sheerer: I don't know.
Participant 2: Okay. Okay.
Participant 1: So the ach is open, right? So it's kind of like anywhere from the world, right?
Christian Sheerer: No, it's within the U.S. for now. We will be rolling out international payments shortly.
Participant 2: Oh, very good. Okay.
Participant 3: Yeah.
Participant 1: That's what the protection for my bias also I want, you know, so, you know, that serves both the purpose of AML requirements and, you know, we don't have to go through a headache of. somebody stealing the money. Okay, good. Yeah, thanks Christian for all the information. You know, like you plan to send me an email with in a contact details and any follow-ups. If I have a question or something I need, I will come back to you. And you know, once all the services are ready, I will set up the account as an umbrella account and get all my buyers and sellers set it up.
Christian Sheerer: Yeah, I would recommend setting up an account. Pretty easy to do, free to start. And then when you need the.
Participant 2: You.
Christian Sheerer: Can have a trial for that 35 a month period and then when you need to turn it on, it'll turn on automatically after the trial.
Participant 2: Oh, wow, okay.
Participant 1: That sounds good. Yeah, I will check those things and very soon I'll set up the account. And, you know, that should be good.
Christian Sheerer: Awesome.
Participant 2: Okay.
Participant 1: Thanks a lot, Christian.
Christian Sheerer: Yeah, no problem.
Participant 2: Thank you.
Participant 1: You're welcome.
Christian Sheerer: Bye.

---

**Recording:** https://storage.googleapis.com/saved-meeting-recording.prod.circleback.ai/meeting_3250032.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=circleback-ai%40appspot.gserviceaccount.com%2F20251022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251022T153136Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=01364ec7563c22137f12bf43e3542649dfd00ddc041962baf32206dc3cb42b820fa8f776840afd159e122433026ea86a8b598bf7195a093a9df07f9544a4bf731e7bc51768466852067c95a4e42068c95432eec9245ac36f6cae939b1ee7956b36d892e035073d60cfeb5060469c9f9a2b9e6fa476ab0ea3a80a7024adfd1e7298c13a6dd25a139966349d39c6a707635bad953b8d5ca0ee477dfc4dd65df9b3fe70e6a47b4144305535849e932cef0c217eb4cd4e33d4c36c9bb7cf51dd6bbe678166fb25ea4c81ca3dad92ce913ecf4f6bcc582d085cd840a6852b71e02ea929dcb7f9205385f5f0d8ab6f8d1c8b8c265c5998c535ea43c6a179500fae6aef
