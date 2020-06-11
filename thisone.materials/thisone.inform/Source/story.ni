"newmedia" by Neha Lingareddy

Include Vorple Notifications by Juhana Leinonen.

The player is in Crew's mess."Going by the long communal tables, I’d say we’re in some sort of cafeteria, it looks like. Very dimly lit. Ah, here’s a sign, I think I can make it out… it says this is the ‘Crew’s Mess’. And the floor… is rocking? I think we might be on some sort of ship!"

Flashlight is in Crew's mess. 

Flashlight is a device.

Perikey is in Crew's mess. 

Perikey is an object.

Ladder is an object in Crew's mess.

After taking ladder, say "go up to the engine compartment".

Engine compartment is above Crew's mess. "CAN YOU HEAR ME??
SORRY BUT WE’LL HAVE TO SHOUT OVER THE NOISE IN HERE.
THIS WHOLE ROOM IS ONE MASSIVE ENGINE! NEVER SEEN SO MANY GEARS AND PIPES IN MY LIFE… I SEE ONE THICK ROD STICKING STRAIGHT OUT THROUGH THE FAR WALL, LABELED ‘PROPELLOR AXEL."

Switch is a device in the Engine compartment.

After taking the switch, say "turn the switch on".

After switching on switch, say "Woohoo! the engine switch is on".

Galley is a room.
Galley is east of Crew's mess.

Before going to the Galley:
	 if the flashlight is switched on:
	 	say "'Hmmm, looks like we have some essentials in here … a bottle of brandy and a radiation suit'"; 
		continue the action;
	otherwise:
		say "It’s pretty dark in here … looks like we’re gonna need to switch on the  flashlight and reenter";
		stop the action;
	
Radiation suit is an object in Galley.
Radiation suit can be taken.

Brandy is in Galley. 
After taking Brandy, say "Should we give it a taste?".
Brandy can be tasted. 
After tasting Brandy, end the story saying "You have no tolerance … and you drank the whole bottle … rip".

Nuclear core is above Galley.

Before going to the nuclear core:
	if radiation suit is carried:
		 say "Whew ok, good that we have these suits, wouldn’t want to be exposed to whatever radiation is going on in there. Here’s how to use the headset in these things, because there’s no way we’ll hear each other otherwise… Ok, let’s get inside now.";
		continue the action;
	otherwise:
		 say "Give me a sec, this door is heavy as hell. What is this thing made out of, lead? Ok here we are… oh. I… I don’t feel very well, all of a sudden.YOU HAVE ABSORBED A LETHAL DOSE OF RADIATION AND DIED."; 
		end the story saying "YOU HAVE ABSORBED A LETHAL DOSE OF RADIATION AND DIED.";
		
Charger is a device in nuclear core.

After taking the charger, say "switch on the charger".

Before switching on Charger:
	if nuclear fuel rods is carried:
		say "drop the nuclear fuel rods in this room";
		continue the action;
	otherwise:
		say "you need the nuclear fuel rods";
		stop the action;

Crew's bunks is east of Galley."This is definitely where the crew lives, given the bunks and all. Anyone fancy a cat nap? Brrr it’s really freezing down here… and what’s with the shimmering spirits in the air?"

Crew's bunks is a room.

Ghost is a person in Crew's bunks.

After asking Ghost about "who are you", say "Oh, you're not scared of me? Hmmm, just go up to find the captain then"

Nuclear fuel rods is an object in Crew's bunks.

After taking Nuclear fuel rods, say "Take us to the nuclear core room"

Control room is above Crew's bunks.

Control room is a room. 
"Looks like we made it to the control room of whatever this place is… I can see a dashboard, some blinking lights, comms, and what looks like… a periscope? Wait what the… there’s someone else in here with us! He’s all tied up and unconscious, dressed in military garb… he looks like the captain of this vessel. Should we try to wake him up? "

Captain is a person in Control room.

Understand "talk to [someone]" as a mistake ("To start a conversation, try to ASK [the noun] ABOUT something or TELL [the noun] ABOUT something.").

After asking Captain about "home", say "Thank goodness you’re here on my submarine! My crew turned on me and left me for dead. I - ohhh my head hurts. Ahh! Jesus. I don’t think I’m fit to do much piloting right now - you’ll need to take over. From the console, it seems as though the engine’s in trouble - we’re out of nuclear fuel. You’ll need to find the fuel rods, put them in the nuclear core, and switch the engine on high to supercharge the sub in order for us to get home". 

After asking the Captain about something, say "Annnd he passed out again. Poor guy.".

Periscope is a device in the Control room.

After taking periscope, say "try switching on the periscope".

Steering control is a device in the Control room.

After taking the steering control, say "try switching on the steering control".

Before switching on periscope:
	  if Perikey is taken, say "Periscope unlocked. The way home is to use the steering control. Wake up the captain to find out how.";
	  otherwise say "You all need the keys to the Periscope. Got get them!";
	
Before switching on Steering control:
		if charger is switched on and switch is switched on, end the story saying "YESSS! All of you can get home now";
		otherwise say "You can't switch it on right now. Ask the captain about home"; stop the action;


Release along with the "Vorple" interpreter and a website.
