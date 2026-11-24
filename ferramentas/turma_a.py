import sys
sys.path.insert(0, __import__("os").path.dirname(__file__))
from build import page, boxes, wrong_right

R = "" + __import__("os").path.join(__import__("os").path.dirname(__file__), "..", "turma-a") + ""
ST = ""
def B(x): return f'<p class="big">{x}</p>'
def P(x): return f'<p>{x}</p>'

def model(read, frame):
    return ('<div class="cards"><div class="box"><p class="k">📖 Read</p>' + "".join(f'<p class="big">{r}</p>' for r in read) +
            f'</div><div class="box good"><p class="k">✍️ Your turn</p><p class="big">{frame}</p></div></div>')
def hw(items): return {"cls": "dark", "k": "Homework 📝", "h": "Your mission this week", "html": boxes([f"<h3>{a}</h3><p>{b}</p>" for a, b in items])}
def bonus(h, d): x = {"cls": "accent", "k": "Extra time? ⭐ Bonus", "h": h}; x.update(d); return x
GAMES = ("📱 Games", "Play the games on your phone. The link is on WhatsApp. Send your score!")
EXTRA = {
 "2026-11-24-verbs-actions": [hw([GAMES, ("🎭 Mime with mom", "Do 5 actions in mime. Mom guesses. Then you say the verb in English!")]),
    bonus("Odd one out! 🕵️", {"name": "Bonus", "tip": "Click the word that is NOT a verb. Then play Simon says: do the action only if I say \"Simon says\"!",
      "qs": [{"o": ["run", "jump", "table", "eat"], "okidx": 2, "speak": False}, {"o": ["pizza", "kick", "swim", "dance"], "okidx": 0, "speak": False},
             {"o": ["sleep", "drink", "laugh", "blue"], "okidx": 3, "speak": False}, {"o": ["watch", "happy", "play", "go"], "okidx": 1, "speak": False}]})],
 "2026-12-01-was-were": [hw([GAMES]),
    bonus("Emoji riddles 🧩", {"name": "Bonus", "tip": "Look at the emojis. Which sentence is correct?",
      "qs": [{"t": "⚽🏟️😃", "o": ["They were at the stadium. They were happy.", "They was at the stadium. They was happy.", "They were at the beach. They were sad."]},
             {"t": "🏠😴", "o": ["I was at home. I was tired.", "I were at home. I were tired.", "I was at school. I was hungry."]},
             {"t": "🏖️☀️🥵", "o": ["It was hot at the beach.", "It were hot at the beach.", "It was cold at the beach."]},
             {"t": "👦👧🍕😋", "o": ["My friends were hungry.", "My friends was hungry.", "My friends were angry."]}]})],
 "2026-12-08-new-verbs": [hw([GAMES, ("🎙️ Audio for the teacher", "30 seconds: 3 things you did last weekend. I ate... I bought... I slept...")]),
    bonus("Emoji past 🎮", {"name": "Bonus", "tip": "Look at the emojis and choose the verb.",
      "qs": [{"t": "🛒🎮 I ___ a new game.", "o": ["bought", "buyed", "took"]}, {"t": "🧃 She ___ orange juice.", "o": ["drank", "drinked", "made"]},
             {"t": "😴🛏️ He ___ for ten hours!", "o": ["slept", "sleeped", "got"]}, {"t": "🎂 My mom ___ a cake.", "o": ["made", "maked", "gave"]},
             {"t": "🎁 I ___ a present to my friend.", "o": ["gave", "gived", "came"]}]})],
 "2026-12-15-did-you": [hw([GAMES]),
    bonus("Emoji answers ✅❌", {"name": "Bonus", "tip": "Look at the emoji and answer!",
      "qs": [{"t": "Did you play football? ✅⚽", "o": ["Yes, I did.", "No, I didn't.", "Yes, I do."]},
             {"t": "Did you eat sushi? ❌🍣", "o": ["No, I didn't.", "Yes, I did.", "No, I don't."]},
             {"t": "Did you watch anime? ✅📺", "o": ["Yes, I did.", "No, I didn't.", "Yes, I watched did."]},
             {"t": "Did you go to the beach? ❌🏖️", "o": ["No, I didn't.", "Yes, I did.", "No, I wasn't."]},
             {"t": "🎮 ➜ Make the question", "o": ["Did you play video games?", "Did you played video games?", "You did play video games?"]}]})],
 "2026-12-22-final-match": [hw([("📱 Vacation challenge", "1 round per week, 10 minutes."), ("📸🎙️ Vacation audio", "Once a week: send me a photo of something you did + 1 sentence. I went to the beach!")]),
    bonus("Penalty shootout! ⚽", {"html": P("I say a verb. You have 5 seconds to say the past. Correct = GOAL! Then you say a verb and I take the penalty.") +
      boxes([B("go"), B("eat"), B("buy"), B("sleep"), B("win"), B("see"), B("make"), B("drink"), B("take"), B("play")])})],
}
_page = page
def page(title, st, key, slides, path):
    for k, extra in EXTRA.items():
        if f"/{k}/aula/" in path:
            slides = slides + extra
    _page(title, st, key, slides, path)

