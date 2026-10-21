# HTML rebuilds of the Rally prototype screens (sharp at any size).
# Every size is in em; the phone sets font-size from its own width (cqw), so screens scale as one unit.

IC = {
 'spark': '<svg viewBox="0 0 24 24"><path d="M12 2c.6 4.7 2.6 7.6 8 10-5.4 2.4-7.4 5.3-8 10-.6-4.7-2.6-7.6-8-10 5.4-2.4 7.4-5.3 8-10z"/></svg>',
 'steps': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="8" cy="15" rx="2.6" ry="4" transform="rotate(-18 8 15)"/><ellipse cx="16" cy="8" rx="2.6" ry="4" transform="rotate(18 16 8)"/></svg>',
 'waves': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 10c2-2 4-2 6 0s4 2 6 0 4-2 6 0M3 15c2-2 4-2 6 0s4 2 6 0 4-2 6 0"/></svg>',
 'home': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M4 11 12 4l8 7v9h-5v-5H9v5H4z"/></svg>',
 'people': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="9" cy="8" r="3"/><path d="M3 19c0-3.3 2.7-5 6-5s6 1.7 6 5"/><circle cx="17" cy="9" r="2.4"/><path d="M17 14c2.4 0 4 1.6 4 4.5"/></svg>',
 'journal': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><rect x="5" y="3.5" width="14" height="17" rx="2"/><path d="M9 8h6M9 12h6"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 'back': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M15 5l-7 7 7 7"/></svg>',
 'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M5 18.5V6.8A2.8 2.8 0 0 1 7.8 4h8.4A2.8 2.8 0 0 1 19 6.8v6.4a2.8 2.8 0 0 1-2.8 2.8H9z"/></svg>',
}
def ic(n, cls=''): return '<span class="pi %s">%s</span>' % (cls, IC[n])

STATUS = ('<div class="ps-status"><span>9:41</span><span class="ps-sig"><i></i><i></i><i></i><i></i>'
          '<b class="ps-bat"></b></span></div>')

def tabbar(dim=False):
    return ('<div class="ps-tabs%s"><span class="on">%s<em>The Rally</em></span><span>%s<em>Huddles</em></span><span>%s<em>Journal</em></span></div>'
            % (' dim' if dim else '', ic('home'), ic('people'), ic('journal')))

def phone(inner, label, crop=None, cls=''):
    style = ' style="--crop:%s"' % crop if crop else ''
    return ('<div class="ph%s%s" role="img" aria-label="%s"%s><div class="ph-scr">%s%s</div><span class="ph-notch"></span></div>'
            % (' crop' if crop else '', (' ' + cls) if cls else '', label, style, STATUS, inner))

HOME = ('<div class="ps-pad"><p class="ps-eye">Good morning</p><div class="ps-hi"><p class="ps-h1">Hi, Jordan</p><span class="ps-av">J</span></div>'
  '<div class="ps-check"><p class="ps-q">How are you feeling today?</p><div class="ps-chips">'
  '<span><b class="d y"></b>Energized</span><span><b class="d b"></b>Balanced</span><span><b class="d g"></b>Need a reset</span><span><b class="d o"></b>Taking it easy</span></div>'
  '<span class="ps-btn">Submit</span></div>'
  '<div class="ps-modes"><span class="m1">%s<em>Start</em></span><span class="m2">%s<em>Move</em></span><span class="m3">%s<em>Restore</em></span></div>'
  '<div class="ps-feat"><span class="ps-feat-ic">%s</span><p class="ps-eye lt">Featured for your desk-heavy day</p><p class="ps-feat-t">Desk Reset Flow</p>'
  '<p class="ps-feat-s">Eight minutes to unwind your shoulders and reset your posture.</p></div></div>'
  % (ic('spark','c-or'), ic('steps','c-bl'), ic('waves','c-rd'), IC['steps'])) + tabbar()

WELCOME = ('<div class="ps-hero or"><span class="ps-hero-spark">%s</span></div><div class="ps-pad"><div class="ps-dash"><i class="on"></i><i></i><i></i><i></i><i></i><i></i></div>'
  '<div class="ps-low"><p class="ps-eye">Welcome to Rally</p><p class="ps-big">Find movement in your everyday moments.</p><span class="ps-btn">Get started</span></div></div>'
  % IC['spark'])

