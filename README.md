# Piss-off-Microsoft and Google
Blocklist to obliterate Microsoft Copilot, Bing, and telemetry.

## What Luckless Does
Luckless merges and maintains host-based blocklists aimed at shutting off Microsoft and Google tracking. The lists can be used with tools like AdGuard Home, Pi-hole, or uBlock Origin to keep unwanted telemetry at bay.

## Block Lists

Below is a brief description of each list provided in this repository and what it is used for.

- **Microsoft_Tracking_Blocklist.txt** – The main "Piss off Microsoft" list that blocks Copilot, Bing AI, and other invasive Microsoft services.
- **Slimmed_Microsoft_Blocklist.txt** – A lighter Microsoft telemetry blocklist which keeps core Office apps and licensing working.
- **General_Blocking_Rules.txt** – Generic tracking and analytics domains that typically do not affect essential functionality.
- **Samsung_Tracker_Blocklist_Cleaned.txt** – HaGeZi's list targeting Samsung's built‑in tracking services.
- **Mobile_Game_Ads_Blocklist.txt** – Blocks common mobile game ad networks such as Unity Ads, AppLovin, and Vungle.
- **Adult_Content_Blocklist.txt** – Blocks popular adult content domains.
- **Google_Gemini_Blocklist.txt** – Blocks Google Gemini (formerly Bard) AI endpoints and related services.
- **Meta_Allowlist.txt** – Whitelist rules to permit Facebook domains when using these blocklists.
- **Home_Automation_Allowlist.txt** – Whitelist rules to keep Lennox, Ring, Nest, and TP-Link services accessible.

## Using These Lists
Copy the raw text of any blocklist into your ad blocker of choice. Most folks just paste it into AdGuard Home, Pi-hole, or uBlock Origin. Update regularly—Microsoft has a habit of spawning new endpoints like rabbits.

## Why So Serious?
Sure, the repo name is a bit cheeky, but the goal is simple: reclaim a little privacy. If our lists help you out and make you chuckle, that's a win-win.

For a friendly overview, check out [index.md](./index.md).
