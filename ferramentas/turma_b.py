"""Turma B (nível A2/B1): aulas de 24/11 a 22/12/2026. Conteúdo original."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import page, boxes, wrong_right

R = os.path.join(os.path.dirname(__file__), "..", "turma-b")
ST = ""
SHOW = "Record your audio mission and send it to me too! 🎙️"
def B(x): return f'<p class="big">{x}</p>'
def P(x): return f'<p>{x}</p>'
def intro(k, h, extra=""):
    return {"cls": "dark", "k": k, "h": h, "h1": True, "html":
            P("1. Listen to the words and repeat out loud.") + P("2. Play the 4 games.") +
            P("3. Do the audio mission and send your score. 📲") + extra +
            '<p class="tip">🔊 Turn on the sound of your phone.</p>'}
def mission(title, items, example=""):
    return {"cls": "accent", "k": "Audio mission 🎙️", "h": title, "html":
            P("Record a 1-minute audio on WhatsApp and send it to me.") + boxes([B(x) for x in items]) +
            (P("Example: " + example) if example else "")}
def final(txt): return {"cls": "dark", "k": "Final score", "h": "Well done! 🏆", "final": txt, "show": SHOW}

IRR = [("go", "went"), ("have", "had"), ("feel", "felt"), ("spend", "spent"), ("leave", "left"),
       ("read", "read"), ("sleep", "slept"), ("take", "took"), ("see", "saw"), ("do", "did")]
ED = [(w, snd, w) for w, snd in [("watched", "/t/"), ("stopped", "/t/"), ("worked", "/t/"), ("played", "/d/"), ("stayed", "/d/"),
      ("called", "/d/"), ("wanted", "/ɪd/"), ("visited", "/ɪd/"), ("decided", "/ɪd/")]]
PP = [("be", "been"), ("eat", "eaten"), ("see", "seen"), ("do", "done"), ("take", "taken"),
      ("try", "tried"), ("meet", "met"), ("lose", "lost"), ("ride", "ridden"), ("forget", "forgotten")]
FUT = [(a, b, a) for a, b in [("I'm going to study more.", "plan ✔"), ("I think it will rain.", "prediction 🔮"),
       ("I'll help you!", "decision now ⚡"), ("I'll call you later. I promise.", "promise 🤝")]]

def ed(word, sound):
    return {"t": f"<b>{word}</b>", "listen": word, "label": "Listen", "o": [sound] + [x for x in ("/t/", "/d/", "/ɪd/") if x != sound],
            "speak": word}

# =========================== AULA 1: 24/11 Past simple (detox) ===========================
d = "2026-11-24-past-simple"
page("How was your detox? (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "English class · Past Simple", "h": "How was your detox? 📵", "h1": True,
     "html": B("Telling stories about your week")},
    {"k": "Warm-up · 5 min", "h": "Your homework: the mini detox", "html": boxes([
        "<h3>Did you try the mini detox?</h3>", "<h3>What did you do instead of using your phone?</h3>",
        "<h3>How did you feel?</h3>", "<h3>Was it easy or hard? Why?</h3>"])},
    {"k": "Grammar · Regular verbs", "h": "Regular verbs: + ed", "html":
        '<table><tr><th>Verb</th><th>Past</th><th>Rule</th></tr>'
        '<tr><td>check</td><td><b>checked</b></td><td>+ ed</td></tr>'
        '<tr><td>use</td><td><b>used</b></td><td>+ d</td></tr>'
        '<tr><td>stop</td><td><b>stopped</b></td><td>double the consonant</td></tr>'
        '<tr><td>try</td><td><b>tried</b></td><td>consonant + y ➜ ied</td></tr>'
        '<tr><td>play</td><td><b>played</b></td><td>vowel + y ➜ yed</td></tr></table>'},
    {"cls": "dark", "k": "Irregular verbs", "h": "Irregular verbs: no rule, just practice!", "cards": IRR},
    {"k": "Exercise 1", "name": "Choose the past", "h": "Choose the past form",
     "qs": [{"t": "try", "o": ["tried", "tryed", "trid"]}, {"t": "stop", "o": ["stopped", "stoped", "stopt"]},
            {"t": "feel", "o": ["felt", "feeled", "fell"]}, {"t": "spend", "o": ["spent", "spended", "spend"]},
            {"t": "leave", "o": ["left", "leaved", "lived"]}, {"t": "play", "o": ["played", "plaid", "plaied"]},
            {"t": "sleep", "o": ["slept", "sleeped", "slep"]}, {"t": "read", "o": ["read", "readed", "red"]}]},
    {"cls": "dark", "k": "Negatives and questions", "h": "After DID / DIDN'T, use the base verb",
     "pre": wrong_right(["I didn't <b>used</b> my phone.", "Did you <b>felt</b> better?"],
                        ["I didn't <b>use</b> my phone.", "Did you <b>feel</b> better?"]),
     "html": B("Where <b>did</b> you <b>go</b>? ➜ I <b>went</b> to the park.")},
    {"k": "Exercise 2", "name": "Which is correct", "h": "Which sentence is correct?",
     "qs": [{"o": ["I didn't check Instagram.", "I didn't checked Instagram.", "I not checked Instagram."]},
            {"o": ["Did you sleep well?", "Did you slept well?", "You did sleep well?"]},
            {"o": ["What did you do on Sunday?", "What you did on Sunday?", "What did you did on Sunday?"]},
            {"o": ["She didn't go out.", "She didn't went out.", "She wasn't go out."]},
            {"o": ["How did you feel?", "How you felt?", "How did you felt?"]},
            {"o": ["We spent two hours outside.", "We spend two hours outside yesterday.", "We spended two hours outside."]}]},
    {"cls": "dark", "k": "Exercise 3", "name": "Detox story", "h": "Complete the story", "story": [
        "Last Saturday, I ", ["decided", "decide"], " to try a digital detox. I ", ["left", "leaved"],
        " my phone in my bedroom and I ", ["went", "goed"], " to the park. At first, I ", ["felt", "feeled"],
        " anxious, but then I ", ["read", "readed"], " a book and I ", ["didn't", "wasn't"],
        " think about Instagram. In the evening, I ", ["checked", "check"], " my phone: I ", ["had", "haved"],
        " 87 notifications!"]},
    {"k": "Speaking · 10 min", "h": "Tell me about your week", "html": P("Answer, then ask me the same questions!") + boxes([
        "<h3>What did you do last weekend?</h3>", "<h3>Where did you go?</h3>",
        "<h3>What time did you go to bed yesterday?</h3>", "<h3>What did you watch or read this week?</h3>"]) +
        P("Follow-up: Why? · How did you feel? · Who were you with?")},
    {"cls": "dark", "k": "Wrap-up", "h": "Today's summary 🎯", "html": boxes([
        "<h3>Regular</h3><p>checked, used, stopped, tried</p>",
        "<h3>Irregular</h3><p>went, felt, spent, left</p>",
        "<h3>Question / negative</h3><p>Did you go? · I didn't go.</p>"])},
], f"{R}/{d}/aula/index.html")

page("How was your detox? (homework)", ST, "tarefa:b:" + d, [
    intro("Homework · Past Simple", "Past Simple Training 📵"),
    {"k": "Listen and repeat", "h": "Irregular verbs", "cards": IRR},
    {"k": "Game 1", "name": "Past form", "h": "Choose the past form",
     "qs": [{"t": "go", "o": ["went", "goed", "gone"]}, {"t": "take", "o": ["took", "taked", "taken"]},
            {"t": "study", "o": ["studied", "studyed", "studed"]}, {"t": "see", "o": ["saw", "seed", "seen"]},
            {"t": "plan", "o": ["planned", "planed", "plant"]}, {"t": "do", "o": ["did", "done", "doed"]},
            {"t": "have", "o": ["had", "haved", "has"]}, {"t": "enjoy", "o": ["enjoyed", "enjoied", "enjoyd"]}]},
    {"cls": "dark", "k": "Game 2", "name": "Which is correct", "h": "Which sentence is correct?",
     "qs": [{"o": ["Did you watch the series?", "Did you watched the series?", "You watched the series did?"]},
            {"o": ["I didn't feel tired.", "I didn't felt tired.", "I wasn't feel tired."]},
            {"o": ["Where did you go?", "Where you went?", "Where did you went?"]},
            {"o": ["He didn't take his phone.", "He didn't took his phone.", "He not took his phone."]},
            {"o": ["What did you have for lunch?", "What did you had for lunch?", "What you had for lunch?"]},
            {"o": ["We didn't stay at home.", "We didn't stayed at home.", "We weren't stay at home."]}]},
    {"k": "Game 3 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "I left my phone at home.", "label": "1", "o": ["I left my phone at home.", "I lost my phone at home.", "I leave my phone at home."]},
            {"listen": "She spent the day outside.", "label": "2", "o": ["She spent the day outside.", "She spends the day outside.", "She sent the day outside."]},
            {"listen": "Did you sleep well?", "label": "3", "o": ["Did you sleep well?", "Do you sleep well?", "Did you speak well?"]},
            {"listen": "We didn't watch TV.", "label": "4", "o": ["We didn't watch TV.", "We don't watch TV.", "We didn't want TV."]},
            {"listen": "I felt relaxed.", "label": "5", "o": ["I felt relaxed.", "I feel relaxed.", "I fell relaxed."]},
            {"listen": "They went to the beach.", "label": "6", "o": ["They went to the beach.", "They want to the beach.", "They go to the beach."]}]},
    {"cls": "dark", "k": "Game 4", "name": "Make the question", "h": "Make the question",
     "tip": "Look at the answer. Which question is correct?",
     "qs": [{"t": "I went to the mall. ➜", "o": ["Where did you go?", "Where did you went?", "Where you went?"]},
            {"t": "I woke up at 10. ➜", "o": ["What time did you wake up?", "What time did you woke up?", "What time you woke up?"]},
            {"t": "I read a book. ➜", "o": ["What did you read?", "What did you readed?", "What you read did?"]},
            {"t": "I felt happy. ➜", "o": ["How did you feel?", "How did you felt?", "How you felt?"]},
            {"t": "I met my cousin. ➜", "o": ["Who did you meet?", "Who did you met?", "Who you met?"]},
            {"t": "Yes, I did. ➜", "o": ["Did you enjoy it?", "Did you enjoyed it?", "Do you enjoyed it?"]}]},
    mission("Your last weekend", ["5 things you did", "1 thing you didn't do", "How you felt"],
            "On Saturday I went to... I didn't use my phone in the morning... I felt..."),
    final("You can tell stories in the past now! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 2: 01/12 Travel stories ===========================
d = "2026-12-01-travel-stories"
page("Travel stories (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "English class · Past Simple", "h": "Travel stories ✈️", "h1": True,
     "html": B("was / were · ago · first, then... · the -ed sound")},
    {"k": "Warm-up · 5 min", "h": "Your audio mission", "html": boxes([
        "<h3>Tell me again: what did you do last weekend?</h3>", "<h3>Where was your last trip?</h3>",
        "<h3>Beach or mountains?</h3>", "<h3>Plane, bus or car?</h3>"])},
    {"k": "Grammar", "h": "was / were + time expressions", "html":
        '<table><tr><th></th><th>Past of be</th></tr><tr><td>I / he / she / it</td><td><b>was</b> / wasn\'t</td></tr>'
        '<tr><td>you / we / they</td><td><b>were</b> / weren\'t</td></tr></table>' +
        boxes([B("<b>last</b> summer / last year"), B("two years <b>ago</b>"), B("<b>in</b> 2023 / <b>in</b> July")]) +
        P("⚠️ Not: <s>in last year</s> · <s>ago two years</s>")},
    {"cls": "dark", "k": "Exercise 1", "name": "Time words", "h": "last, ago or in?",
     "qs": [{"t": "I went to Recife three years ___.", "o": ["ago", "last", "in"]},
            {"t": "We traveled ___ summer.", "o": ["last", "ago", "in"]},
            {"t": "My parents visited Natal ___ 2022.", "o": ["in", "last", "ago"]},
            {"t": "The trip ___ amazing!", "o": ["was", "were", "did"]},
            {"t": "The hotels ___ very expensive.", "o": ["were", "was", "did"]},
            {"t": "I ___ at home last weekend.", "o": ["wasn't", "weren't", "didn't"]}]},
    {"k": "Tell a story", "h": "Connect your story 🔗", "html": boxes([B("First, ..."), B("Then, ..."), B("After that, ..."), B("Finally, ...")]) +
        P("First, we took a bus. Then, we checked in at the hotel. After that, we went to the beach. Finally, we had dinner by the sea.")},
    {"cls": "dark", "k": "Pronunciation", "h": "The -ed sound 👂", "cards": ED, "html":
        P("<b>/t/</b> after p, k, s, sh, ch · <b>/d/</b> after most other sounds · <b>/ɪd/</b> after t or d (an extra syllable!)")},
    {"k": "Exercise 2 · Pronunciation", "name": "-ed sound", "h": "Which sound?", "tip": "Click 🔊, listen and choose the -ed sound.",
     "qs": [ed("talked", "/t/"), ed("needed", "/ɪd/"), ed("arrived", "/d/"), ed("walked", "/t/"),
            ed("started", "/ɪd/"), ed("traveled", "/d/")]},
    {"cls": "dark", "k": "Exercise 3", "name": "Trip story", "h": "Complete the story", "story": [
        "Two years ", ["ago", "last"], ", my friends and I ", ["went", "go"], " to Porto de Galinhas. ",
        ["First", "Finally"], ", we took a bus. The trip ", ["was", "were"], " long, but the views ", ["were", "was"],
        " beautiful. ", ["Then", "First"], ", we swam in the natural pools. I ", ["didn't", "wasn't"],
        " want to leave! ", ["Finally", "First"], ", we ", ["came", "comed"], " back home, tired but happy."]},
    {"cls": "accent", "k": "Speaking · 10 min", "h": "Your best trip 🗺️", "html": boxes([
        "<h3>Where did you go?</h3>", "<h3>When was it?</h3>", "<h3>Who did you go with?</h3>",
        "<h3>What did you do there?</h3>", "<h3>How was the food?</h3>", "<h3>Would you go back?</h3>"]) +
        P("Use First, Then, After that, Finally!")},
    {"cls": "dark", "k": "Game · 5 min", "h": "Two truths and a lie: trips ✈️", "html":
        P("Say 3 sentences about trips in your life. One is false. I will guess!") +
        B("Example: I went to São Paulo in 2019. I was on a plane for 12 hours once. I swam with dolphins.")},
    {"k": "Wrap-up", "h": "Today's summary 🎯", "html": boxes([
        "<h3>Time</h3><p>last summer · two years ago · in 2023</p>",
        "<h3>Story</h3><p>First, Then, After that, Finally</p>",
        "<h3>-ed</h3><p>/t/ watched · /d/ played · /ɪd/ wanted</p>"])},
], f"{R}/{d}/aula/index.html")

page("Travel stories (homework)", ST, "tarefa:b:" + d, [
    intro("Homework · Travel", "Travel Story Training ✈️"),
    {"k": "Listen and repeat", "h": "The -ed sound", "cards": ED},
    {"k": "Game 1 · Pronunciation", "name": "-ed sound", "h": "Which sound?", "tip": "Click 🔊, listen and choose the -ed sound.",
     "qs": [ed("looked", "/t/"), ed("ended", "/ɪd/"), ed("opened", "/d/"), ed("washed", "/t/"),
            ed("invited", "/ɪd/"), ed("enjoyed", "/d/")]},
    {"cls": "dark", "k": "Game 2", "name": "Time words", "h": "Choose the correct option",
     "qs": [{"t": "I visited my grandma two weeks ___.", "o": ["ago", "last", "in"]},
            {"t": "They traveled to Bahia ___ month.", "o": ["last", "ago", "in"]},
            {"t": "She was born ___ 2007.", "o": ["in", "last", "ago"]},
            {"t": "The beach ___ crowded.", "o": ["was", "were", "did"]},
            {"t": "We ___ tired after the trip.", "o": ["were", "was", "did"]},
            {"t": "The museums ___ open on Monday.", "o": ["weren't", "wasn't", "didn't"]}]},
    {"k": "Game 3", "name": "Story order", "h": "Choose the best word", "tip": "Think about the order of the story.",
     "qs": [{"t": "___, we packed our bags. (the start)", "o": ["First", "Finally", "After that"]},
            {"t": "We arrived at the airport. ___, we got on the plane.", "o": ["Then", "First", "Ago"]},
            {"t": "We checked in at the hotel. ___ that, we had lunch.", "o": ["After", "Then", "Finally"]},
            {"t": "___, after a great week, we came back home. (the end)", "o": ["Finally", "First", "Then"]},
            {"t": "I didn't like the food, ___ the hotel was great.", "o": ["but", "so", "because"]},
            {"t": "It was very hot, ___ we stayed in the pool all day.", "o": ["so", "but", "because"]}]},
    {"cls": "dark", "k": "Game 4 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "We traveled last summer.", "label": "1", "o": ["We traveled last summer.", "We travel every summer.", "We traveled last Sunday."]},
            {"listen": "The trip was amazing.", "label": "2", "o": ["The trip was amazing.", "The trip is amazing.", "The trips were amazing."]},
            {"listen": "I visited my aunt two years ago.", "label": "3", "o": ["I visited my aunt two years ago.", "I visit my aunt two years ago.", "I visited my aunt ten years ago."]},
            {"listen": "Then we walked to the beach.", "label": "4", "o": ["Then we walked to the beach.", "Then we worked at the beach.", "Then we wanted the beach."]},
            {"listen": "The hotels were expensive.", "label": "5", "o": ["The hotels were expensive.", "The hotel was expensive.", "The hotels weren't expensive."]},
            {"listen": "Finally, we decided to stay.", "label": "6", "o": ["Finally, we decided to stay.", "Finally, we decide to stay.", "First, we decided to stay."]}]},
    mission("Your best trip", ["Where and when", "Who with", "What you did (First, Then, After that, Finally)", "How it was"],
            "Two years ago, I went to... First, we... Then... It was..."),
    final("Great travel stories! Your past simple is getting stronger! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 3: 08/12 Have you ever...? ===========================
d = "2026-12-08-have-you-ever"
page("Have you ever...? (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "English class · Present Perfect", "h": "Have you ever...? 🌍", "h1": True,
     "html": B("Life experiences: present perfect × past simple")},
    {"k": "Warm-up · 5 min", "h": "Your trip audio", "html": boxes([
        "<h3>Tell me about your best trip in 3 sentences.</h3>", "<h3>Where do you want to go one day?</h3>",
        "<h3>What is the most interesting place you know?</h3>"])},
    {"k": "Grammar", "h": "have / has + past participle", "html":
        boxes([B("I <b>have been</b> to Recife."), B("She <b>has eaten</b> sushi."), B("I <b>have never</b> flown.")]) +
        boxes([B("<b>Have</b> you <b>ever</b> tried tapioca?") + P("✅ Yes, I have. · ❌ No, I haven't. / No, never.")]) +
        P("We use it for <b>experiences in your life</b>, when the time is not important.")},
    {"cls": "dark", "k": "Past participles", "h": "Verb ➜ participle", "cards": PP},
    {"k": "Exercise 1", "name": "Participle", "h": "Choose the participle",
     "qs": [{"t": "Have you ever ___ a famous person? (meet)", "o": ["met", "meeted", "meet"]},
            {"t": "I have never ___ a horse. (ride)", "o": ["ridden", "rode", "rided"]},
            {"t": "She has ___ to Argentina. (be)", "o": ["been", "was", "be"]},
            {"t": "Have you ever ___ your phone? (lose)", "o": ["lost", "losed", "lose"]},
            {"t": "We have ___ that movie three times. (see)", "o": ["seen", "saw", "seed"]},
            {"t": "He has never ___ Japanese food. (eat)", "o": ["eaten", "ate", "eated"]}]},
    {"cls": "dark", "k": "The big rule", "h": "Finished time ➜ past simple", "pre":
        wrong_right(["I <b>have been</b> to Recife <b>last year</b>."], ["I <b>went</b> to Recife <b>last year</b>."]),
     "html": B("Have you ever been to Recife? ➜ Yes, I have! ➜ When <b>did</b> you <b>go</b>? ➜ I <b>went</b> in 2023.") +
        P("yesterday · last year · in 2023 · two days ago ➜ <b>past simple</b>")},
    {"k": "Exercise 2", "name": "Perfect or past", "h": "Present perfect or past simple?",
     "qs": [{"o": ["I have tried sushi.", "I have tried sushi last week."]},
            {"o": ["She went to Rio in 2020.", "She has gone to Rio in 2020."]},
            {"o": ["Have you ever lost your phone?", "Did you ever lost your phone?"]},
            {"o": ["We saw a great movie yesterday.", "We have seen a great movie yesterday."]},
            {"o": ["I have never been on a plane.", "I never was on a plane."]},
            {"o": ["When did you meet your best friend?", "When have you met your best friend?"]}]},
    {"cls": "dark", "k": "Exercise 3", "name": "Short answers", "h": "Answer correctly",
     "qs": [{"t": "Have you ever eaten açaí? ✅", "o": ["Yes, I have.", "Yes, I did.", "Yes, I ate."]},
            {"t": "Has she ever been to Europe? ❌", "o": ["No, she hasn't.", "No, she didn't.", "No, she haven't."]},
            {"t": "Did you go out last night? ✅", "o": ["Yes, I did.", "Yes, I have.", "Yes, I went did."]},
            {"t": "Have they ever met your family? ❌", "o": ["No, they haven't.", "No, they hasn't.", "No, they didn't met."]},
            {"t": "Have you ever tried a digital detox? ✅", "o": ["Yes, I have.", "Yes, I has.", "Yes, I tried have."]}]},
    {"cls": "accent", "k": "Speaking · 10 min", "h": "Have you ever...? 🎤", "html":
        P("Ask me, then I ask you. If the answer is YES, ask a follow-up in the past: When? Where? How was it?") + boxes([
        B("...been on a plane?"), B("...stayed up all night?"), B("...met a famous person?"),
        B("...lost something important?"), B("...cooked for a lot of people?"), B("...ridden a horse?")])},
    {"cls": "dark", "k": "Game · 5 min", "h": "True or false? 🕵️", "html":
        P("Say 3 sentences with <b>I have...</b> or <b>I have never...</b>. One is false. Can I guess?") +
        B("I have never eaten pizza. I have been to 5 states. I have ridden a camel.")},
    {"k": "Wrap-up", "h": "Today's summary 🎯", "html": boxes([
        "<h3>Experience</h3><p>Have you ever been...? Yes, I have.</p>",
        "<h3>Finished time</h3><p>When did you go? I went in 2023.</p>",
        "<h3>Participles</h3><p>been, eaten, seen, met, lost</p>"])},
], f"{R}/{d}/aula/index.html")

page("Have you ever...? (homework)", ST, "tarefa:b:" + d, [
    intro("Homework · Present Perfect", "Life Experiences Training 🌍"),
    {"k": "Listen and repeat", "h": "Past participles", "cards": PP},
    {"k": "Game 1", "name": "Participle", "h": "Choose the participle",
     "qs": [{"t": "take", "o": ["taken", "took", "taked"]}, {"t": "do", "o": ["done", "did", "doed"]},
            {"t": "forget", "o": ["forgotten", "forgot", "forgetted"]}, {"t": "see", "o": ["seen", "saw", "seed"]},
            {"t": "be", "o": ["been", "was", "being"]}, {"t": "try", "o": ["tried", "tryed", "trid"]},
            {"t": "eat", "o": ["eaten", "ate", "eated"]}, {"t": "meet", "o": ["met", "meeted", "meat"]}]},
    {"cls": "dark", "k": "Game 2", "name": "Perfect or past", "h": "Which sentence is correct?",
     "qs": [{"o": ["I have been to Salvador.", "I have been to Salvador in 2021."]},
            {"o": ["He lost his wallet yesterday.", "He has lost his wallet yesterday."]},
            {"o": ["Have you ever ridden a bike?", "Did you ever ridden a bike?"]},
            {"o": ["We met two years ago.", "We have met two years ago."]},
            {"o": ["She has never seen snow.", "She has never saw snow."]},
            {"o": ["What did you do last night?", "What have you done last night?"]}]},
    {"k": "Game 3", "name": "Short answers", "h": "Answer correctly",
     "qs": [{"t": "Have you ever been to a concert? ✅", "o": ["Yes, I have.", "Yes, I did.", "Yes, I was."]},
            {"t": "Has he ever cooked dinner? ❌", "o": ["No, he hasn't.", "No, he haven't.", "No, he didn't."]},
            {"t": "Did you sleep well last night? ✅", "o": ["Yes, I did.", "Yes, I have.", "Yes, I slept did."]},
            {"t": "Have you ever forgotten a birthday? ❌", "o": ["No, I haven't.", "No, I didn't.", "No, I hasn't."]},
            {"t": "Have they ever tried tapioca? ✅", "o": ["Yes, they have.", "Yes, they has.", "Yes, they did tried."]}]},
    {"cls": "dark", "k": "Game 4 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "Have you ever been to Recife?", "label": "1", "o": ["Have you ever been to Recife?", "Have you ever gone to Recife?", "Did you ever go to Recife?"]},
            {"listen": "I have never eaten sushi.", "label": "2", "o": ["I have never eaten sushi.", "I have never eaten soup.", "I had never eaten sushi."]},
            {"listen": "She has lost her keys.", "label": "3", "o": ["She has lost her keys.", "She lost her keys.", "She has lost her kids."]},
            {"listen": "We went there last year.", "label": "4", "o": ["We went there last year.", "We have been there last year.", "We want there last year."]},
            {"listen": "No, I haven't.", "label": "5", "o": ["No, I haven't.", "No, I didn't.", "No, I hadn't."]},
            {"listen": "When did you meet her?", "label": "6", "o": ["When did you meet her?", "When did you miss her?", "Where did you meet her?"]}]},
    mission("Your life experiences", ["3 things you have done", "3 things you have never done", "For 1 of them: When? How was it?"],
            "I have been to Salvador. I went there in 2022 and it was... I have never ridden a horse."),
    final("Amazing! Now you can talk about your life experiences! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 4: 15/12 Plans and goals ===========================
d = "2026-12-15-plans-goals"
page("Plans and goals (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "English class · Future", "h": "Plans and goals 🎯", "h1": True,
     "html": B("going to × will")},
    {"k": "Warm-up · 5 min", "h": "Your experiences audio", "html": boxes([
        "<h3>Tell me one thing you have never done.</h3>", "<h3>Is there something you want to try one day?</h3>",
        "<h3>What are you going to do this weekend?</h3>"])},
    {"k": "Grammar", "h": "going to or will?", "cards": FUT, "html":
        boxes([B("<b>going to</b> = a plan you already decided"), B("<b>will</b> = a decision NOW, a prediction or a promise")])},
    {"cls": "dark", "k": "Form", "h": "Be careful with the form!", "pre":
        wrong_right(["I <b>going to</b> travel.", "I <b>will to</b> study.", "She <b>wills</b> help."],
                    ["I<b>'m going to</b> travel.", "I <b>will</b> study.", "She <b>will</b> help."]),
     "html": B("Negative: I'm <b>not</b> going to... · I <b>won't</b>...")},
    {"k": "Exercise 1", "name": "going to or will", "h": "going to or will?",
     "qs": [{"t": "I bought the tickets. I ___ visit my aunt in January.", "o": ["am going to", "will"]},
            {"t": "The phone is ringing! I ___ answer it.", "o": ["'ll", "am going to"]},
            {"t": "Look at those clouds! It ___ rain.", "o": ["is going to", "will"]},
            {"t": "Don't worry, I ___ tell anyone. I promise!", "o": ["won't", "am not going to"]},
            {"t": "I think people ___ use phones less in the future.", "o": ["will", "are going to"]},
            {"t": "We ___ start a gym next month. We already paid!", "o": ["are going to", "will"]}]},
    {"cls": "dark", "k": "Exercise 2", "name": "Which is correct", "h": "Which sentence is correct?",
     "qs": [{"o": ["I'm going to study every day.", "I going to study every day.", "I'm going study every day."]},
            {"o": ["She will travel next year.", "She will to travel next year.", "She wills travel next year."]},
            {"o": ["Are you going to work tomorrow?", "You are going to work tomorrow?", "Do you going to work tomorrow?"]},
            {"o": ["I won't use my phone at dinner.", "I willn't use my phone at dinner.", "I won't to use my phone at dinner."]},
            {"o": ["What are you going to do?", "What you are going to do?", "What are you going do?"]}]},
    {"k": "Exercise 3", "name": "Dialogue", "h": "Complete the conversation", "story": [
        "Ana: What ", ["are", "do"], " you going to do on vacation? ",
        "Bia: I'm going ", ["to", "for"], " visit my grandparents. And you? ",
        "Ana: I don't know. Maybe I ", ["will", "am going to"], " stay home. ",
        "Bia: Come with me! My grandma ", ["will", "wills"], " love you! ",
        "Ana: Really? OK, I'll ", ["ask", "to ask"], " my parents tonight!"]},
    {"cls": "accent", "k": "Speaking · 10 min", "h": "Your vacation and your goals 🗓️", "html": boxes([
        "<h3>What are you going to do on vacation?</h3>", "<h3>What are your goals for 2027?</h3>",
        "<h3>What will be different in your life in 5 years?</h3>", "<h3>Which habit are you going to change?</h3>"]) +
        P("Use: I'm going to... · I think I'll... · I'm not going to... · I won't...")},
    {"cls": "dark", "k": "Game · 5 min", "h": "Predict the future 🔮", "html":
        P("Agree or disagree? Explain why.") + boxes([B("In 2050, people will work only 4 days a week."),
        B("Phones will disappear."), B("Everyone will speak English.")])},
    {"k": "Wrap-up", "h": "Today's summary 🎯", "html": boxes([
        "<h3>going to</h3><p>plans: I'm going to travel.</p>",
        "<h3>will</h3><p>now / prediction / promise: I'll help you.</p>",
        "<h3>Negative</h3><p>I'm not going to · I won't</p>"])},
], f"{R}/{d}/aula/index.html")

page("Plans and goals (homework)", ST, "tarefa:b:" + d, [
    intro("Homework · Future", "Future Training 🎯"),
    {"k": "Listen and repeat", "h": "going to × will", "cards": FUT + [("I'm not going to stop.", "negative plan", "I'm not going to stop."), ("I won't forget.", "negative promise", "I won't forget.")]},
    {"k": "Game 1", "name": "going to or will", "h": "going to or will?",
     "qs": [{"t": "I already decided: I ___ learn to drive next year.", "o": ["am going to", "will"]},
            {"t": "A: I'm thirsty. B: I ___ get you some water.", "o": ["'ll", "am going to"]},
            {"t": "She is very tired. She ___ sleep early tonight. (her plan)", "o": ["is going to", "will"]},
            {"t": "I think Brazil ___ win the next World Cup.", "o": ["will", "is going to"]},
            {"t": "Thanks for the money! I ___ pay you back, I promise.", "o": ["'ll", "am going to"]},
            {"t": "They have the tickets. They ___ see the concert on Friday.", "o": ["are going to", "will"]}]},
    {"cls": "dark", "k": "Game 2", "name": "Which is correct", "h": "Which sentence is correct?",
     "qs": [{"o": ["We're going to move in March.", "We going to move in March.", "We're going move in March."]},
            {"o": ["It will be a great year.", "It will to be a great year.", "It wills be a great year."]},
            {"o": ["Is he going to call you?", "He is going to call you?", "Does he going to call you?"]},
            {"o": ["I won't be late.", "I willn't be late.", "I won't to be late."]},
            {"o": ["Where are you going to stay?", "Where you are going to stay?", "Where are you going stay?"]},
            {"o": ["I'm not going to buy it.", "I not going to buy it.", "I'm no going to buy it."]}]},
    {"k": "Game 3", "name": "Complete", "h": "Complete the sentence",
     "qs": [{"t": "My goal for 2027: I'm going to ___ more English.", "o": ["practice", "practicing", "to practice"]},
            {"t": "Don't worry! I ___ forget your birthday.", "o": ["won't", "don't", "am not"]},
            {"t": "What ___ you going to do tomorrow?", "o": ["are", "do", "will"]},
            {"t": "I think it ___ be sunny tomorrow.", "o": ["will", "is", "going"]},
            {"t": "She ___ going to start a new course.", "o": ["is", "will", "does"]},
            {"t": "I'll ___ you later!", "o": ["call", "to call", "calling"]}]},
    {"cls": "dark", "k": "Game 4 · Listen 🎧", "name": "Listen", "h": "Listen and choose", "tip": "Click 🔊, then choose the sentence you heard.",
     "qs": [{"listen": "I'm going to study more.", "label": "1", "o": ["I'm going to study more.", "I'm going to stay more.", "I was going to study more."]},
            {"listen": "I'll call you later.", "label": "2", "o": ["I'll call you later.", "I call you later.", "I'll tell you later."]},
            {"listen": "It's going to rain.", "label": "3", "o": ["It's going to rain.", "It's going to be fine.", "It was going to rain."]},
            {"listen": "I won't forget.", "label": "4", "o": ["I won't forget.", "I want to forget.", "I don't forget."]},
            {"listen": "Are you going to travel?", "label": "5", "o": ["Are you going to travel?", "Are you going to train?", "Did you travel?"]},
            {"listen": "We'll see.", "label": "6", "o": ["We'll see.", "We see.", "Will she?"]}]},
    mission("Your goals for 2027", ["3 things you're going to do", "1 thing you're not going to do", "1 prediction: I think I'll..."],
            "In 2027, I'm going to... I'm not going to... I think I'll..."),
    final("Great! You know how to talk about the future now! 💪"),
], f"{R}/{d}/index.html")

# =========================== AULA 5: 22/12 Final review + vacation ===========================
d = "2026-12-22-final-review"
page("Season Finale (aula)", ST, "aula:b:" + d, [
    {"cls": "dark", "k": "Last class of the year", "h": "Season Finale 🎬", "h1": True, "html": B("Review game + certificate")},
    {"k": "How it works", "h": "5 rounds. Let's see your score! 🏆", "html": boxes([
        B("1 · Past forms"), B("2 · Experiences"), B("3 · The future"), B("4 · Fix the mistake"), B("5 · Story")])},
    {"cls": "dark", "k": "Round 1", "name": "Past forms", "h": "Past forms",
     "qs": [{"t": "leave", "o": ["left", "leaved", "lived"]}, {"t": "try", "o": ["tried", "tryed", "trid"]},
            {"t": "spend", "o": ["spent", "spended", "spend"]}, {"t": "feel", "o": ["felt", "feeled", "fell"]},
            {"t": "stop", "o": ["stopped", "stoped", "stopt"]}, {"t": "take", "o": ["took", "taked", "taken"]}]},
    {"k": "Round 2", "name": "Experiences", "h": "Present perfect or past simple?",
     "qs": [{"o": ["Have you ever been to Bahia?", "Did you ever been to Bahia?"]},
            {"o": ["I went there in 2022.", "I have been there in 2022."]},
            {"t": "Have you ever met a famous person? ❌", "o": ["No, I haven't.", "No, I didn't.", "No, I hasn't."]},
            {"o": ["She has never seen snow.", "She has never saw snow."]},
            {"o": ["When did you start English?", "When have you started English?"]}]},
    {"cls": "dark", "k": "Round 3", "name": "Future", "h": "going to or will?",
     "qs": [{"t": "I bought a new book. I ___ read it on vacation.", "o": ["am going to", "will"]},
            {"t": "A: It's cold! B: I ___ close the window.", "o": ["'ll", "am going to"]},
            {"o": ["I won't stop studying.", "I willn't stop studying."]},
            {"o": ["What are you going to do?", "What you are going to do?"]},
            {"t": "I think 2027 ___ be a great year!", "o": ["will", "is"]}]},
    {"k": "Round 4", "name": "Fix the mistake", "h": "Fix the mistake 🔧", "tip": "Review from Social Media and Digital Detox!",
     "qs": [{"o": ["She uses Instagram every day.", "She use Instagram every day."]},
            {"o": ["How often do you check it?", "How often you check it?"]},
            {"o": ["You should sleep more.", "You should to sleep more."]},
            {"o": ["I spend too much time on my phone.", "I spend too many time on my phone."]},
            {"o": ["I use my phone for messaging friends.", "I use my phone for message friends."]},
            {"o": ["Social media is part of my life.", "Social media are part of my life."]}]},
    {"cls": "dark", "k": "Round 5", "name": "Story", "h": "My year in English", "story": [
        "This year, I ", ["studied", "studyed"], " a lot of English. I ", ["learned", "learn"],
        " to talk about my habits and I ", ["tried", "tryed"], " a digital detox. I ", ["have", "has"],
        " never spoken so much English! Next year, I'm ", ["going", "go"], " to practice even more. I'm sure I ",
        ["will", "am"], " get to B1!"]},
    {"k": "Final score", "h": "What a season! 🏆", "final": "You worked really hard this year. Congratulations!", "send": False, "show": ""},
    {"cls": "accent", "k": "Certificate time 🎓", "h": "Congratulations!", "html": B("You finished the year! 🎉") + P("Your certificate is here!")},
    {"cls": "dark", "k": "Vacation challenge", "h": "Your vacation mission 🏖️", "html": boxes([
        B("1 round per week"), B("10 minutes"), B("1 short audio per week")]) + P("Keep your English alive on vacation! See you in February! 💙")},
], f"{R}/{d}/aula/index.html")

def wk(n, qs, cls="", tip=""):
    return {"cls": cls, "k": f"Week {n}", "name": f"Week {n}", "h": f"Week {n} challenge",
            "tip": (tip + " " if tip else "") + f"Play this round in week {n}.", "qs": qs}

page("Vacation Challenge", ST, "tarefa:b:" + d, [
    {"cls": "dark", "k": "Vacation · 2026/2027", "h": "Vacation Challenge 🏖️", "h1": True, "html":
        P("Your mission: 1 round per week. It takes 10 minutes!") +
        P("Every week, also send me a 1-minute audio answering the question of the week. 🎙️") +
        P("At the end, send your score to the teacher. 📲") + '<p class="tip">🔊 Turn on the sound of your phone.</p>'},
    {"k": "Audio questions", "h": "One question per week 🎙️", "html": boxes([
        "<h3>Week 1</h3><p>What did you do last week?</p>", "<h3>Week 2</h3><p>What is the best place you have ever visited?</p>",
        "<h3>Week 3</h3><p>What are you going to do next weekend?</p>", "<h3>Week 4</h3><p>Describe your daily routine on vacation.</p>",
        "<h3>Week 5</h3><p>Give advice to someone who wants to learn English.</p>", "<h3>Week 6</h3><p>What are your goals for this year?</p>"])},
    wk(1, [{"t": "go", "o": ["went", "goed", "gone"]}, {"t": "study", "o": ["studied", "studyed", "studed"]},
           {"t": "have", "o": ["had", "haved", "has"]}, {"t": "leave", "o": ["left", "leaved", "lived"]},
           {"t": "plan", "o": ["planned", "planed", "plant"]}, {"t": "see", "o": ["saw", "seed", "seen"]}]),
    wk(2, [ed("watched", "/t/"), ed("wanted", "/ɪd/"), ed("played", "/d/"), ed("helped", "/t/"),
           ed("needed", "/ɪd/"), ed("called", "/d/")], "dark", "Click 🔊 and choose the -ed sound."),
    wk(3, [{"o": ["Have you ever been to Pipa?", "Did you ever been to Pipa?"]},
           {"o": ["We met last year.", "We have met last year."]},
           {"t": "Have you ever lost your phone? ✅", "o": ["Yes, I have.", "Yes, I did.", "Yes, I has."]},
           {"t": "eat ➜ participle", "o": ["eaten", "ate", "eated"]},
           {"t": "be ➜ participle", "o": ["been", "was", "being"]},
           {"o": ["She has never tried açaí.", "She has never try açaí."]}]),
    wk(4, [{"t": "I have the tickets. I ___ travel in March.", "o": ["am going to", "will"]},
           {"t": "A: I forgot my pen. B: I ___ lend you mine.", "o": ["'ll", "am going to"]},
           {"o": ["I won't give up.", "I willn't give up."]},
           {"o": ["Are you going to study today?", "You are going to study today?"]},
           {"t": "I think it ___ be a good year.", "o": ["will", "is"]},
           {"o": ["She's going to start a course.", "She going to start a course."]}], "dark"),
    wk(5, [{"o": ["You should drink more water.", "You should to drink more water."]},
           {"o": ["She checks her phone a lot.", "She check her phone a lot."]},
           {"o": ["How often do you go out?", "How often you go out?"]},
           {"o": ["I have too many apps.", "I have too much apps."]},
           {"o": ["I'm not old enough to drive.", "I'm not enough old to drive."]},
           {"o": ["Social media is useful.", "Social media are useful."]}]),
    {"cls": "dark", "k": "Week 6", "name": "Week 6", "h": "Week 6: my vacation story", "story": [
        "My vacation ", ["was", "were"], " great! I ", ["slept", "sleeped"], " a lot and I ", ["spent", "spended"],
        " time with my family. I ", ["have", "has"], " never read so many books! Next month, I'm going ", ["to", "for"],
        " start my classes again, and I ", ["will", "am"], " work hard!"]},
    final("You kept your English alive on vacation! See you in February! 💙"),
], f"{R}/{d}/index.html")
print("ok")
