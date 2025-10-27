---
title: Nickel Demo Request - Thanmay Kumar
date: '2025-09-30'
time: '20:30:15'
duration_sec: 709.51
duration_min: 11.8
participants:
- Christian Sheerer <christian@getnickel.com>
- Thanmay Kumar <thanmay@kyronmedical.com>
source: Circleback
meeting_number: 106
---

Thanmay Kumar: Christian, how's it going?
Christian Sheerer: What's up dude? How are you?
Thanmay Kumar: Doing well, doing well. How are you?
Christian Sheerer: Not bad, can't complain. Busy, but better than sitting around doing nothing.
Thanmay Kumar: So it's good to hear. See this One second. How's it going? It's just, just busy.
Christian Sheerer: Good, busy. I'll, I'll say it again, can't complain. But yeah, you fill me in, I guess. I mean typically what we like to do, hear a little bit more about what you guys do for payments between your customers and your vendors, see if we can't fit in on the AR AP side and then explain a little bit more about what Nickel does. Very brief walkthrough of the platform. Doesn't take super long to get through a lot of it. It's very simple. A lot of the stuff that is difficult to understand is happening on the back end, which is, you know, the super service that we're offering. And so yeah, you should pretty much able to cover all of it in, in the next 30 minutes. But you fill me in on like what you're looking for in terms of payments, like what you guys are currently using and, and how we fit in.
Thanmay Kumar: Yeah, sounds good, I think. I mean I'm, I'm actually an intern working with, with the strategy team right now. Chiron does billing support for a lot of these physicians and they're looking to transition into full stack billing. And so it would be accounts receivable we knew would be payments from patients that would be coming in and we would be collecting on behalf of the physicians practices. And so this was just an option that they were considering and they wanted me to check it out. I think they have set up for insurance payments, but I think it would only be for patients paying and it would be for medical bills.
Christian Sheerer: So the idea is if you use us as like the payments layer under your guys's own payment. So they're, they're, they're paying. Walk me through that.
Thanmay Kumar: Yeah, so they would be paying for services provided by a physician, but we would be handling all the billing for those physicians, which would include collection of payments from insurance companies and from patients. And, and the actual collection from patients would be done with you guys.
Christian Sheerer: Okay. How so? It's not something that we typically do. So we're right, we're with, within the regulatory strictures that we have set up and the compliance requirements that we have with our banking partners, with our connection to the Rails, with the Federal Reserve, all these things, we have to be in direct contact with the end merchant and the end user Customer. And so we get this a lot, all the time, where people come in and they're like, hey, we have a software that does billing and we want to use you as the back end, probably because you saw us free. Ach. It's my assumption. Right.
Thanmay Kumar: That is something we're looking.
Christian Sheerer: Right. Yeah. We want to do it for cheap and you want to take advantage of our rates. But the reason we're able to get those rates is because we're direct between the businesses. And there are other, like, regulatory reasons why we have to be direct between the businesses. So it's not something that we typically do. We would. Because it's not something that we typically do. Hear it out as a project that we would have to take on to build sort of like a custom type of integration, provided that it. It's worth kind of derailing where our engineers are spending their time.
Thanmay Kumar: So. Right. The volume. Right.
Christian Sheerer: Yeah. So I guess. Do you guys do have a sense of the volume that is. Is. Is set up already?
Thanmay Kumar: No, no, I'm not. I'm not exactly sure. Is there. Is there. I mean, do you. Would you have a limit on the total transaction or per transaction size? I think there were some questions.
Christian Sheerer: There's no limit. It's. It's really just going to be kind of like an operational. It's more about like project management bandwidth between you guys and us. Right. Because essentially what would need to happen is every position and every. Every payor and payee, regardless of where they are in this, in the relationship, would have to have some direct interaction with nickel. The payers and payees don't necessarily have to have. Anybody who's doing accounts receivable through us has to have a nickel account. An individual nickel instance. Right. So a physician would have. Each physician would have to have their own nickel account that is managed in some way where then they're sending out payment links. That's how we do it. We send out payment links. Right. And their customers, patients, or whoever's paying them is sending them the payment. The payer in that scenario doesn't really need to have an account. They just pay out against the payment.
Thanmay Kumar: They pay in the link. Yeah, I've seen.
Christian Sheerer: Yeah, exactly. But all the physicians need to have one. Right.
Thanmay Kumar: I think for our. Our insurance workflow, we also have to sign contracts individually. So we can set up each practice individually in their onboarding with nickel. Would that be something then that's feasible through your current system?
Christian Sheerer: Yeah, exactly. It would just be. We would need to. We would need to have each of the Each of the practices have their own account.
Thanmay Kumar: Okay.
Christian Sheerer: The thing then there, though, right? So like, so then that. Let's assume that's the case and. Yeah, so let's assume that's, that's, that's all well and good. They would have to use the nickel payment link, like directly. We couldn't like embed it underflow.
Thanmay Kumar: There's no embedded flows.
Christian Sheerer: Yeah, like, we couldn't embed it under. I'm like on your site right now. I don't, I don't know where I would go, but yeah, if that makes sense, you know.
Thanmay Kumar: Okay, but so that they would have to go to their own practice. You're saying like practice one, dot nickel dot com. Something. Something like that. That link.
Christian Sheerer: Yeah, you have it. Yeah, you have it exactly correct. Yeah. So like, I'll show you.
Thanmay Kumar: Okay. Which also seems not unreasonable. Certainly problem. Yeah, yeah.
Christian Sheerer: And so, so this is. Yeah, this is the GRAS distribution, for example, but this is practice one in your case.
Thanmay Kumar: Okay. And each practice has its own link. If we do it the way it's.
Christian Sheerer: Each invoice even has its own individual payment link.
Thanmay Kumar: Okay.
Christian Sheerer: So it's one to one.
Thanmay Kumar: Could we, I mean, we can generate these links through some API call and, and use them. No, they're generated on the actual website each time.
Christian Sheerer: Yeah. There we. We. That's the regulatory constraint. We cannot do it by it. We, we. I mean, again, we could, depending on the size, technically. Could we? Yeah, we, we need. We, we would need to. And then it wouldn't be free is the other thing. Like, we, we would have to make, make this doable for us because then we have to build out API documentation that you guys can hook up into and, and do all of these things. And like, that's probably without knowing your volume.
Thanmay Kumar: Yeah. I think it's six figures a year.
Christian Sheerer: Yeah.
Thanmay Kumar: Okay. Okay, wait, six figures, I think could be reasonable, but.
Christian Sheerer: Well, what is it? What? Six figures that you would pay to us.
Thanmay Kumar: Right, Right.
Christian Sheerer: Yeah. What. What?
Thanmay Kumar: Just transaction fees. I'm not exactly sure. I'd have to get back to you.
Christian Sheerer: Yeah, yeah.
Thanmay Kumar: But yeah, I'd love to hear more about the fees. I mean, that. That would be fees, you're saying just if we do that. I see. Yeah.
Christian Sheerer: Yeah. That would sort of be the kind of like implementation costs and like up cost. Yeah, got it.
Thanmay Kumar: Okay. Okay. Yeah. I think a lot of the questions I had were, don't really apply then. So the main, main constraint is that you guys can't really hold the money for us in that way. It has to Be direct business to customer, you're saying?
Christian Sheerer: Yeah. The terms that your team might be familiar with are we, we can't like offer our services under independent service vendors.
Thanmay Kumar: Like independent service vendors.
Christian Sheerer: And so, yeah, basically what that means is like, we're, we're building like, not a workaround, but we're building the prevention of the workaround, I guess. Right. Like in. To make it compatible with the structure of how we interact with our customers and their end customers so that they have, we have that they have that one to one relationship between. And where, where Nickel sits in between that. And what I'm sort of stress testing with you guys is basically, you know, they would have to be operating within Nickel or you guys are operating it on the back end, you know, with us yourselves. Right. Because let's say you're selling this billing tool to them and then they have to leave Kyron, the Kiren site, and then go to Nickel to send out a link. Right. It's like, why, why are they, you know, why they should just sign up for Nickel. Right. Essentially. Right. And so like, that's where I say that there is some level of, like, operational situation where we, we have to make sure that it's, you know, palatable for the way that you guys are doing it and palatable for the way that we're doing it.
Thanmay Kumar: Gotcha. Gotcha. Okay, well, I think that sounds great. I. I think maybe this is something we might consider in the future. Yeah, it seems like it doesn't. Doesn't fall right now, but thanks for meeting Christian.
Christian Sheerer: Yeah, no problem. I mean, appreciate it. Just so I get a scope of it, what is, what do you guys do in terms of volume already?
Thanmay Kumar: Again, that's something I'd have to go up and ask. I. I'm. I'm not too sure. That's why. Yeah.
Christian Sheerer: Okay, cool. Yeah, no worries. I mean, we'll have your contact in, in the CRM.
Thanmay Kumar: I'll definitely reach out, I think. I mean, I'll head this up. I think right now probably other payment options are cheaper for us. And then later down the road, this seems like something that would work if our volumes are high enough. If this is something that they actually go down.
Christian Sheerer: Yeah. Yeah, cool. No worries. Yeah, I mean, I'm always glad to learn a little bit more too.
Thanmay Kumar: Yeah. And if I hear more info, if this is something they're more interested in, I'll reach back out and we can meet again for sure. Vice versa. Sorry.
Christian Sheerer: Vice versa.
Thanmay Kumar: Okay, sounds good. I'll see you around.
Christian Sheerer: All right, boss. You have a good one.

---

**Recording:** https://storage.googleapis.com/saved-meeting-recording.prod.circleback.ai/meeting_4114712.mp4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=circleback-ai%40appspot.gserviceaccount.com%2F20251022%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251022T153218Z&X-Goog-Expires=86400&X-Goog-SignedHeaders=host&X-Goog-Signature=be70df3e004eae8ebc9db7694c3b62f30cbf3ca9c6fc53b3040cb95ae689353b42888371e5fc8e8f2a9dcd95e0cde728426f351ce41842f8b945c0ef009d448dde7e921d5599bea8c94796f3fe3b953a0eec9f1dbc3829d3f46d2d8ac52ee1f7422823abf482e00af97d1227dcc5d9d5aed8356c11ba5d0e43577a09c72e1b90a0778838532c95aa2db9f3daa5bbb21338240fbabfc62db185dadc9c8786be96a2cfe65cb26e64ed97079e81cd2323bf80b70017571930ebd6f5f929c46c6563d677364d50d2785e8d42e559948e065fb1aedfcf1ab2fe8ad7d1cd4c69f4bbe5ad1cbbcfc219f47125090b77ae82bb648b6c97559fdcc10239e8a67806909c07