MOVE = ('<div class="ps-pad"><div class="ps-top"><p class="ps-eye dk">Move · Desk Reset Flow</p><span class="ps-x">%s</span></div>'
  '<div class="ps-orb"><span>%s</span></div><p class="ps-mid">Let’s take a movement break together.</p><p class="ps-time">7:59</p>'
  '<p class="ps-pace">Move at whatever pace feels good today.</p><div class="ps-dots"><i class="on"></i><i></i><i></i><i></i></div>'
  '<span class="ps-btn rd">End session</span></div>' % (IC['x'], IC['steps']))

REFLECT = ('<div class="ps-hero bl"><span class="ps-hero-orb">%s</span></div><div class="ps-pad tight"><p class="ps-eye">Rally complete</p>'
  '<p class="ps-h2">Nice work, Jordan. You made time for yourself.</p><p class="ps-q">How did that feel?</p>'
  '<div class="ps-chips sm"><span><b class="d y"></b>Energized</span><span><b class="d g"></b>Calm</span><span><b class="d b"></b>Good</span><span><b class="d m"></b>Meh</span></div>'
  '<p class="ps-q">Rate it <em>(optional)</em></p><div class="ps-chips sm"><span>Relaxing</span><span>Energizing</span><span>Grounding</span><span>Refreshing</span><span>Peaceful</span><span>Tough</span></div>'
  '<p class="ps-q">What stood out? <em>(optional)</em></p><div class="ps-input">Anything you want to remember…</div><p class="ps-q">Want more like this?</p></div>' % IC['steps'])

WHATIS = ('<div class="ps-pad"><div class="ps-dash two"><i class="on"></i><i class="on"></i><i></i><i></i><i></i><i></i></div><p class="ps-eye">Good to know</p>'
  '<p class="ps-h2">What is a Rally?</p><p class="ps-sub">One intentional movement moment. It doesn’t have to be a workout.</p>'
  '<div class="ps-grid"><span>%s Taking the stairs</span><span>%s Parking farther away</span><span>%s Walking during lunch</span><span>%s Stretching between meetings</span>'
  '<span>%s Standing for three minutes</span><span>%s A quick mobility break</span></div>'
  '<p class="ps-foot">Small moments become lasting habits — even more meaningful when you’re moving together.</p></div>'
  % tuple(ic(n,'c-or') for n in ('steps','steps','steps','waves','spark','waves')))

HUDDLE = ('<div class="ps-pad"><div class="ps-top"><span class="ps-x or">%s</span><p class="ps-h3">Lunch Break Huddle</p><span class="ps-x or">%s</span></div>'
  '<div class="ps-goal"><p class="ps-eye lt">4 members · Goal</p><p class="ps-goal-t">Complete 5 movement breaks this week</p><span class="ps-goal-pill">3 of 5 movement breaks this week</span></div>'
  '<p class="ps-q">Scoreboard</p><div class="ps-score"><div><span class="ps-avs"><i></i><i></i><i></i></span><b>7</b><em>Breakfast Yoga</em></div><span class="vs">vs</span>'
  '<div><span class="ps-avs bl"><i></i><i></i><i></i></span><b class="bl">5</b><em>Desk Breakers</em></div></div><span class="ps-prog"><i></i></span></div>'
  % (IC['back'], IC['chat']))

def wf(inner, label, crop=None):
    style = ' style="--crop:%s"' % crop if crop else ''
    return '<div class="ph wf" role="img" aria-label="%s"%s><div class="ph-scr">%s%s</div><span class="ph-notch"></span></div>' % (label, style, STATUS, inner)
