# Piss-off-Microsoft and Google
Curated host-based blocklists aimed at silencing Microsoft, Google and other
telemetry or advertising domains. Think of them as digital duct tape that keeps
your computer from tattling about your every click. With these lists in place,
Windows update beacons, OneDrive callbacks, Office clickstream collection, ad
servers and other analytics noise quietly vanish into the void.

## List Maintenance
The blocklists in this repository are periodically refreshed from upstream
sources and curated by the community. Import them into AdGuard Home, Pi-hole or
uBlock Origin to cut down unwanted telemetry.

## Block Lists

Below is a brief description of each list provided in this repository and what it is used for.

- **Microsoft_Telemetry_Blocklist.txt** – Because Windows loves to tattle, this mega-list tries to muzzle every nosy domain Microsoft dreams up and now includes the former Slim Telemetry rules.
- **General_Blocking_Rules.txt** – A sampler platter of the biggest trackers from across the web—perfect for a no-fuss privacy boost, and now covering Google Gemini endpoints.
- **Samsung_Tracker_Blocklist_Cleaned.txt** – Tell your Galaxy phone to quit gossiping with Samsung's servers and enjoy some peace and quiet.
- **Advertising_Network_Blocklist.txt** – Blocks Google ad servers, mobile game ad networks, and other major advertising networks, plus the entries from the former Core Blocking List.
- **Adult_Content_Blocklist.txt** – Keeps your network squeaky clean by sweeping away domains you'd rather not explain to grandma.
- **Common_Services_Allowlist.txt** – Consolidated allowlist for Amazon, Meta, gaming, smart home, UniFi, writing AI, and other essential services.

## Direct Raw Links
Skip the browsing—grab any list directly:

- [Microsoft_Telemetry_Blocklist.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/Microsoft_Telemetry_Blocklist.txt)
- [General_Blocking_Rules.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/General_Blocking_Rules.txt)
- [Samsung_Tracker_Blocklist_Cleaned.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/Samsung_Tracker_Blocklist_Cleaned.txt)
- [Advertising_Network_Blocklist.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/Advertising_Network_Blocklist.txt)
- [Adult_Content_Blocklist.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/Adult_Content_Blocklist.txt)
- [Common_Services_Allowlist.txt](https://raw.githubusercontent.com/talonric332/Piss-off-Microsoft/main/Common_Services_Allowlist.txt)

## Using These Lists
Use the raw links above to grab any list and import it into your ad blocker of choice. Many folks just paste them into AdGuard Home, Pi-hole, or uBlock Origin. Check back often—Microsoft loves to roll out new endpoints. If you're on AdGuard Home, set your filter update interval to **1 hour** so you always fetch the latest changes.

## About This Project
Piss-off-Microsoft and Google is an open-source effort to reclaim a bit of
privacy by blocking known tracking domains. The lists are in the public domain
under the CC0 license and rely on community contributions. We have no
affiliation with Microsoft, Google or any other company—just a shared desire to
mute intrusive telemetry.

## Releases
Current version: **v1.3.2**
These blocklists are updated regularly. Grab the latest release from the GitHub releases page.

