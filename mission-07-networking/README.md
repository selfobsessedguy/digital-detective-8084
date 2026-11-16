# Mission 07 - Computer networks

## 1. Task / objective

The objective of Mission 07 was to understand how computer networks function. This included learning key networking concepts (LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, Client-server), observing how network diagnostic tools like ping and nslookup work while preserving privacy, and explaining step by step what happens behind the scenes when a user visits a website in a browser.

## 2. Work completed

I researched and defined all eight networking terms using simple analogies and everyday examples. I explored network diagnostic utilities used for connectivity checking and domain name resolution, noting what they show without exposing any private home network details. I then wrote a clear, seven-step breakdown describing how a web browser communicates with a web server over the internet.

Here is the detailed work:

### Task 7.1 - Explain network concepts

Concept 1: LAN (Local Area Network)
- Explanation in my own words: A network that connects computers and devices located in a small, localized physical area such as a single home, a school classroom, or an office room.
- Example: A home Wi-Fi network that connects a laptop, smartphone, and smart TV together.

Concept 2: MAN (Metropolitan Area Network)
- Explanation in my own words: A network that covers a larger geographic space like a whole town, city, or university campus with multiple buildings.
- Example: A university campus network linking libraries, student dorms, and lecture halls across a city.

Concept 3: WAN (Wide Area Network)
- Explanation in my own words: A vast network that spans across huge distances, connecting cities, states, countries, or the entire globe.
- Example: The global Internet, which connects billions of devices worldwide through satellite and undersea cables.

Concept 4: DNS (Domain Name System)
- Explanation in my own words: The directory or phonebook of the internet. It takes human-readable website names and translates them into the numeric IP addresses computers need to find servers.
- Example: Looking up the name example.com to get its numeric server IP address 93.184.215.14.

Concept 5: Router
- Explanation in my own words: A piece of networking hardware that connects different networks together. It looks at the destination address on incoming data packets and directs them on the best path.
- Example: The home Wi-Fi router box that connects your personal home devices to your Internet Service Provider.

Concept 6: Protocol
- Explanation in my own words: An agreed-upon set of rules and communication formats that computers and programs must follow so they can understand each other.
- Example: HTTPS (Hypertext Transfer Protocol Secure), which defines how encrypted web pages are requested and sent.

Concept 7: Packet switching
- Explanation in my own words: A technique where a large chunk of data (like a file or video) is chopped up into small individual packets. Each packet travels independently across the fastest available route through routers, and the receiving computer puts them back together.
- Example: Watching a streaming video where video frames travel over the internet in thousands of tiny numbered packets.

Concept 8: Client-server
- Explanation in my own words: A system structure where one device (the client) asks for information or a service, and a powerful central computer (the server) processes the request and responds with the data.
- Example: A laptop web browser (the client) asking for a search results page from Google web servers (the server).

### Task 7.2 - Observe network information

Diagnostic commands:
- Connectivity test command: ping -c 3 example.com
- DNS lookup command: nslookup example.com

Privacy-safe observations:
- Running nslookup example.com returns the domain name and the associated IPv4 address (such as 93.184.215.14) and IPv6 address (such as 2606:2800:21f:cb07:6820:80da:af6b:8b2c).
- All personal home IP addresses, router gateway addresses, and local Wi-Fi network names are kept private as [redacted] to follow security guidelines.

Answers to questions:
- What a connectivity test helps you check: A connectivity test like ping checks whether your computer can successfully reach a target machine over the network. It verifies that the network cable or Wi-Fi is working, that the destination server is online, and it shows the latency (how many milliseconds the round trip takes).
- What information a DNS lookup displays: A DNS lookup tool displays the domain name being investigated, the address of the DNS resolver answering the question, and the exact public IP addresses mapped to that domain.
- The role of DNS when you enter a website name in a browser: When a human types a name like example.com, computers cannot navigate using letters. The browser automatically asks a DNS server to translate that name into an IP address. Without DNS, people would have to memorize long strings of numbers for every website they ever visit.

### Task 7.3 - What happens when you open a website?

Step 1: The user opens a web browser (the client) and types a web address such as https://example.com and hits the Enter key.

Step 2: The browser client first checks its local cache, and if not found, asks a DNS server to translate the domain name into an IP address.

Step 3: The DNS server looks up its records and sends the numeric IP address back to the browser client.

Step 4: The client initiates an HTTPS connection using standard internet protocols and sends an HTTP GET request packet addressed to the server's IP address.

Step 5: The request packet travels out of the computer, through the local router, across the Internet Service Provider, and hops through multiple intermediate routers using packet switching until reaching the destination server.

Step 6: The web server receives the request, processes it, retrieves the web page files (HTML, CSS, images), and transmits them back across the network as response packets.

Step 7: The client receives all the response packets, verifies their integrity, reassembles them in the correct sequence, and the browser displays the rendered web page on the screen for the user.

## 3. Commands / tools used

- ping: network diagnostic tool used to test packet transmission and latency to a host.
- nslookup: network tool used to query DNS servers and find IP addresses for domain names.

## 4. My understanding

I learned that the internet is not one giant single wire, but rather a huge web of interconnected networks. The distinction between human-friendly names (domains) and machine addresses (IP addresses) was made crystal clear by DNS.

Understanding packet switching also helped me realize why internet connections are so resilient: if one router is busy or broken, packets can simply take another path and get reassembled at the end.

## 5. Difficulties faced

At first, I did not understand why pinging a domain like example.com might show latency or why we need both IP addresses and domain names.

## 6. How I resolved them

I thought of it like postal mail: the domain name is like a person's name, but the postal truck needs a street address (the IP address) to deliver the letter to the right house. DNS is like the phone directory that gives the street address.

## 7. Evidence / files

- Mission documentation: mission-07-networking/README.md

## 8. Commit details

Commit message: Explain networking concepts and website communication
Status: Committed to local git repository on branch main.
