# The Web Archive Awesome Graph (WAAG)

## Contents

- [Training/Documentation]()
- [Resources for Web Publishers]()
- [Web Archiving Service Providers]()
  - [Self-hostable, Open Source]()
  - [Hosted, Closed Source]()
- [Community Resources]()
  - [Mailing Lists]()
  - [Other Awesome Lists]()
  - [Slack]()
  - [Twitter]()
  - [Blogs and Scholarship]()
- [Tools & Software]()
  - [Curation]()
  - [Utilities]()
  - [Replay]()
  - [Search & Discovery]()
  - [Analysis]()
  - [Quality Assurance]()
  - [WARC I/O Libraries]()
  - [Acquisition]()


## Training/Documentation



## Resources for Web Publishers

These resources can help when working with individuals or organisations who
publish on the web, and who want to make sure their site can be archived.
- [Definition of Web Archivability](https://nullhandle.org/web-archivability/index.html) - This describes the ease with which web content can be preserved. (


## Web Archiving Service Providers

The intention is that we only list services that allow web archives to be
exported in standard formats (WARC or WACZ). But this is not an endorsement of
these services, and readers should check and evaluate these options based on
their needs.


### Self-hostable, Open Source

- [Conifer](https://conifer.rhizome.org/) - From 
- [Browsertrix](https://webrecorder.net/browsertrix/) - From 

### Hosted, Closed Source

- [Archive-It](https://archive-it.org/) - From the Internet Archive.
- [Arkiwera](https://arkiwera.se/wp/websites/) 
- [Hanzo](https://www.hanzo.co/chronicle) 
- [MirrorWeb](https://www.mirrorweb.com/solutions/capabilities/website-archiving) 
- [PageFreezer](https://www.pagefreezer.com/) 
- [Smarsh](https://www.smarsh.com/platform/compliance-management/web-archive) 

## Community Resources



### Mailing Lists

- [IIPC](http://netpreserve.org/about-us/iipc-mailing-list/) 
- [Common Crawl](https://groups.google.com/g/common-crawl) 
- [OpenWayback](https://groups.google.com/g/openwayback-dev) 
- [WASAPI](https://groups.google.com/g/wasapi-community) 

### Other Awesome Lists

- [The Web Crawl section of COPTR](http://coptr.digipres.org/Category:Web_Crawl) 
- [The WARC Ecosystem](http://www.archiveteam.org/index.php?title=The_WARC_Ecosystem) 
- [Awesome Memento](https://github.com/machawk1/awesome-memento) 
- [Web Archiving Community](https://github.com/pirate/ArchiveBox/wiki/Web-Archiving-Community) 

### Slack

- [Archivers Slack](https://archivers.slack.com) 
- [Archives Unleashed Slack](https://archivesunleashed.slack.com/) 
- [Common Crawl Foundation Partners](https://ccfpartners.slack.com/) 
- [IIPC Slack](https://iipc.slack.com/) - Ask 

### Twitter

- [@NetPreserve](https://twitter.com/NetPreserve) - Official IIPC handle.
- [@WebSciDL](https://twitter.com/WebSciDL) - ODU Web Science and Digital Libraries Research Group.
- [#WebArchiveWednesday](https://twitter.com/hashtag/webarchivewednesday) 
- [#WebArchiving](https://twitter.com/search?q=%23webarchiving) 

### Blogs and Scholarship

- [DSHR's Blog](https://blog.dshr.org/) - David Rosenthal regularly reviews and summarizes work done in the Digital Preservation field.
- [UK Web Archive Blog](https://blogs.bl.uk/webarchive/) 
- [Common Crawl Foundation Blog](https://commoncrawl.org/blog) 
- [IIPC Blog](https://netpreserveblog.wordpress.com/) 
- [Web Archiving Roundtable](https://webarchivingrt.wordpress.com/) - Unofficial blog of the Web Archiving Roundtable of the 
- [WS-DL Blog](https://ws-dl.blogspot.com/) - Web Science and Digital Libraries Research Group blogs about various Web archiving related topics, scholarly work, and academic trip reports.
- [The Web as History](https://www.uclpress.co.uk/products/84010) - An open-source book that provides a conceptual overview to web archiving research, as well as several case studies.

## Tools & Software

This list of tools and software is intended to briefly describe some of the most
important and widely-used tools related to web archiving. For more details, we
recommend you refer to (and contribute to!) these excellent resources from other
groups:
- [Comparison of web archiving software](https://github.com/archivers-space/research/tree/master/web_archiving)  💽
- [Awesome Website Change Monitoring](https://github.com/edgi-govdata-archiving/awesome-website-change-monitoring)  💽 ⭐ 505 👀 30


### Curation

- [Zotero Robust Links Extension](https://robustlinks.mementoweb.org/zotero/) - A  💽

### Utilities

- [cdx-toolkit](https://pypi.org/project/cdx-toolkit/) - Library and CLI to consult cdx indexes and create WARC extractions of subsets. Abstracts away Common Crawl's unusual crawl structure.  💽
- [Go Get Crawl](https://github.com/karust/gogetcrawl) - Extract web archive data using  💽 ⭐ 155 👀 3
- [gowarcserver](https://github.com/nlnwa/gowarcserver)  💽 ⭐ 16 👀 6
- [ArchiveTools](https://github.com/recrm/ArchiveTools) - Collection of tools to extract and interact with WARC files (Python). 💽 ⭐ 73 👀 5
- [har2warc](https://github.com/webrecorder/har2warc) - Convert HTTP Archive (HAR) -> Web Archive (WARC) format (Python). 💽 ⭐ 51 👀 6

### Replay

- [OpenWayback](https://github.com/iipc/openwayback/) - The open source project aimed to develop Wayback Machine, the key software used by web archives worldwide to play back archived websites in the user's browser.  💽
- [Reconstructive](https://oduwsdl.github.io/Reconstructive/) - Reconstructive is a ServiceWorker module for client-side reconstruction of composite mementos by rerouting resource requests to corresponding archived copies (JavaScript). 💽
- [ReplayWeb.page](https://webrecorder.net/replaywebpage/) - A browser-based, fully client-side replay engine for both local and remote WARC & WACZ files. Also available as an Electron based desktop application.  💽
- [warc2html](https://github.com/iipc/warc2html) - Converts WARC files to static HTML suitable for browsing offline or rehosting. 💽 ⭐ 44 👀 10
- [InterPlanetary Wayback (ipwb)](https://github.com/oduwsdl/ipwb) - Web Archive (WARC) indexing and replay using  💽 ⭐ 625 👀 22
- [PYWB](https://github.com/webrecorder/pywb) - A Python 3 implementation of web archival replay tools, sometimes also known as 'Wayback Machine'.  💽 ⭐ 1484 👀 60

### Search & Discovery

- [Tempas v1](http://tempas.L3S.de/v1) - Temporal web archive search based on  💽
- [Tempas v2](http://tempas.L3S.de/v2) - Temporal web archive search based on links and anchor texts extracted from the German web from 1996 to 2013 (results are not limited to German pages, e.g.,  💽
- [Mink](https://github.com/machawk1/mink) - A  💽 ➡️ moved to https://github.com/machawk1/Mink
- [SecurityTrails](https://securitytrails.com/) - Web based archive for WHOIS and DNS records. REST API available free of charge. 💽
- [PANDORÆ](https://github.com/Guillaume-Levrier/PANDORAE) - A desktop research software to be plugged on a Solr endpoint to query, retrieve, normalize and visually explore web archives.  💽 ⭐ 12 👀 2
- [hyphe](https://github.com/medialab/hyphe) - A webcrawler built for research uses with a graphical user interface in order to build web corpuses made of lists of web actors and maps of links between them.  💽 ⭐ 350 👀 31
- [webarchive-discovery](https://github.com/ukwa/webarchive-discovery) - WARC and ARC full-text indexing and discovery tools, with a number of associated tools capable of using the index shown below.  💽 ⭐ 123 👀 23
- [playback](https://github.com/wabarc/playback) - A toolkit for searching archived webpages from  💽 ⭐ 8 👀 3

### Analysis

- [Web Data Commons](http://webdatacommons.org/) - Structured data extracted from Common Crawl.  💽
- [Common Crawl Web Graph](https://commoncrawl.org/category/web-graph/) - A host or domain-level graph of the web, with ranking information.  💽
- [Common Crawl Columnar Index](https://commoncrawl.org/tag/columnar-index/) - SQL-queryable index, with CDX info plus language classification.  💽
- [Archives Unleashed Toolkit](https://github.com/archivesunleashed/aut) - Archives Unleashed Toolkit (AUT) is an open-source platform for analyzing web archives with Apache Spark.  💽 ⭐ 143 👀 14
- [Archives Unleashed Notebooks](https://github.com/archivesunleashed/notebooks) - Notebooks for working with web archives with the Archives Unleashed Toolkit, and derivatives generated by the Archives Unleashed Toolkit.  💽 ⭐ 26 👀 5
- [Tweet Archvies Unleashed Toolkit](https://github.com/archivesunleashed/twut) - An open-source toolkit for analyzing line-oriented JSON Twitter archives with Apache Spark.  💽 ⭐ 9 👀 3
- [Common Crawl Jupyter notebooks](https://github.com/commoncrawl/cc-notebooks) - A collection of notebooks using Common Crawl's various datasets.  💽 ⭐ 52 👀 17
- [ArchiveSpark](https://github.com/helgeho/ArchiveSpark) - An Apache Spark framework (not only) for Web Archives that enables easy data processing, extraction as well as derivation.  💽 ⭐ 148 👀 15
- [Archives Research Compute Hub](https://github.com/internetarchive/arch) - Web application for distributed compute analysis of Archive-It web archive collections.  💽 ⭐ 17 👀 20

### Quality Assurance

- [Xenu](http://home.snafu.de/tilman/xenulink.html) - Desktop link checker for Windows. 💽
- [WineBottler](http://winebottler.kronenberg.org/) - For running Xenu and Notepad++ on macOS. 💽
- [Chrome link gopher](https://chrome.google.com/webstore/detail/bpjdkodgnbfalgghnbeggfbfjpcfamkf/publish-accepted?hl=en-US&gl=US) - Browser extension: link harvester on a page. 💽
- [Chrome Check My Links](https://chrome.google.com/webstore/detail/check-my-links/ojkcdipcgfaekbeaelaapakgnjflfglf) - Browser extension: a link checker with more options. 💽
- [Chrome link checker](https://chrome.google.com/webstore/detail/link-checker/aibjbgmpmnidnmagaefhmcjhadpffaoi) - Browser extension: basic link checker. 💽
- [Chrome Open Multiple URLs](https://chrome.google.com/webstore/detail/open-multiple-urls/oifijhaokejakekmnjmphonojcfkpbbh?hl=de) - Browser extension: opens multiple URLs and also extracts URLs from text. 💽
- [Chrome Revolver](https://chrome.google.com/webstore/detail/revolver-tabs/dlknooajieciikpedpldejhhijacnbda) - Browser extension: switches between browser tabs. 💽
- [FlameShot](https://github.com/lupoDharkael/flameshot) - Screen capture and annotation on Ubuntu. 💽 ➡️ moved to https://github.com/flameshot-org/flameshot
- [Windows Snipping Tool](https://support.microsoft.com/en-gb/help/13776/windows-use-snipping-tool-to-capture-screenshots) - Windows built-in for partial screen capture and annotation. On macOS you can use Command + Shift + 4 (keyboard shortcut for taking partial screen capture). 💽
- [PlayOnLinux](https://www.playonlinux.com/en/) - For running Xenu and Notepad++ on Ubuntu. 💽
- [PlayOnMac](https://www.playonmac.com/en/) - For running Xenu and Notepad++ on macOS. 💽
- [xDoTool](https://github.com/jordansissel/xdotool) - Click automation on Ubuntu. 💽 ⭐ 3448 👀 62

### WARC I/O Libraries

- [node-warc](https://github.com/N0taN3rd/node-warc) - Parse WARC files or create WARC files using either  💽 ⭐ 97 👀 8
- [FastWARC](https://github.com/chatnoir-eu/chatnoir-resiliparse) - A high-performance WARC parsing library (Python). 💽 ⭐ 102 👀 8
- [Warcat](https://github.com/chfoo/warcat) - Tool and library for handling Web ARChive (WARC) files (Python).  💽 ⭐ 156 👀 10
- [Warcat-rs](https://github.com/chfoo/warcat-rs) - Command-line tool and Rust library for handling Web ARChive (WARC) files.  💽 ⭐ 15 👀 1
- [Unwarcit](https://github.com/emmadickson/unwarcit) - Command line interface to unzip WARC and WACZ files (Python). 💽 ⭐ 10 👀 4
- [HadoopConcatGz](https://github.com/helgeho/HadoopConcatGz) - A Splitable Hadoop InputFormat for Concatenated GZIP Files (and  💽 ⭐ 9 👀 2
- [jwarc](https://github.com/iipc/jwarc) - Read and write WARC files with a type safe API (Java). 💽 ⭐ 48 👀 5
- [Sparkling](https://github.com/internetarchive/Sparkling) - Internet Archive's Sparkling Data Processing Library.  💽 ⭐ 13 👀 19
- [warctools](https://github.com/internetarchive/warctools) - Library to work with ARC and WARC files (Python). 💽 ⭐ 159 👀 43
- [Jwat](https://github.com/netarchivesuite/jwat) - Libraries for reading/writing/validating WARC/ARC/GZIP files (Java).  💽 ⭐ 3 👀 7
- [Jwat-Tools](https://github.com/netarchivesuite/jwat-tools) - Tools for reading/writing/validating WARC/ARC/GZIP files (Java).  💽 ⭐ 5 👀 6
- [webarchive](https://github.com/richardlehane/webarchive) - Golang readers for ARC and WARC webarchive formats (Golang). 💽 ⭐ 20 👀 7
- [warcio](https://github.com/webrecorder/warcio) - Streaming WARC/ARC library for fast web archive IO (Python).  💽 ⭐ 408 👀 21

### Acquisition

Mainly Crawling
- [WARCreate](http://matkelly.com/warcreate/) - A  💽
- [SiteStory](http://mementoweb.github.io/SiteStory/) - A transactional archive that selectively captures and stores transactions that take place between a web client (browser) and a web server.  💽
- [StormCrawler](http://stormcrawler.net/) - A collection of resources for building low-latency, scalable web crawlers on Apache Storm.  💽
- [Wget](http://www.gnu.org/software/wget/) - An open source file retrieval utility that of  💽
- [HTTrack](http://www.httrack.com/) - An open source website copying utility.  💽
- [Crawl](https://git.autistici.org/ale/crawl) - A simple web crawler in Golang.  💽
- [Wpull](https://github.com/chfoo/wpull) - A Wget-compatible (or remake/clone/replacement/alternative) web downloader and crawler.  💽 ➡️ moved to https://github.com/ArchiveTeam/wpull
- [twarc](https://github.com/docnow/twarc) - A command line tool and Python library for archiving Twitter JSON data.  💽 ➡️ moved to https://github.com/DocNow/twarc
- [DiskerNet](https://github.com/dosyago/DiskerNet) - A non-WARC-based tool which hooks into the Chrome browser and archives everything you browse making it available for offline replay.  💽 ➡️ moved to https://github.com/dosyago/dn
- [Heritrix](https://github.com/internetarchive/heritrix3/wiki) - An open source, extensible, web-scale, archival quality web crawler.  💽
- [ArchiveBox](https://github.com/pirate/ArchiveBox) - A tool which maintains an additive archive from RSS feeds, bookmarks, and links using wget, Chrome headless, and other methods (formerly  💽 ➡️ moved to https://github.com/ArchiveBox/ArchiveBox
- [crocoite](https://github.com/promyloph/crocoite) - Crawl websites using headless Google Chrome/Chromium and save resources, static DOM snapshot and page screenshots to WARC files.  💽 ➡️ moved to https://github.com/PromyLOPh/crocoite
- [Social Feed Manager](https://gwu-libraries.github.io/sfm-ui/) - Open source software that enables users to create social media collections from Twitter, Tumblr, Flickr, and Sina Weibo public APIs.  💽
- [Web Curator Tool](https://webcuratortool.org) - Open-source workflow management for selective web archiving.  💽
- [ArchiveWeb.Page](https://webrecorder.net/archivewebpage/) - A plugin for Chrome and other Chromium based browsers that lets you interactively archive web pages, replay them, and export them as WARC & WACZ files. Also available as an Electron based desktop application. 💽
- [Community Archive](https://www.community-archive.org/) - Open Twitter Database and API with tools and resources for building on archived Twitter data. 💽
- [grab-site](https://github.com/ArchiveTeam/grab-site) - The archivist's web crawler: WARC output, dashboard for all crawls, dynamic ignore patterns.  💽 ⭐ 1470 👀 41
- [Chronicler](https://github.com/CGamesPlay/chronicler) - Web browser with record and replay functionality.  💽 ⭐ 87 👀 5
- [Squidwarc](https://github.com/N0taN3rd/Squidwarc) - An  💽 ⭐ 170 👀 9
- [WebMemex](https://github.com/WebMemex) - Browser extension for Firefox and Chrome which lets you archive web pages you visit.  💽
- [freeze-dry](https://github.com/WebMemex/freeze-dry) - JavaScript library to turn page into static, self-contained HTML document; useful for browser extensions.  💽 ⭐ 294 👀 10
- [monolith](https://github.com/Y2Z/monolith) - CLI tool to save a web page as a single HTML file.  💽 ⭐ 13387 👀 63
- [Waybackpy](https://github.com/akamhy/waybackpy) -  Wayback Machine Save, CDX and availability API interface in Python and a command-line tool   💽 ⭐ 519 👀 10
- [Wget-lua](https://github.com/alard/wget-lua) - Wget with Lua extension.  💽 ⭐ 24 👀 3
- [Auto Archiver](https://github.com/bellingcat/auto-archiver) - Python script to automatically archive social media posts, videos, and images from a Google Sheets document. Read the  💽 ⭐ 687 👀 23
- [SingleFile](https://github.com/gildas-lormeau/SingleFile) - Browser extension for Firefox/Chrome and CLI tool to save a faithful copy of a complete page as a single HTML file.  💽 ⭐ 17305 👀 127
- [Obelisk](https://github.com/go-shiori/obelisk) - Go package and CLI tool for saving web page as single HTML file.  💽 ⭐ 278 👀 9
- [Scoop](https://github.com/harvard-lil/scoop) - High-fidelity, browser-based, single-page web archiving library and CLI for witnessing the web.  💽 ⭐ 156 👀 7
- [Web2Warc](https://github.com/helgeho/Web2Warc) - An easy-to-use and highly customizable crawler that enables anyone to create their own little Web archives (WARC/CDX).  💽 ⭐ 24 👀 3
- [Brozzler](https://github.com/internetarchive/brozzler) - A distributed web crawler (爬虫) that uses a real browser (Chrome or Chromium) to fetch pages and embedded urls and to extract links.  💽 ⭐ 699 👀 39
- [Warcprox](https://github.com/internetarchive/warcprox) - WARC-writing MITM HTTP/S proxy.  💽 ⭐ 401 👀 38
- [F(b)arc](https://github.com/justinlittman/fbarc) - A commandline tool and Python library for archiving data from  💽 ⭐ 77 👀 15
- [WAIL](https://github.com/machawk1/wail) - A graphical user interface (GUI) atop multiple web archiving tools intended to be used as an easy way for anyone to preserve and replay web pages;  💽 ⭐ 372 👀 13
- [archivenow](https://github.com/oduwsdl/archivenow) - A  💽 ⭐ 420 👀 20
- [Warcworker](https://github.com/peterk/warcworker) - An open source, dockerized, queued, high fidelity web archiver based on Squidwarc with a simple web GUI.  💽 ⭐ 58 👀 5
- [html2warc](https://github.com/steffenfritz/html2warc) - A simple script to convert offline data into a single WARC file.  💽 ⭐ 21 👀 3
- [crau](https://github.com/turicas/crau) - crau is the way (most) Brazilians pronounce crawl, it's the easiest command-line tool for archiving the Web and playing archives: you just need a list of URLs.  💽 ⭐ 61 👀 3
- [Cairn](https://github.com/wabarc/cairn) - A npm package and CLI tool for saving webpages.  💽 ⭐ 47 👀 4
- [Wayback](https://github.com/wabarc/wayback) - A toolkit for snapshot webpage to Internet Archive, archive.today, IPFS and beyond.  💽 ⭐ 1930 👀 9
- [Browsertrix Crawler](https://github.com/webrecorder/browsertrix-crawler) - A Chromium based high-fidelity crawling system, designed to run a complex, customizable browser-based crawl in a single Docker container.  💽 ⭐ 746 👀 23
