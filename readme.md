<h1>Town of Salem, Night 1 Alert Veteran Simulator</h1>
<h2>What is this?</h2>
<p>
  This is a program which simulates night 1 of a ranked practice, town of salem game in which there is a veteran and he alerts. The simulation is repeated many times to see if it there is a favourable outcome on average. To my knowledge, the code is correct. Some assumptions are made but I consider them to be reasonable assumptions about how the game is <em>actually</em> played. I encourage anyone to look through the code and suggest improvements.
</p>
<h2>Well, is it a viable strategy?</h2>
<p>
  The answer seems to be yes, provided the code is correct and the assumptions are reasonable. 
</p>
<h2>Fun numbers</h2>
<p>
  Here are the results of <strong>1,000,000</strong> night ones with a veteran who alerts:
</p>
<pre>
  (0) Most bloodthirsty veteran: 6 kills (Mafioso, Doctor, Bodyguard, Doctor, Forger, Serial Killer)
  (1) Total good results: 288582
  (2) Total bad results: 231744
  (3) Total veteran kills: 520326
  (4) Good results per night: 0.288582
  (5) Bad results per night: 0.231744
  (6) Veteran kills per night: 0.520326
  (7) On his best night, the veteran killed: Mafioso, Forger, Serial Killer, Witch (+4)
  (8) On his worst night, the veteran killed: Investigator, Doctor, Bodyguard, Bodyguard (-4)
  (9) Kill distribution [0 veteran kills, 1 vet kill, 2, ...]:
         [605132, 289013, 88274, 15703, 1742, 128, 8, 0, 0, 0, 0, 0]
  (10) Good kill distribution:
         [759706, 194320, 43683, 2268, 23]
  (11) Bad kill distribution:
         [791167, 187247, 20296, 1255, 35, 0, 0, 0]
  (12) Veteran kill distribution:
         Jailor        0
         Godfather     9864
         Serial Killer 18851
         Arsonist      18900
         Witch         18946
         Framer        20866
         Consort       21086
         Janitor       21102
         Blackmailer   21164
         Forger        21208
         Disguiser     21242
         Consigliere   21456
         Transporter   31031
         Investigator  34057
         Sheriff       34216
         Lookout       34280
         Bodyguard     49002
         Doctor        49158
         Mafioso       73897
</pre>
<h2>Some comments on the above numbers</h2>
<p>
From <strong>(1)</strong> & <strong>(2)</strong>, we can see that as a night one veteran, you'll kill ~0.29 bad guys per game and ~0.23 good guys per game. Thus, it is indeed viable to alert on night one as the veteran. This does <em>not</em> include the fact that killing <em>anybody</em> makes you a confirmed veteran which is a good thing! Having a confirmed town member is great for the team.
</p>
<p>
To clarify point <strong>(9)</strong>, this means that in a million games, the night one veteran killed zero people 605,132 times, killed one person 289013 times, and so on. Amusingly, you'll only kill somebody around 40% of the time if you alert night 1.
</p>
<p>
Points <strong>(11)</strong> & <strong>(12)</strong> are similar to point <strong>(10)</strong>. The veteran killed no bad guys 759,706 times, one bad guy 194,320 times, and so on. He killed 4 bad guys 23 times out of a million! 4 is the maximum number of bad guys he can kill under our reasonable assumptions. He killed 4 good guys 35 times out of a million. The veteran would surely be lynched for his failure in such a game.
</p>
<p>
Point <strong>(12)</strong> is pretty fun and the trends can be explained fairly easily:
</p>
<p>
Of course, the jailor cannot be killed by the veteran.
</p>
<p>
The godfather is rarely killed because he sends the mafioso in his place unless the mafioso gets jailed or roleblocked.
</p>
<p>
The next "class" of players are the serial killer, witch, and arsonist. Each of these appear in <sup>1</sup>&frasl;<sub>3</sub> of games. They also select amongst <em>all</em> other players to act upon so they are unlikely to visit the veteran.
</p>
<p>
Now we have the framer, consort, janitor, blackmailer, forger, disguiser, and consigliere. Any one of these roles appears in the game <sup>2</sup>&frasl;<sub>7</sub> of the time and only visit the 11 other <em>non-mafia players</em>. This makes them more likely to visit the veteran than neutrals and town members.
</p>
<p>
The loneliest class is the transporter alone. The Transporter can show up as part of Town Support <sup>1</sup>&frasl;<sub>5</sub> or Town Random (roughly <sup>1</sup>&frasl;<sub>12</sub>). The escort would be in the same boat but we choose to exclude the escort from night 1 action as that is a reasonable line of play and it simplifies things.
</p>
<p>
Now we have the investigator, sheriff, and lookout. They show up as part of Town Investigative (<sup>1</sup>&frasl;<sub>4</sub> each) or Town Random (roughly <sup>1</sup>&frasl;<sub>12</sub>). Since they show up a bit more often than the transporter, they die to the veteran a bit more often!
</p>
<p>
The most likely town members to die to the veteran are the ones that show up the most! Of course, those are the doctor and bodyguard. They appear as Town Protective in half of games each and also sometimes as Town Support. These poor guys get shot by the veteran so often and they were just trying to help!
</p>
<p>
Finally, we have the poor mafioso who does the godfather's bidding, is in <em>every single game</em>, and visits <em>only non-mafia</em>. Of course, he dies to the veteran the most.
</p>

  
