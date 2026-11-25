"""Turma B: aula extra (coringa) Family Gossip. Conteúdo original; os posts do Reddit são abertos ao vivo, fora do site."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import page, boxes, wrong_right

R = os.path.join(os.path.dirname(__file__), "..", "turma-b")
ST = ""
def B(x): return f'<p class="big">{x}</p>'
def P(x): return f'<p>{x}</p>'
def model(read, frame):
    return ('<div class="cards"><div class="box"><p class="k">📖 Read</p>' + "".join(f'<p class="big">{r}</p>' for r in read) +
            f'</div><div class="box good"><p class="k">✍️ Your turn</p><p class="big">{frame}</p></div></div>')
def table(rows):
    return ('<table><tr><th>She said: "..."</th><th>She said that...</th></tr>' +
            "".join(f"<tr><td>{a}</td><td><b>{b}</b></td></tr>" for a, b in rows) + "</table>")

GOSSIP = [(a, b, a) for a, b in [("Guess what!", "start the gossip"), ("You won't believe this...", "start the gossip"),
          ("Apparently, ...", "I heard it, but I'm not sure"), ("Don't tell anyone!", "it's a secret"),
          ("My lips are sealed. 🤐", "I won't tell"), ("No way!", "surprise!"), ("Seriously?", "surprise!"),
          ("Spill the tea! ☕", "tell me the gossip!")]]
FAMILY = [(a, b, a) for a, b in [("mother-in-law", "your husband's / wife's mom"), ("sister-in-law", "your brother's wife"),
          ("stepmother", "your dad's new wife"), ("half-brother", "same dad, different mom"), ("niece / nephew", "your sister's kids"),
          ("the black sheep", "the 'different' one in the family"), ("take after", "be similar to"), ("get along with", "have a good relationship")]]

d = "extra-family-gossip"
page("Family Gossip (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "Extra class · Reported speech", "h": "Family Gossip ☕👀", "h1": True,
     "html": B("Did you hear what happened?")},
    {"k": "Warm-up · 5 min", "h": "Who do you take after?", "html": P("Remember our chat about hair and eye color? Let's continue!") +
        boxes(["<h3>Who do you look like: your mom or your dad?</h3>", "<h3>Who is the funniest person in your family?</h3>",
               "<h3>Who is the family gossip? 👀</h3>", "<h3>Who do you get along with best?</h3>"]) +
        model(["I have my mom's eyes, but I take after my dad: we're both stubborn!"], "I have my ______'s ______. I take after ______.")},
    {"cls": "dark", "k": "Family words", "h": "The family tree 🌳", "cards": FAMILY},
    {"k": "Gossip expressions", "h": "How to gossip in English ☕", "cards": GOSSIP, "html":
        model(["Guess what! Apparently, my cousin is moving to Canada!", "No way! Seriously?"], "Guess what! Apparently, ______.")},
    {"cls": "dark", "k": "Grammar · Reported speech", "h": "Tell the gossip: one step back in time ⏪", "html":
        table([("I <b>am</b> pregnant.", "she <b>was</b> pregnant."), ("I <b>live</b> with my boyfriend.", "she <b>lived</b> with her boyfriend."),
               ("I <b>can't</b> come.", "she <b>couldn't</b> come."), ("I <b>will</b> tell Mom.", "she <b>would</b> tell Mom."),
               ("I'<b>m going to</b> quit.", "she <b>was going to</b> quit.")]) +
        P("💡 The pronouns change too: I ➜ she / he · my ➜ her / his · that is optional")},
    {"k": "Read and build", "h": "Your turn to report", "html":
        model(["My aunt: \"I'm getting married again!\" ➜ My aunt said that she was getting married again.",
               "My brother: \"I can't cook.\" ➜ My brother said he couldn't cook."],
              "Someone in my family said that ______.")},
    {"cls": "dark", "k": "said or told?", "h": "said vs told", "pre":
        wrong_right(["She <b>said me</b> that...", "She <b>told that</b>..."], ["She <b>told me</b> that...", "She <b>said that</b>..."]),
     "html": B("<b>tell</b> + person: told <b>me</b>, told <b>my mom</b> · <b>say</b> + no person: said that...") +
        model(["My sister <b>told me</b> a secret. She <b>said</b> it was serious."], "My ______ told me that ______.")},
    {"k": "Exercise 1", "name": "Report it", "h": "Report the gossip",
     "qs": [{"t": "Aunt Rita: \"I am in love.\" ➜ She said she ___ in love.", "o": ["was", "is", "were"]},
            {"t": "Leo: \"I can't come to lunch.\" ➜ He said he ___ come to lunch.", "o": ["couldn't", "can't", "doesn't"]},
            {"t": "Mom: \"I will call Grandma.\" ➜ She said she ___ call Grandma.", "o": ["would", "will", "was"]},
            {"t": "Bia: \"I live in Recife now.\" ➜ She said she ___ in Recife.", "o": ["lived", "lives", "living"]},
            {"t": "Dad: \"I'm going to sell the car.\" ➜ He said he ___ to sell the car.", "o": ["was going", "is going", "going"]},
            {"t": "Ana: \"My boyfriend is rich.\" ➜ She said that ___ boyfriend was rich.", "o": ["her", "my", "his"]}]},
    {"cls": "dark", "k": "Exercise 2", "name": "said or told", "h": "said or told?",
     "qs": [{"t": "My cousin ___ me a big secret.", "o": ["told", "said"]},
            {"t": "She ___ that she was tired.", "o": ["said", "told"]},
            {"t": "Grandma ___ everyone about the wedding.", "o": ["told", "said"]},
            {"t": "He ___ he was sorry.", "o": ["said", "told"]},
            {"t": "Who ___ you that?", "o": ["told", "said"]},
            {"t": "My mom ___ nothing at dinner.", "o": ["said", "told"]}]},
    {"k": "Exercise 3", "name": "Sunday lunch", "h": "The Sunday lunch drama 🍝", "story": [
        "At Sunday lunch, my aunt Rita ", ["told", "said"], " us that she ", ["was", "is"], " getting married again. My grandma ",
        ["said", "told"], " that she ", ["didn't", "doesn't"], " like the groom. Then my cousin whispered that the groom ",
        ["was", "is"], " twenty years younger! My mom ", ["told", "said"], " me not to say anything. My lips ",
        ["are", "were"], " sealed... but I'm telling YOU! 😂"]},
    {"cls": "accent", "k": "Reddit time · 15 min", "h": "Reddit Stories: AITA? 👀", "html":
        boxes(["<h3>AITA</h3><p>Am I the asshole? (= Am I wrong?)</p>", "<h3>OP</h3><p>original poster: the person who wrote the post</p>",
               "<h3>NTA</h3><p>Not the asshole: OP is right</p>", "<h3>YTA</h3><p>You're the asshole: OP is wrong</p>",
               "<h3>ESH</h3><p>Everyone sucks here</p>", "<h3>NAH</h3><p>No assholes here</p>"]) +
        P("1. We read the post together. 2. You retell it: <b>OP said that... Her sister told her that...</b> 3. Your verdict!") +
        model(["OP said that her mother-in-law told everyone her secret. I think OP is NTA because..."],
              "OP said that ______. My verdict: ______, because ______.")},
    {"k": "Speaking · 8 min", "h": "Your family gossip ☕", "html": P("Real or invented, you decide! I'll guess.") +
        boxes(["<h3>A funny thing someone in your family said</h3>", "<h3>A secret someone told you (an old one!)</h3>",
               "<h3>The biggest family drama you remember</h3>"]) +
        model(["My uncle told us that he saw a ghost in the kitchen. My dad said he was crazy!"], "My ______ told us that ______.")},
    {"cls": "dark", "k": "Wrap-up", "h": "Today's summary 🎯", "html": boxes([
        "<h3>Report</h3><p>am ➜ was · can ➜ could · will ➜ would</p>", "<h3>said / told</h3><p>told ME · said THAT</p>",
        "<h3>Gossip</h3><p>Guess what! · Apparently... · My lips are sealed.</p>"])},
    {"cls": "dark", "k": "Homework 📝", "h": "Your homework this week", "html": boxes([
        "<h3>📱 Games + 🎙️ audio</h3><p>Play the 4 games and record a 1-minute audio: report a piece of gossip (real or invented). The link is on WhatsApp.</p>",
        "<h3>✍️ Writing (optional)</h3><p>Write your own AITA post: 60 to 80 words, a family drama, real or invented. Start with AITA for...?</p>"])},
    {"cls": "accent", "k": "Extra time? ⭐ Bonus", "h": "Broken telephone 📞", "html":
        P("I whisper (say quickly) a gossip sentence. You report it: <b>You said that...</b> Then you say one and I report it. The crazier, the better!") +
        boxes([B("\"My cat is secretly a millionaire.\""), B("\"I will marry a famous singer.\""), B("\"My grandma can dance better than me.\"")]) +
        model(["You said that your cat was secretly a millionaire!"], "You said that ______.")},
], f"{R}/{d}/aula/index.html")

page("Family Gossip (homework)", ST, "tarefa:b:" + d, [
    {"cls": "dark", "k": "Homework · Reported speech", "h": "Gossip Training ☕", "h1": True, "html":
        P("1. Listen to the expressions and repeat out loud.") + P("2. Play the 4 games.") +
        P("3. Do the audio mission and send your score. 📲") + '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Listen and repeat", "h": "Gossip expressions", "cards": GOSSIP},
    {"k": "Game 1", "name": "Report it", "h": "Report the gossip",
     "qs": [{"t": "Tom: \"I am tired.\" ➜ He said he ___ tired.", "o": ["was", "is", "were"]},
            {"t": "Julia: \"I can drive.\" ➜ She said she ___ drive.", "o": ["could", "can", "would"]},
            {"t": "Grandpa: \"I will travel.\" ➜ He said he ___ travel.", "o": ["would", "will", "could"]},
            {"t": "Lia: \"I work at a bank.\" ➜ She said she ___ at a bank.", "o": ["worked", "works", "working"]},
            {"t": "Max: \"I'm going to move.\" ➜ He said he ___ going to move.", "o": ["was", "is", "were"]},
            {"t": "Sara: \"My brother is single.\" ➜ She said ___ brother was single.", "o": ["her", "my", "his"]}]},
    {"cls": "dark", "k": "Game 2", "name": "said or told", "h": "said or told?",
     "qs": [{"t": "She ___ me the truth.", "o": ["told", "said"]}, {"t": "They ___ that they were busy.", "o": ["said", "told"]},
            {"t": "My dad ___ us a funny story.", "o": ["told", "said"]}, {"t": "What did he ___?", "o": ["say", "tell"]},
            {"t": "Please ___ me everything!", "o": ["tell", "say"]}, {"t": "I ___ goodbye and left.", "o": ["said", "told"]}]},
    {"k": "Game 3 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "Guess what!", "label": "1", "o": ["Guess what!", "Guess who!", "Get out!"]},
            {"listen": "She said she was tired.", "label": "2", "o": ["She said she was tired.", "She says she is tired.", "She said she was tight."]},
            {"listen": "He told me a secret.", "label": "3", "o": ["He told me a secret.", "He told me the secret.", "He sold me a secret."]},
            {"listen": "My lips are sealed.", "label": "4", "o": ["My lips are sealed.", "My lips are sweet.", "My lips are dry."]},
            {"listen": "Apparently, she moved.", "label": "5", "o": ["Apparently, she moved.", "Apparently, she moves.", "Apparently, she loved."]},
            {"listen": "My sister-in-law is pregnant.", "label": "6", "o": ["My sister-in-law is pregnant.", "My mother-in-law is pregnant.", "My sister is pregnant."]}]},
    {"cls": "dark", "k": "Game 4", "name": "Family words", "h": "Who is it?",
     "qs": [{"t": "Your husband's mother", "o": ["mother-in-law", "stepmother", "aunt"]},
            {"t": "Your sister's son", "o": ["nephew", "niece", "cousin"]},
            {"t": "Your dad's new wife", "o": ["stepmother", "mother-in-law", "half-sister"]},
            {"t": "Same dad, different mom", "o": ["half-brother", "stepbrother", "brother-in-law"]},
            {"t": "The 'different' one in the family", "o": ["the black sheep", "the white sheep", "the black cat"]},
            {"t": "I ___ my mom: we're very similar.", "o": ["take after", "get along", "look for"]}]},
    {"cls": "accent", "k": "Audio mission 🎙️", "h": "Report a piece of gossip", "html":
        P("Record a 1-minute audio on WhatsApp and send it to me. Real or invented, you decide!") +
        boxes([B("Who told you?"), B("What did they say? (He said that...)"), B("What do you think?")]) +
        P("Example: Guess what! My cousin told me that she was moving to Canada. She said that her boyfriend lived there. I think...")},
    {"cls": "dark", "k": "Final score", "h": "Well done! 🏆", "final": "Now you can tell any gossip in English! ☕",
     "show": "Record your audio mission and send it to me too! 🎙️"},
], f"{R}/{d}/index.html")
print("ok")
