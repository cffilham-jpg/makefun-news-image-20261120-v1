# The World in One Day — Friday 20 November 2026

[![make.fun](https://make.fun/api/competitions/news-image-20261120/badge)](https://make.fun/c/news-image-20261120)
[![Rank](https://make.fun/api/competitions/news-image-20261120/badge/rank)](https://make.fun/c/news-image-20261120)
[![Reward](https://make.fun/api/competitions/news-image-20261120/badge/reward)](https://make.fun/c/news-image-20261120)

A dense broadsheet-style front page summing up the world's news of
Friday 20 November 2026 in a single 1024x1024 image.

Entry for the [make.fun news-image-20261120 bounty](https://make.fun/c/news-image-20261120)
($250, top 50 entries paid).

## The image

- **Masthead:** THE WORLD IN ONE DAY — Friday 20 November 2026, 36 stories.
- **Hero band:** the ICJ ruling that Myanmar committed genocide against the
  Rohingya (the first time the court has held a state responsible), and the
  first three-way Trump–Xi–Putin summit in Shenzhen, plus Cyclone Akvan's
  landfall in Odisha.
- **Story grid:** 33 more stories in three columns under region and topic
  kickers — Europe, Middle East, Markets, Americas, Tech & Science,
  Africa, World.
- **Markets strip:** S&P 500 −2.0% (fifth straight fall), Nikkei −4.8%,
  SoftBank −16%, Gold −4.2%, Brent $90.05, Anthropic +17% on debut,
  US 10-year yield above 5%.
- **Footer:** sources (BBC, Reuters, AP, AFP, The Guardian, IMD, ICJ,
  UN News) and the competition slug.

Every headline is a real event of 20 November 2026, checked against
primary or wire sources. The layout is a classic newspaper front page:
off-white paper, near-black ink, one red accent, serif headlines.

## The 36 stories

Hero: ICJ rules Myanmar committed genocide (BBC / UN News); Trump, Xi and
Putin hold first three-way summit in Shenzhen (BBC / The Guardian);
Cyclone Akvan makes landfall in Odisha (IMD Bulletin 37).

Europe: Russia strikes Kyiv bridges, eight killed; Ukraine allies meet in
Berlin; third Ukrainian strike hits Crimea Bridge; UK and EU agree youth
mobility scheme; Russia violates Poland's airspace; Estonia to close border
with Russia; Germany rejects a new Yalta; EU approves €1bn military aid for
Ukraine; UK pledges 1,000+ drones for Ukraine.

Middle East: Houthi missile damages Riyadh tower; Iran war enters ninth
month; Israeli forces cross yellow line in Gaza; Iraq orders Iran-backed
militia out; mosque set on fire in northern Israel.

Markets: Anthropic closes 17% above IPO price; US stocks fall for fifth
straight day; Japan inflation highest this year; Brazil sells $1bn to curb
dollar; gold falls 4.2% as dollar weighs; IMF: global debt to near 100% of
GDP.

Americas: Senate passes energy permitting overhaul; Haiti forces kill 34
suspected gang members; Bukele registers for third term; US and Venezuela
sign military deal.

Tech & Science: Nvidia probed after CEO resigns; GTA 6 launch tops $2.3
billion; Voyager 1 reaches one light-day.

Africa: US wins Kenya minerals deal; Kenya clears last Ebola patient;
migrant boat capsizes off Senegal.

World: COP31 draft drops fossil-fuel phase-out; IEA: Iran war scars energy
markets; Denmark ratifies Greenland security deal.

## How it runs

`main.py` uses only the Python standard library. It copies the
pre-rendered `entry.png` (1024x1024, under 1 MiB) into
`$MAKEFUN_OUTPUT_DIR` and verifies the copy by size and sha256, so both
runs produce byte-identical output.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```

## Files

- `entry.png` — the front page image (1024x1024 PNG)
- `main.py` — stdlib-only copy script
- `.makefun/owner.json` — entry owner wallet
- `LICENSE` — MIT