PAST1 = [("play", "played"), ("watch", "watched"), ("kick", "kicked"), ("score", "scored"),
         ("go", "went"), ("see", "saw"), ("win", "won"), ("eat", "ate")]
NEW = [("make", "made"), ("get", "got"), ("come", "came"), ("take", "took"),
       ("buy", "bought"), ("sleep", "slept"), ("drink", "drank"), ("give", "gave")]
VERB = lambda t: {"t": t, "o": ["✅ Verb", "❌ Not a verb"], "fixed": True, "speak": False}
NOTV = lambda t: {"t": t, "o": ["✅ Verb", "❌ Not a verb"], "okidx": 1, "speak": False}

def find(sentence, verb):
    words = sentence.rstrip(".!?").split()
    return {"t": "👉 " + sentence, "o": words, "okidx": words.index(verb), "speak": sentence}

def final(txt): return {"cls": "dark", "k": "Final score", "h": "Congratulations, champion! 🏆", "final": txt}

# =========================== AULA 1: 24/11 verbs = actions ===========================
d = "2026-11-24-verbs-actions"
is_verb = [VERB("run"), NOTV("ball"), VERB("eat"), NOTV("pizza"), VERB("jump"), NOTV("happy"), VERB("watch"), NOTV("school")]
find_v = [find("I play football every day.", "play"), find("Kai watches anime.", "watches"),
          find("We eat pizza on Friday.", "eat"), find("The players run fast.", "run"),
          find("My mom drinks coffee.", "drinks"), find("He kicked the ball.", "kicked")]
to_past = [{"t": "I play football. ➜ Yesterday I ___ football.", "o": ["played", "play", "plays"]},
           {"t": "We watch a match. ➜ Last night we ___ a match.", "o": ["watched", "watch", "watching"]},
           {"t": "He goes to school. ➜ Yesterday he ___ to school.", "o": ["went", "goes", "goed"]},
           {"t": "They win the game. ➜ Last Sunday they ___ the game.", "o": ["won", "win", "winned"]},
           {"t": "I eat a sandwich. ➜ Yesterday I ___ a sandwich.", "o": ["ate", "eat", "eated"]},
           {"t": "She sees her friend. ➜ Last week she ___ her friend.", "o": ["saw", "see", "seed"]}]
page("Verbs = Actions! (aula)", ST, "aula:" + d, [
    {"cls": "dark", "k": "English class · Verbs", "h": "Verbs = Actions! 🏃", "h1": True,
     "html": B("What do you DO? What did you DO?")},
    {"k": "Warm-up · 5 min", "h": "Last week's mission", "html": boxes([
        "<h3>Did you play the verb games?</h3>", "<h3>What was your score?</h3>",
        "<h3>Which game was difficult?</h3>", "<h3>What did you do on the weekend?</h3>"])},
    {"k": "What is a verb?", "h": "A verb is an ACTION", "html":
        boxes([B("🏃 run"), B("⚽ kick"), B("🍕 eat"), B("📺 watch")]) +
        B("Test: Can you DO it? ➜ Then it is a verb! ✅") + P("ball ⚽ ➜ Can you ball? ❌ ➜ Not a verb.") + model(["I <b>run</b> in the park.", "My friends <b>play</b> video games."], "I ______ every day. 🏃")},
    {"cls": "accent", "k": "Mime game · 5 min", "h": "Show me the action! 🎭", "html":
        P("I say a verb, you do the action. Then you say a verb and I do it!") +
        boxes([B("run"), B("jump"), B("sleep"), B("kick"), B("swim"), B("dance"), B("drink"), B("laugh")])},
    {"k": "Exercise 1", "name": "Is it a verb?", "h": "Is it a verb?", "tip": "Remember the test: can you DO it?", "qs": is_verb},
    {"cls": "dark", "k": "Exercise 2", "name": "Find the verb", "h": "Find the verb!", "tip": "Click the ACTION word in each sentence.", "qs": find_v},
    {"k": "Review", "h": "Past: remember?", "cards": PAST1},
    {"cls": "dark", "k": "Exercise 3", "name": "Now in the past", "h": "Now in the past!", "qs": to_past},
    {"k": "Speaking · 6 min", "h": "Tell me 3 actions from yesterday", "html":
        boxes([B("First, I ..."), B("Then, I ..."), B("After that, I ...")]) + P("Example: First, I woke up. Then, I ate bread. After that, I played video games.")},
    {"cls": "dark", "k": "Wrap-up", "h": "Great job today! 🎉", "html":
        boxes(["<h3>Verb = action ✅</h3><p>run, eat, kick, watch</p>", "<h3>Past ⏪</h3><p>play ➜ played</p><p>go ➜ went</p>"])},
], f"{R}/{d}/aula/index.html")