XBOX = '<span class="wf-img"><svg viewBox="0 0 100 60" preserveAspectRatio="none"><path d="M0 0 100 60M100 0 0 60" stroke="#9a9a9a" stroke-width="1" vector-effect="non-scaling-stroke"/></svg></span>'
WF_FEED = ('<div class="ps-pad"><div class="wf-tabs"><span>‹</span><span class="on">Discover</span><span>Achievements</span></div>'
  '<div class="wf-post"><p class="wf-t">Breakfast Yoga</p><p class="wf-s">Posted 1 hr</p>%s<span class="wf-l"></span><span class="wf-l wf-short"></span></div>'
  '<div class="wf-post"><p class="wf-t">Pause Soccer Moms</p><p class="wf-s">Jan 15</p>%s<span class="wf-l"></span></div></div>' % (XBOX, XBOX))
WF_SETUP = ('<div class="ps-pad"><p class="wf-head">Move Now</p><p class="wf-q">How much time do you have?</p><span class="wf-field"></span>'
  '<p class="wf-q">What activity level do you desire?</p><span class="wf-slider"><i></i></span><p class="wf-q">What areas do you want to target?</p>'
  '<svg class="wf-fig" viewBox="0 0 60 60" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><circle cx="36" cy="9" r="5"/><path d="M33 16 26 32l10 6v14M26 32 16 46M30 22l12 6 8-6M30 22 18 26 12 20"/></svg></div>')

SCREENS = {
 'flow1': phone(HOME, 'Home screen with the How are you feeling today check-in'),
 'flow2': phone(WELCOME, 'Daily Rally screen inviting the user to find movement in everyday moments'),
 'flow3': phone(MOVE, 'In-progress movement break with a timer'),
 'flow4': phone(REFLECT, 'Rally complete screen asking how it felt'),
 'before': phone(HOME, 'Before: home screen with no explanation of what a Rally is', crop='1.79'),
 'after': phone(WHATIS, 'After: onboarding screen titled What is a Rally? with everyday examples', crop='1.59'),
 'home': phone(HOME, 'Prototype home screen with a one-question mood check-in', crop='1.25'),
 'huddle': phone(HUDDLE, 'Prototype Huddle screen with a shared goal and scoreboard', crop='1.37'),
 'wf_feed': wf(WF_FEED, 'Early wireframe of a public social feed'),
 'wf_setup': wf(WF_SETUP, 'Early wireframe of a three-question setup'),
}