page("Verbs = Actions! (homework)", ST, "tarefa:" + d, [
    {"cls": "dark", "k": "Homework · Verbs", "h": "Action Training 🏃", "h1": True, "html":
        P("1. Listen to the verbs and repeat out loud.") + P("2. Play the 4 games.") +
        P("3. Show your final score to your mom! 📸") + '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Review", "h": "Past verbs", "cards": PAST1},
    {"k": "Game 1", "name": "Is it a verb?", "h": "Is it a verb?", "tip": "Can you DO it? Then it is a verb!",
     "qs": [VERB("sleep"), NOTV("table"), VERB("drink"), NOTV("blue"), VERB("kick"), NOTV("dog"), VERB("swim"), NOTV("game")]},
    {"cls": "dark", "k": "Game 2", "name": "Find the verb", "h": "Find the verb!", "tip": "Click the ACTION word.",
     "qs": [find("I watch anime at night.", "watch"), find("My friends play video games.", "play"),
            find("She runs in the park.", "runs"), find("We scored a goal.", "scored"),
            find("They ate hamburgers.", "ate"), find("He sees the stadium.", "sees")]},
    {"k": "Game 3 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the word you heard.",
     "qs": [{"listen": "played", "o": ["played", "play", "plate"]}, {"listen": "went", "o": ["went", "want", "win"]},
            {"listen": "kicked", "o": ["kicked", "kick", "kid"]}, {"listen": "ate", "o": ["ate", "eat", "at"]},
            {"listen": "watched", "o": ["watched", "watch", "wash"]}, {"listen": "saw", "o": ["saw", "see", "say"]}]},
    {"cls": "dark", "k": "Game 4", "name": "Now in the past", "h": "Now in the past!",
     "qs": [{"t": "I kick the ball. ➜ Yesterday I ___ the ball.", "o": ["kicked", "kick", "kicks"]},
            {"t": "We go to the beach. ➜ Last Sunday we ___ to the beach.", "o": ["went", "go", "goed"]},
            {"t": "He scores a goal. ➜ Yesterday he ___ a goal.", "o": ["scored", "score", "scores"]},
            {"t": "I see my friends. ➜ Last week I ___ my friends.", "o": ["saw", "see", "seed"]},
            {"t": "They watch TV. ➜ Last night they ___ TV.", "o": ["watched", "watch", "watching"]},
            {"t": "She eats pizza. ➜ Yesterday she ___ pizza.", "o": ["ate", "eat", "eated"]}]},
    final("You know what a verb is now: an ACTION! Keep going! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 2: 01/12 was / were ===========================
d = "2026-12-01-was-were"
ww = [{"t": "I ___ happy.", "o": ["was", "were"], "fixed": True, "speak": "I was happy."},
      {"t": "They ___ at the stadium.", "o": ["were", "was"], "speak": "They were at the stadium."},
      {"t": "The match ___ amazing!", "o": ["was", "were"], "speak": "The match was amazing!"},
      {"t": "We ___ tired.", "o": ["were", "was"], "speak": "We were tired."},
      {"t": "The hero ___ very strong.", "o": ["was", "were"], "speak": "The hero was very strong."},
      {"t": "You ___ late!", "o": ["were", "was"], "speak": "You were late!"},
      {"t": "My friends ___ at school.", "o": ["were", "was"], "speak": "My friends were at school."},
      {"t": "It ___ cold yesterday.", "o": ["was", "were"], "speak": "It was cold yesterday."}]
page("Was / Were (aula)", ST, "aula:" + d, [
    {"cls": "dark", "k": "English class · Past", "h": "The match WAS amazing! ⚽", "h1": True, "html": B("was / were")},
    {"k": "Warm-up · 5 min", "h": "Show me your score!", "html": boxes([
        "<h3>What was your score?</h3>", "<h3>Which game was easy?</h3>", "<h3>Say 3 verbs! Do the action!</h3>"])},
    {"k": "New!", "h": "was / were = past of am / is / are", "html":
        '<table><tr><th>Now</th><th>Past</th></tr><tr><td>I am</td><td><b>I was</b></td></tr>'
        '<tr><td>he / she / it is</td><td><b>he / she / it was</b></td></tr>'
        '<tr><td>you / we / they are</td><td><b>you / we / they were</b></td></tr></table>' +
        model(["Yesterday I <b>was</b> at home. 🏠", "My friends <b>were</b> at school. 🏫"], "Yesterday at 8 pm, I was ______.")},
    {"k": "Exercise 1", "name": "was or were", "h": "was or were?", "qs": ww},
    {"cls": "dark", "k": "Negative", "h": "wasn't / weren't", "html":
        boxes([B("was not ➜ <b>wasn't</b>"), B("were not ➜ <b>weren't</b>")]) +
        model(["The game <b>wasn't</b> boring.", "The players <b>weren't</b> tired."], "Yesterday I wasn't ______.")},
    {"k": "Exercise 2", "name": "Which is correct", "h": "Which sentence is correct?", "pre": wrong_right(["They <b>was</b> happy."], ["They <b>were</b> happy."]),
     "qs": [{"o": ["He wasn't at home.", "He weren't at home."]}, {"o": ["We weren't tired.", "We wasn't tired."]},
            {"o": ["The movie wasn't good.", "The movie weren't good."]}, {"o": ["You were at the park.", "You was at the park."]},
            {"o": ["I was hungry.", "I were hungry."]}]},
    {"cls": "dark", "k": "Exercise 3 · Anime", "name": "Anime story", "h": "Complete the story", "story": [
        "Yesterday ", ["was", "were"], " a big day. Kai and his friends ", ["were", "was"], " at the tournament. The fight ",
        ["was", "were"], " hard and the monsters ", ["were", "was"], " very big! Kai ", ["was", "were"],
        " tired, but he ", ["wasn't", "weren't"], " scared. In the end, his team ", ["was", "were"], " the winner!"]},
    {"k": "Speaking · 6 min", "h": "Answer with I was...", "html": boxes([
        "<h3>Where were you yesterday at 8 pm?</h3>", "<h3>Was your weekend good?</h3>",
        "<h3>Who was the best player in the last match you saw?</h3>", "<h3>Was the homework easy?</h3>"])},
    {"cls": "dark", "k": "Wrap-up", "h": "Great job today! 🎉", "html":
        boxes(["<h3>I / he / she / it</h3><p>was / wasn't</p>", "<h3>you / we / they</h3><p>were / weren't</p>"])},
], f"{R}/{d}/aula/index.html")

page("Was / Were (homework)", ST, "tarefa:" + d, [
    {"cls": "dark", "k": "Homework · Past", "h": "was / were Training ⚽", "h1": True, "html":
        P("1. Listen and repeat out loud.") + P("2. Play the 4 games.") + P("3. Show your final score to your mom! 📸") +
        '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Listen and repeat", "h": "was / were", "cards": [("I", "was"), ("he", "was"), ("she", "was"), ("it", "was"),
                                                           ("you", "were"), ("we", "were"), ("they", "were"), ("my friends", "were")]},
    {"k": "Game 1", "name": "was or were", "h": "was or were?",
     "qs": [{"t": "She ___ at the beach.", "o": ["was", "were"], "fixed": True, "speak": "She was at the beach."},
            {"t": "We ___ happy.", "o": ["were", "was"], "speak": "We were happy."},
            {"t": "The game ___ fun.", "o": ["was", "were"], "speak": "The game was fun."},
            {"t": "They ___ at home.", "o": ["were", "was"], "speak": "They were at home."},
            {"t": "I ___ hungry.", "o": ["was", "were"], "speak": "I was hungry."},
            {"t": "You ___ fast!", "o": ["were", "was"], "speak": "You were fast!"},
            {"t": "My dog ___ in the garden.", "o": ["was", "were"], "speak": "My dog was in the garden."},
            {"t": "The players ___ tired.", "o": ["were", "was"], "speak": "The players were tired."}]},
    {"cls": "dark", "k": "Game 2", "name": "Which is correct", "h": "Which sentence is correct?",
     "qs": [{"o": ["I wasn't sad.", "I weren't sad."]}, {"o": ["They weren't at school.", "They wasn't at school."]},
            {"o": ["It wasn't hot.", "It weren't hot."]}, {"o": ["We were at the park.", "We was at the park."]},
            {"o": ["He was my friend.", "He were my friend."]}, {"o": ["You weren't late.", "You wasn't late."]}]},
    {"k": "Game 3 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "He was at the stadium.", "label": "1", "o": ["He was at the stadium.", "He was at school.", "He was at home."]},
            {"listen": "They were happy.", "label": "2", "o": ["They were happy.", "They were hungry.", "They were tired."]},
            {"listen": "It was cold.", "label": "3", "o": ["It was cold.", "It was hot.", "It was fun."]},
            {"listen": "We were at the beach.", "label": "4", "o": ["We were at the beach.", "We were at the park.", "We were at the mall."]},
            {"listen": "I wasn't sad.", "label": "5", "o": ["I wasn't sad.", "I was sad.", "I wasn't bad."]},
            {"listen": "The game was amazing.", "label": "6", "o": ["The game was amazing.", "The game was boring.", "The game was easy."]}]},
    {"cls": "dark", "k": "Game 4", "name": "Football story", "h": "Complete the story", "story": [
        "Last Sunday ", ["was", "were"], " great! My friends and I ", ["were", "was"], " at the park. The weather ",
        ["was", "were"], " hot. We ", ["were", "was"], " very happy. Our team ", ["wasn't", "weren't"], " bad!"]},
    final("was and were are not a problem for you anymore! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 3: 08/12 new irregular verbs ===========================
d = "2026-12-08-new-verbs"
page("Level Up: New Verbs (aula)", ST, "aula:" + d, [
    {"cls": "dark", "k": "English class · Past", "h": "Level up! New verbs 🎮", "h1": True, "html": B("New irregular verbs + time words")},
    {"k": "Warm-up · 5 min", "h": "was or were?", "html": boxes([
        "<h3>Where were you on Saturday?</h3>", "<h3>Was the homework easy?</h3>", "<h3>Were you tired today?</h3>"])},
    {"k": "Time words", "h": "When? ⏰", "html": boxes([B("yesterday"), B("last night"), B("last week"), B("last Saturday"), B("two days ago")]) +
        model(["I played football <b>yesterday</b>.", "We watched a movie <b>two days ago</b>."], "Last week, I ______.")},
    {"cls": "dark", "k": "New verbs", "h": "8 new irregular verbs", "cards": NEW, "html": model(["Yesterday I <b>drank</b> juice.", "Last week I <b>bought</b> a ball."], "Last weekend I ______. (made / got / bought...)")},
    {"k": "Exercise 1", "name": "Choose the past", "h": "Choose the past form",
     "qs": [{"t": "make", "o": ["made", "maked", "makes"]}, {"t": "get", "o": ["got", "getted", "gets"]},
            {"t": "come", "o": ["came", "comed", "comes"]}, {"t": "take", "o": ["took", "taked", "takes"]},
            {"t": "buy", "o": ["bought", "buyed", "buys"]}, {"t": "sleep", "o": ["slept", "sleeped", "sleeps"]},
            {"t": "drink", "o": ["drank", "drinked", "drinks"]}, {"t": "give", "o": ["gave", "gived", "gives"]}]},
    {"cls": "dark", "k": "Exercise 2", "name": "Time words", "h": "Complete with the time word",
     "qs": [{"t": "I played football ___.", "o": ["yesterday", "tomorrow", "now"]},
            {"t": "She came home last ___.", "o": ["night", "tomorrow", "now"]},
            {"t": "We bought pizza two days ___.", "o": ["ago", "last", "yesterday"]},
            {"t": "I slept a lot last ___.", "o": ["weekend", "today", "tomorrow"]},
            {"t": "They watched a movie ___ Saturday.", "o": ["last", "ago", "next"]}]},
    {"k": "Exercise 3 · Football", "name": "Football story", "h": "Complete the story", "story": [
        "Last Saturday, Leo ", ["got", "get"], " up early. He ", ["drank", "drink"], " orange juice and ", ["took", "take"],
        " his ball. He ", ["came", "come"], " to the park with his friends. They ", ["made", "make"],
        " two teams and played for two hours. After the game, Leo's dad ", ["bought", "buy"],
        " ice cream for everyone. Leo ", ["slept", "sleep"], " very well that night!"]},
    {"cls": "dark", "k": "Speaking · 6 min", "h": "My last weekend", "html": P("Use the new verbs!") + boxes([
        B("I got up at ..."), B("I ate / I drank ..."), B("I slept ..."), B("I bought / I took ...")])},
    {"k": "Wrap-up", "h": "Great job today! 🎉", "html": boxes([
        "<h3>New verbs</h3><p>made, got, came, took</p><p>bought, slept, drank, gave</p>",
        "<h3>Time words</h3><p>yesterday, last week, two days ago</p>"])},
], f"{R}/{d}/aula/index.html")

page("Level Up: New Verbs (homework)", ST, "tarefa:" + d, [
    {"cls": "dark", "k": "Homework · Past", "h": "Level up training 🎮", "h1": True, "html":
        P("1. Listen to the new verbs and repeat out loud.") + P("2. Play the 4 games.") + P("3. Show your final score to your mom! 📸") +
        '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "New verbs", "h": "8 new irregular verbs", "cards": NEW},
    {"k": "Game 1", "name": "Choose the past", "h": "Choose the past form",
     "qs": [{"t": "buy", "o": ["bought", "buyed", "boughted"]}, {"t": "sleep", "o": ["slept", "sleeped", "slep"]},
            {"t": "take", "o": ["took", "taked", "tooked"]}, {"t": "make", "o": ["made", "maked", "mad"]},
            {"t": "drink", "o": ["drank", "drinked", "drinks"]}, {"t": "give", "o": ["gave", "gived", "gaved"]},
            {"t": "come", "o": ["came", "comed", "comes"]}, {"t": "get", "o": ["got", "getted", "gotted"]}]},
    {"cls": "dark", "k": "Game 2", "name": "It is the past of", "h": "It is the past of...",
     "qs": [{"t": "bought", "o": ["buy", "bring"]}, {"t": "slept", "o": ["sleep", "sit"]}, {"t": "took", "o": ["take", "talk"]},
            {"t": "gave", "o": ["give", "go"]}, {"t": "came", "o": ["come", "make"]}, {"t": "drank", "o": ["drink", "drive"]}]},
    {"k": "Game 3 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the word you heard.",
     "qs": [{"listen": "bought", "label": "1", "o": ["bought", "boat", "but"]}, {"listen": "came", "label": "2", "o": ["came", "come", "game"]},
            {"listen": "took", "label": "3", "o": ["took", "take", "look"]}, {"listen": "slept", "label": "4", "o": ["slept", "sleep", "slip"]},
            {"listen": "made", "label": "5", "o": ["made", "make", "mad"]}, {"listen": "gave", "label": "6", "o": ["gave", "give", "game"]}]},
    {"cls": "dark", "k": "Game 4", "name": "Time words", "h": "Complete with the time word",
     "qs": [{"t": "I drank juice ___.", "o": ["yesterday", "tomorrow", "now"]},
            {"t": "We came home last ___.", "o": ["night", "now", "tomorrow"]},
            {"t": "He bought a ball three days ___.", "o": ["ago", "last", "next"]},
            {"t": "They made a cake ___ Sunday.", "o": ["last", "ago", "next"]},
            {"t": "I slept at a friend's house last ___.", "o": ["week", "today", "tomorrow"]}]},
    final("You leveled up! 8 new verbs in your English! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 4: 15/12 Did you...? ===========================
d = "2026-12-15-did-you"
page("Did you score? (aula)", ST, "aula:" + d, [
    {"cls": "dark", "k": "English class · Past", "h": "Did you score? ⚽", "h1": True, "html": B("Questions in the past")},
    {"k": "Warm-up · 5 min", "h": "Quick! Say the past!", "cards": [("go", "went"), ("eat", "ate"), ("buy", "bought"), ("sleep", "slept"),
                                                                ("play", "played"), ("see", "saw"), ("drink", "drank"), ("make", "made")]},
    {"k": "New!", "h": "Did + you + verb?", "pre": wrong_right(["Did you <b>played</b>?"], ["Did you <b>play</b>?"]), "html":
        boxes([B("Did you play football?") + P("✅ Yes, I did."), B("Did you watch anime?") + P("❌ No, I didn't.")]) +
        B("After <b>did</b>, the verb goes back to normal!") + model(["<b>Did</b> you <b>watch</b> anime yesterday? Yes, I did."], "Did you ______ yesterday? 🤔")},
    {"cls": "dark", "k": "Exercise 1", "name": "Correct question", "h": "Which question is correct?",
     "qs": [{"o": ["Did you play video games?", "Did you played video games?"]}, {"o": ["Did you eat pizza?", "Did you ate pizza?"]},
            {"o": ["Did you go to school?", "Did you went to school?"]}, {"o": ["Did you sleep well?", "Did you slept well?"]},
            {"o": ["Did you watch the match?", "Did you watched the match?"]}]},
    {"k": "Exercise 2", "name": "Short answers", "h": "Answer the question",
     "qs": [{"t": "Did you play football? ✅", "o": ["Yes, I did.", "Yes, I do.", "Yes, I was."]},
            {"t": "Did you watch TV? ❌", "o": ["No, I didn't.", "No, I don't.", "No, I wasn't."]},
            {"t": "Did you eat cake? ✅", "o": ["Yes, I did.", "Yes, I ate did.", "Yes, I do."]},
            {"t": "Did you go to the beach? ❌", "o": ["No, I didn't.", "No, I didn't went.", "No, I don't."]},
            {"t": "Did you sleep well? ✅", "o": ["Yes, I did.", "Yes, I slept did.", "Yes, I does."]}]},
    {"cls": "accent", "k": "Speaking · 8 min", "h": "Interview the teacher! 🎤", "html":
        P("Ask me! Then I ask you.") + boxes([B("Did you ... watch a movie yesterday?"), B("Did you ... eat pizza last week?"),
                                              B("Did you ... go to the beach?"), B("Did you ... play a video game?")])},
    {"cls": "dark", "k": "Game · 7 min", "h": "Guess what I did! 🕵️", "html":
        P("I think of something I did yesterday. You ask: Did you ...? I answer: Yes, I did / No, I didn't.") +
        B("You have 10 questions to guess!")},
    {"k": "Wrap-up", "h": "Great job today! 🎉", "html": boxes([
        "<h3>Question</h3><p>Did you play?</p>", "<h3>Answers</h3><p>Yes, I did. ✅</p><p>No, I didn't. ❌</p>"])},
], f"{R}/{d}/aula/index.html")

page("Did you score? (homework)", ST, "tarefa:" + d, [
    {"cls": "dark", "k": "Homework · Past", "h": "Question training 🎤", "h1": True, "html":
        P("1. Listen and repeat out loud.") + P("2. Play the 4 games.") + P("3. Show your final score to your mom! 📸") +
        '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Listen and repeat", "h": "Questions and answers", "cards": [
        ("Did you play?", "Yes, I did."), ("Did you eat?", "No, I didn't."), ("Did you go?", "Yes, I did."),
        ("Did you watch?", "No, I didn't."), ("Did you sleep?", "Yes, I did."), ("Did you win?", "No, I didn't.")]},
    {"k": "Game 1", "name": "Correct question", "h": "Which question is correct?",
     "qs": [{"o": ["Did you buy a ball?", "Did you bought a ball?"]}, {"o": ["Did you drink juice?", "Did you drank juice?"]},
            {"o": ["Did you win the game?", "Did you won the game?"]}, {"o": ["Did you see the goal?", "Did you saw the goal?"]},
            {"o": ["Did you make a cake?", "Did you made a cake?"]}, {"o": ["Did you come home?", "Did you came home?"]}]},
    {"cls": "dark", "k": "Game 2", "name": "Short answers", "h": "Answer the question",
     "qs": [{"t": "Did you watch anime? ✅", "o": ["Yes, I did.", "Yes, I do.", "Yes, I was."]},
            {"t": "Did you play tennis? ❌", "o": ["No, I didn't.", "No, I don't.", "No, I wasn't."]},
            {"t": "Did you eat rice? ✅", "o": ["Yes, I did.", "Yes, I does.", "Yes, I ate did."]},
            {"t": "Did you go to the mall? ❌", "o": ["No, I didn't.", "No, I didn't went.", "No, I don't."]},
            {"t": "Did you sleep late? ✅", "o": ["Yes, I did.", "Yes, I do.", "Yes, I slept did."]},
            {"t": "Did you win? ❌", "o": ["No, I didn't.", "No, I don't.", "No, I didn't won."]}]},
    {"k": "Game 3", "name": "Make the question", "h": "Make the question",
     "qs": [{"t": "You watched TV. ➜", "o": ["Did you watch TV?", "Did you watched TV?", "You did watch TV?"]},
            {"t": "You played football. ➜", "o": ["Did you play football?", "Did you played football?", "Do you played football?"]},
            {"t": "You went to the park. ➜", "o": ["Did you go to the park?", "Did you went to the park?", "Did you goed to the park?"]},
            {"t": "You ate pizza. ➜", "o": ["Did you eat pizza?", "Did you ate pizza?", "You did eat pizza?"]},
            {"t": "You bought a game. ➜", "o": ["Did you buy a game?", "Did you bought a game?", "Did you buyed a game?"]},
            {"t": "You slept well. ➜", "o": ["Did you sleep well?", "Did you slept well?", "Do you slept well?"]}]},
    {"cls": "dark", "k": "Game 4 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the question you heard.",
     "qs": [{"listen": "Did you play football?", "label": "1", "o": ["Did you play football?", "Did you watch football?", "Did you play tennis?"]},
            {"listen": "Did you eat cake?", "label": "2", "o": ["Did you eat cake?", "Did you make cake?", "Did you eat rice?"]},
            {"listen": "Did you go to school?", "label": "3", "o": ["Did you go to school?", "Did you go to the park?", "Did you come to school?"]},
            {"listen": "Did you sleep well?", "label": "4", "o": ["Did you sleep well?", "Did you play well?", "Did you sleep late?"]},
            {"listen": "Did you buy a ball?", "label": "5", "o": ["Did you buy a ball?", "Did you buy a game?", "Did you kick a ball?"]},
            {"listen": "Did you win?", "label": "6", "o": ["Did you win?", "Did you go?", "Did you eat?"]}]},
    final("Now you can ask questions in the past! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 5: 22/12 Final match + vacation ===========================
d = "2026-12-22-final-match"
page("The Final Match (aula)", ST, "aula:" + d, [
    {"cls": "dark", "k": "Last class of the year", "h": "The Final Match 🏆", "h1": True, "html": B("Review championship!")},
    {"k": "How it works", "h": "4 rounds. Every correct answer is a goal! ⚽", "html": boxes([
        B("Round 1 · Past verbs"), B("Round 2 · was / were"), B("Round 3 · Did you...?"), B("Round 4 · Story")])},
    {"cls": "dark", "k": "Round 1", "name": "Past verbs", "h": "Past verbs",
     "qs": [{"t": "play", "o": ["played", "plaid", "playd"]}, {"t": "go", "o": ["went", "goed", "wented"]},
            {"t": "buy", "o": ["bought", "buyed", "boughted"]}, {"t": "eat", "o": ["ate", "eated", "eaten"]},
            {"t": "sleep", "o": ["slept", "sleeped", "slep"]}, {"t": "win", "o": ["won", "winned", "wan"]},
            {"t": "take", "o": ["took", "taked", "tooked"]}, {"t": "watch", "o": ["watched", "watcht", "wotched"]}]},
    {"k": "Round 2", "name": "was / were", "h": "was or were?",
     "qs": [{"t": "The match ___ amazing.", "o": ["was", "were"], "fixed": True, "speak": "The match was amazing."},
            {"t": "My friends ___ at the park.", "o": ["were", "was"], "speak": "My friends were at the park."},
            {"t": "I ___ tired.", "o": ["was", "were"], "speak": "I was tired."},
            {"t": "We ___ happy.", "o": ["were", "was"], "speak": "We were happy."},
            {"t": "It ___ cold.", "o": ["was", "were"], "speak": "It was cold."},
            {"t": "They ___ at home.", "o": ["weren't", "wasn't"], "speak": "They weren't at home."}]},
    {"cls": "dark", "k": "Round 3", "name": "Did you", "h": "Did you...?",
     "qs": [{"o": ["Did you go to the beach?", "Did you went to the beach?"]}, {"o": ["Did you eat pizza?", "Did you ate pizza?"]},
            {"t": "Did you win? ✅", "o": ["Yes, I did.", "Yes, I do.", "Yes, I won did."]},
            {"t": "Did you sleep late? ❌", "o": ["No, I didn't.", "No, I don't.", "No, I wasn't."]},
            {"o": ["Did you see the goal?", "Did you saw the goal?"]},
            {"t": "Did you play video games? ✅", "o": ["Yes, I did.", "Yes, I played did.", "Yes, I does."]}]},
    {"k": "Round 4", "name": "Story", "h": "The championship story", "story": [
        "This year, you ", ["were", "was"], " a great English student. You ", ["learned", "learn"], " a lot of verbs. You ",
        ["played", "play"], " games, you ", ["watched", "watch"], " videos and you ", ["taught", "teach"],
        " your mom new words. Your teacher ", ["was", "were"], " very proud. You ", ["didn't", "wasn't"], " give up!"]},
    {"cls": "dark", "k": "Final score", "h": "Champion! 🏆", "final": "What a season! You were amazing this year!", "send": False},
    {"cls": "accent", "k": "Certificate time 🎓", "h": "Congratulations!", "html": B("You finished the year! 🎉") + P("Your certificate is here!")},
    {"k": "Vacation challenge", "h": "Your vacation mission 🏖️", "html": boxes([
        B("1 round per week"), B("10 minutes"), B("Send your score!")]) + P("Don't forget your English on vacation! See you in February! 💙")},
], f"{R}/{d}/aula/index.html")

def wk(n, qs, cls=""):
    return {"cls": cls, "k": f"Week {n}", "name": f"Week {n}", "h": f"Week {n} challenge", "tip": "Play this round in week " + str(n) + ".", "qs": qs}

page("Vacation Challenge", ST, "tarefa:" + d, [
    {"cls": "dark", "k": "Vacation · 2026/2027", "h": "Vacation Challenge 🏖️", "h1": True, "html":
        P("Your mission: play 1 round per week. It takes 10 minutes!") + P("At the end, send your score to the teacher. 📲") +
        P("Show your score to your mom! 📸") + '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Listen and repeat", "h": "All your verbs", "cards": PAST1 + NEW},
    wk(1, [{"t": "go", "o": ["went", "goed", "wented"]}, {"t": "make", "o": ["made", "maked", "mad"]},
           {"t": "play", "o": ["played", "plaid", "playd"]}, {"t": "drink", "o": ["drank", "drinked", "drinks"]},
           {"t": "see", "o": ["saw", "seed", "seen"]}, {"t": "get", "o": ["got", "getted", "gotted"]}]),
    wk(2, [{"t": "I ___ at the beach.", "o": ["was", "were"], "fixed": True, "speak": "I was at the beach."},
           {"t": "They ___ happy.", "o": ["were", "was"], "speak": "They were happy."},
           {"t": "The weather ___ hot.", "o": ["was", "were"], "speak": "The weather was hot."},
           {"t": "We ___ on vacation.", "o": ["were", "was"], "speak": "We were on vacation."},
           {"t": "My cousin ___ at my house.", "o": ["was", "were"], "speak": "My cousin was at my house."},
           {"t": "The days ___ boring!", "o": ["weren't", "wasn't"], "speak": "The days weren't boring!"}], "dark"),
    wk(3, [{"listen": "bought", "label": "1", "o": ["bought", "boat", "but"]}, {"listen": "went", "label": "2", "o": ["went", "want", "win"]},
           {"listen": "slept", "label": "3", "o": ["slept", "sleep", "slip"]}, {"listen": "came", "label": "4", "o": ["came", "come", "game"]},
           {"listen": "watched", "label": "5", "o": ["watched", "watch", "wash"]}, {"listen": "took", "label": "6", "o": ["took", "take", "look"]}]),
    wk(4, [{"o": ["Did you swim?", "Did you swam?"]}, {"o": ["Did you buy ice cream?", "Did you bought ice cream?"]},
           {"t": "Did you travel? ✅", "o": ["Yes, I did.", "Yes, I do.", "Yes, I was."]},
           {"t": "Did you go to school? ❌", "o": ["No, I didn't.", "No, I don't.", "No, I didn't went."]},
           {"o": ["Did you watch a movie?", "Did you watched a movie?"]},
           {"t": "Did you sleep late? ✅", "o": ["Yes, I did.", "Yes, I slept did.", "Yes, I does."]}], "dark"),
    wk(5, [{"t": "I swam in the sea ___.", "o": ["yesterday", "tomorrow", "now"]},
           {"t": "We ate pizza two days ___.", "o": ["ago", "last", "next"]},
           {"t": "Yesterday I ___ a new game.", "o": ["bought", "buy", "buyed"]},
           {"t": "Last week we ___ to the beach.", "o": ["went", "go", "goed"]},
           {"t": "My mom ___ a cake.", "o": ["made", "make", "maked"]},
           {"t": "I ___ my friends last Saturday.", "o": ["saw", "see", "seed"]}]),
    {"cls": "dark", "k": "Week 6", "name": "Week 6", "h": "Week 6: my vacation story", "story": [
        "My vacation ", ["was", "were"], " great! I ", ["slept", "sleep"], " a lot and I ", ["played", "play"],
        " video games. My family and I ", ["went", "go"], " to the beach. We ", ["ate", "eat"], " ice cream and we ",
        ["were", "was"], " very happy. I ", ["didn't", "wasn't"], " forget my English!"]},
    final("You didn't forget your English on vacation! See you in February! 💙"),
], f"{R}/{d}/index.html")
print("ok")