CSS = '''
/* Rally prototype screens rebuilt in HTML (all sizes in em, scaled by the phone width) */
.ph{position:relative;container-type:inline-size;width:100%;max-width:100%;aspect-ratio:194/418;flex:none}
.ph.crop{aspect-ratio:1/var(--crop)}
.ph-scr{position:absolute;inset:0;background:#F7EFE7;border:3.4cqw solid #1B1513;border-radius:15cqw;overflow:hidden;font-family:'Work Sans','Helvetica Neue',Arial,sans-serif;font-size:5.7cqw;line-height:1.25;color:#2A211C;display:flex;flex-direction:column}
.ph.crop .ps-tabs{display:none}
.ph.crop .ps-pad{flex:none}
.ph.crop .ps-feat{flex:none;min-height:8.5em;padding-bottom:1em}
.ph.crop .ph-scr{border-bottom:0;border-bottom-left-radius:0;border-bottom-right-radius:0}
.ph-notch{position:absolute;top:2.6cqw;left:33%;width:34%;height:6.4cqw;border-radius:9cqw;background:#1B1513}
.ph p{margin:0}
.ps-status{display:flex;justify-content:space-between;align-items:center;padding:4.2cqw 8cqw 0 9cqw;font-size:.78em;font-weight:600;height:9cqw;flex:none;position:relative;z-index:2}
.ps-sig{display:flex;align-items:flex-end;gap:.12em}.ps-sig i{display:block;width:.22em;background:currentColor;border-radius:.05em}
.ps-sig i:nth-child(1){height:.3em}.ps-sig i:nth-child(2){height:.45em}.ps-sig i:nth-child(3){height:.6em}.ps-sig i:nth-child(4){height:.75em}
.ps-bat{display:block;width:1.3em;height:.62em;border-radius:.18em;background:currentColor;margin-left:.3em}
.ps-pad{padding:2.5cqw 7cqw 0;display:flex;flex-direction:column;gap:.55em;flex:1;min-height:0}
.ps-pad.tight{gap:.42em;padding-top:3cqw}
.ps-eye{font-size:.62em;font-weight:600;letter-spacing:.11em;text-transform:uppercase;color:#A99C92}
.ps-eye.lt{color:rgba(255,255,255,.85)}.ps-eye.dk{color:#6B5E55;letter-spacing:.05em}
.ps-hi{display:flex;justify-content:space-between;align-items:center;margin-top:-.35em}
.ps-h1{font-size:1.3em;font-weight:600}
.ps-h2{font-size:1.08em;font-weight:600;line-height:1.2}
.ps-h3{font-size:.86em;font-weight:600}
.ps-av{width:1.75em;height:1.75em;border-radius:50%;background:linear-gradient(135deg,#C44A3E,#8B2A3E);color:#fff;font-size:.72em;font-weight:700;display:grid;place-items:center}
.ps-check{background:#FBF4EC;border:1px solid #F0E3D6;border-radius:.9em;padding:.75em .7em;display:flex;flex-direction:column;gap:.5em}
.ps-q{font-size:.78em;font-weight:600}.ps-q em{font-weight:400;color:#A99C92;font-style:normal;font-size:.85em}
.ps-chips{display:flex;flex-wrap:wrap;gap:.3em}
.ps-chips span{display:inline-flex;align-items:center;gap:.35em;background:#fff;border-radius:2em;padding:.42em .85em;font-size:.56em;font-weight:600;color:#6B5E55;box-shadow:0 .08em .3em rgba(110,60,30,.08)}
.ps-chips.sm span{font-size:.5em;padding:.34em .7em}
.d{display:block;width:.6em;height:.6em;border-radius:50%}.d.y{background:#E8B24A}.d.b{background:#6E9CC8}.d.g{background:#9BB8A8}.d.o{background:#E79A72}.d.m{background:#C9BFB6}
.ps-btn{display:block;text-align:center;background:#D0703C;color:#fff;font-weight:600;font-size:.7em;border-radius:2em;padding:.62em}
.ps-btn.rd{background:#8B2A3E;border-radius:2em;padding:.8em;margin-top:auto;margin-bottom:9cqw}
.ps-modes{display:grid;grid-template-columns:repeat(3,1fr);gap:.45em}
.ps-modes span{border-radius:.8em;padding:.6em .5em .55em;display:flex;flex-direction:column;gap:.5em}
.ps-modes .m1{background:#FBF1DE}.ps-modes .m2{background:#E7EEF6}.ps-modes .m3{background:#FBE6E3}
.ps-modes em{font-style:normal;font-weight:600;font-size:.66em}
.pi{display:grid;place-items:center;width:1.7em;height:1.7em;border-radius:.5em;background:#fff}.pi svg{width:1em;height:1em}
.ps-modes .pi{box-shadow:0 .1em .3em rgba(0,0,0,.05)}
.c-or svg{fill:#D58A2C;stroke:#D58A2C}.c-bl{color:#6E9CC8}.c-rd{color:#C9645A}
.c-or svg[fill="none"]{fill:none}
.ps-feat{position:relative;border-radius:1em;background:linear-gradient(160deg,#B7D5EE 0%,#7FA9D4 45%,#3F6FA6 100%);color:#fff;padding:3em .8em 6.4em;overflow:hidden;flex:1;min-height:10em;display:flex;flex-direction:column;justify-content:flex-end;gap:.25em}
.ps-feat-ic{position:absolute;right:.6em;top:.7em;width:3.6em;height:3.6em;color:rgba(255,255,255,.65)}.ps-feat-ic svg{width:100%;height:100%}
.ps-feat .ps-eye{font-size:.48em;letter-spacing:.08em}
.ps-feat-t{font-size:.9em;font-weight:600}.ps-feat-s{font-size:.55em;opacity:.85;line-height:1.35}
.ps-tabs{position:absolute;left:7cqw;right:7cqw;bottom:4cqw;z-index:3;background:#FCF8F3;border-radius:3em;box-shadow:0 .25em .8em rgba(60,30,20,.18),inset 0 0 0 1px rgba(255,255,255,.8);display:grid;grid-template-columns:1.15fr 1fr 1fr;align-items:center;padding:.26em;gap:.15em}
.ps-tabs > span{display:flex;flex-direction:column;align-items:center;gap:.08em;padding:.36em 0 .3em;color:#B3A69B;border-radius:2.5em}
.ps-tabs > span .pi{background:none;width:1.12em;height:1.12em;border-radius:0;color:inherit}
.ps-tabs > span .pi svg{width:1.12em;height:1.12em}
.ps-tabs em{font-style:normal;font-size:.5em;font-weight:600;color:inherit}
.ps-tabs > span.on{background:linear-gradient(135deg,#C9583F,#8B2A3E);color:#fff;box-shadow:0 .1em .3em rgba(139,42,62,.3)}
.ps-tabs.dim > span.on{opacity:.85}
.ps-hero{position:relative;height:46%;flex:none;margin-top:-9cqw}
.ps-hero.or{background:linear-gradient(180deg,#E7914F 0%,#CE6A2E 38%,#C7836D 68%,#F7EFE7 100%)}
.ps-hero.bl{height:40%;background:linear-gradient(180deg,#8DB6DF 0%,#6F9BCB 45%,#B7CDE4 78%,#F7EFE7 100%)}
.ps-hero-spark{position:absolute;left:50%;top:52%;translate:-50% -50%;width:5em;height:5em}.ps-hero-spark svg{width:100%;height:100%;fill:rgba(255,226,200,.55)}
.ps-hero-orb{position:absolute;left:50%;top:50%;translate:-50% -50%;width:3.1em;height:3.1em;border-radius:50%;background:rgba(255,255,255,.28);display:grid;place-items:center;color:#fff}.ps-hero-orb svg{width:1.4em;height:1.4em}
.ps-dash{display:flex;gap:.35em;margin-top:.4em}.ps-dash i{flex:1;height:.16em;border-radius:.2em;background:#EADFD4}.ps-dash i.on{background:#D0703C}
.ps-low{margin-top:auto;margin-bottom:9cqw;display:flex;flex-direction:column;gap:.55em}
.ps-big{font-size:1.3em;font-weight:600;line-height:1.18}
.ps-top{display:flex;justify-content:space-between;align-items:center;margin-top:.4em}
.ps-x{width:1.35em;height:1.35em;border-radius:50%;background:#fff;display:grid;place-items:center;color:#B8404A;box-shadow:0 .1em .3em rgba(0,0,0,.08)}.ps-x svg{width:.7em;height:.7em}
.ps-x.or{background:none;box-shadow:none;color:#D0703C}.ps-x.or svg{width:.9em;height:.9em}
.ps-orb{align-self:center;margin-top:2.2em;width:7.2em;height:7.2em;border-radius:50%;background:radial-gradient(circle at 40% 35%,#9CC0E4,#4F7FB5 70%,#3B67A0);box-shadow:0 0 0 .5em rgba(111,155,203,.15),0 .8em 1.6em rgba(63,111,166,.35);display:grid;place-items:center}
.ps-orb span{width:2.6em;height:2.6em;border-radius:50%;background:rgba(255,255,255,.25);display:grid;place-items:center;color:#fff}.ps-orb svg{width:1.3em;height:1.3em}
.ps-mid{text-align:center;font-size:.86em;font-weight:600;margin-top:1.1em}
.ps-time{text-align:center;font-size:.6em;color:#6B5E55}
.ps-pace{text-align:center;font-size:.64em;color:#C4633A;padding:0 1.5em}
.ps-dots{display:flex;justify-content:center;gap:.25em}.ps-dots i{width:.3em;height:.3em;border-radius:50%;background:#E7D8CB}.ps-dots i.on{width:.9em;border-radius:.2em;background:#D0703C}
.ps-input{background:#fff;border:1px solid #EEE2D7;border-radius:2em;padding:.6em 1em;font-size:.56em;color:#B5A89E}
.ps-sub{font-size:.66em;color:#8A7D73;line-height:1.35}
.ps-grid{display:grid;grid-template-columns:1fr 1fr;gap:.45em;margin-top:.5em}
.ps-grid span{background:#fff;border-radius:.6em;padding:.55em .5em;display:flex;align-items:center;gap:.45em;font-size:.58em;font-weight:600;line-height:1.2;box-shadow:0 .08em .3em rgba(110,60,30,.06)}
.ps-grid .pi{width:2em;height:2em;flex:none;background:#F4ECE4}
.ps-foot{font-size:.62em;font-weight:600;line-height:1.35;margin-top:.6em}
.ps-goal{border-radius:.9em;padding:.8em;background:linear-gradient(135deg,#F2B45C,#E0874A);color:#fff;display:flex;flex-direction:column;gap:.35em}
.ps-goal-t{font-size:.84em;font-weight:600;line-height:1.2}
.ps-goal-pill{align-self:flex-start;background:rgba(255,255,255,.25);border-radius:1em;padding:.25em .6em;font-size:.5em;font-weight:600}
.ps-score{background:#fff;border-radius:.9em;padding:.7em .5em .4em;display:grid;grid-template-columns:1fr auto 1fr;align-items:center;text-align:center}
.ps-score div{display:flex;flex-direction:column;align-items:center;gap:.15em}
.ps-score b{font-size:1.25em;color:#C4633A}.ps-score b.bl{color:#4F7FB5}.ps-score em{font-style:normal;font-size:.48em;color:#8A7D73}
.ps-score .vs{font-size:.5em;color:#A99C92}
.ps-avs{display:flex}.ps-avs i{width:.9em;height:.9em;border-radius:50%;border:.1em solid #fff;background:#C4633A;margin-left:-.25em}.ps-avs i:nth-child(2){background:#8B2A3E}.ps-avs i:nth-child(3){background:#E2A64A}
.ps-avs.bl i{background:#6E9CC8}.ps-avs.bl i:nth-child(2){background:#3F6FA6}.ps-avs.bl i:nth-child(3){background:#9BB8A8}
.ps-prog{display:block;height:.3em;border-radius:.3em;background:#EADFD4;overflow:hidden}.ps-prog i{display:block;width:58%;height:100%;background:linear-gradient(90deg,#8B2A3E,#C4633A)}
/* wireframes */
.ph.wf .ph-scr{background:#fff;border-width:3cqw;border-radius:14cqw;color:#111;font-family:Arial,Helvetica,sans-serif}
.wf-tabs{display:flex;gap:.8em;align-items:center;font-size:.62em;margin-top:.3em}.wf-tabs .on{text-decoration:underline}
.wf-post{border:1px solid #bbb;padding:.5em;display:flex;flex-direction:column;gap:.25em}
.wf-t{font-size:.6em;font-weight:700}.wf-s{font-size:.48em;color:#666}
.wf-img{display:block;height:4.6em;border:1px solid #9a9a9a}.wf-img svg{width:100%;height:100%;display:block}
.wf-l{display:block;height:.35em;background:#ddd}.wf-l.wf-short{width:60%}
.wf-head{font-size:.7em;text-align:center;text-decoration:underline;margin-top:.3em}
.wf-q{font-size:.56em;margin-top:.5em}
.wf-field{display:block;height:1.2em;border:1px solid #999;border-radius:.3em}
.wf-slider{display:block;height:.15em;background:#999;position:relative;margin:.5em 0}.wf-slider i{position:absolute;left:0;top:-.3em;width:.7em;height:.7em;border-radius:50%;background:#111}
.wf-fig{width:55%;align-self:center;margin-top:.6em}
'''

# Scope every rule under .project .ph so the site's general text styles (e.g. `.project p`) never override the phone.
import re as _re
def _scope(css):
    css=_re.sub(r'/\*.*?\*/','',css,flags=_re.S)
    def fix(m):
        sels=[]
        for sel in m.group(1).split(','):
            sel=sel.strip()
            if not sel: continue
            sels.append('.project '+sel if sel.startswith('.ph') else '.project .ph '+sel)
        return ','.join(sels)+'{'+m.group(2)+'}'
    return _re.sub(r'([^{}]+)\{([^{}]*)\}',fix,css)
CSS = '.project .ph-scr p,.project .ph-scr span{font-size:inherit;line-height:inherit;color:inherit;letter-spacing:normal;margin:0;max-width:none}\n' + _scope(CSS)
